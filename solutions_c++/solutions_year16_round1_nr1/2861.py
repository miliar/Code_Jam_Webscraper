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
#define ll long long
#define mp make_pair
#define pb push_back
#define ff first
#define ss second

int main(){
	ios_base::sync_with_stdio(false);
	int t, T=1;
	cin>>t;

	while(t--){
		string s, ans;
		cin>>s;

		int n = s.size();
		bool visited[n];

		for(int i=0 ; i<n ; i++)
			visited[i] = false;
		
		int l = 1, end = n;

		while(true){
			char last = '0';
			int index = -1;
			for(int i=0 ; i<end ; i++){
				if(visited[i])
					continue;
				if(s[i]>=last){
					last = s[i];
					index = i;
				}
			}

			if(index == -1)
				break;

			end = index;
			visited[index] = true;

			ans.pb(last);
		}
	
		for(int i=1 ; i<n ; i++)
			if(!visited[i])
				ans.pb(s[i]);

		cout<<"Case #"<<T++<<": "<<ans<<"\n";
	}

	return 0;
}