#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <set>
#include <algorithm>

using namespace std;

#define MAX 100005
#define INF (ll)1e18
#define ll long long
#define mp make_pair
#define pb push_back
#define ff first
#define ss second

int def[3][3];
int a[(1<<15)];
string finalAnswer;

void solve(int node, int level){
	if(!level)
		return;
	int left, right;
	left = 2 * node, right = 2 * node + 1;

	if(a[node] == 0){
		a[left] = 0, a[right] = 2;
	} else if(a[node] == 1){
		a[left] = 1, a[right] = 0;
	} else {
		a[left] = 1, a[right] = 2;
	}

	solve(left, level - 1), solve(right, level - 1);
}

void minimize(string str){
	string left, right;
	int l = str.size();

	if(l == 1){
		finalAnswer.pb(str[0]);
		return;
	}

	for(int i=0 ; i<l/2 ; i++)
		left.pb(str[i]);
	for(int i=l/2 ; i<l ; i++)
		right.pb(str[i]);
	if(left>right)
		swap(left, right);
	minimize(left);
	minimize(right);
}	

int main(){
	ios_base::sync_with_stdio(false);
	int t, T=1;
	cin>>t;

	def[0][2] = def[1][0] = def[2][1] = 1;
	string order = "RPS";

	while(t--){
		int n;
		int arr[3];
		cin>>n;

		for(int i=0 ; i<3 ; i++)
			cin>>arr[i];

		int N = 1<<n;

		string ans = "";

		for(int i=0 ; i<3 ; i++){
			int node = 1;
			a[node] = i;
			solve(node, n);
			int index = (1<<n), cnt = 0;
			int tempArr[3];
			for(int j=0 ; j<3 ; j++)
				tempArr[j] = arr[j];
		
			bool flag = true;
			while(cnt<N){
				tempArr[a[index++]]--, cnt++;
			}

			for(int j=0 ; j<3 ; j++)
				if(tempArr[j] != 0)
					flag = false;
		
			if(flag){
				cnt = 0, index = (1<<n);
				string tempAns = "";
				while(cnt<N){
					tempAns.pb(order[a[index]]);
					index++, cnt++;
				}
				if(!ans.size())
					ans = tempAns;
				else if(tempAns<ans)
					ans = tempAns;
			}
		}

		finalAnswer = "";

		cout<<"Case #"<<T++<<": ";
		if(ans.size()){
			minimize(ans);
			cout<<finalAnswer<<"\n";
		} else
			cout<<"IMPOSSIBLE"<<"\n";

	}

	return 0;
}