#include <bits/stdc++.h> 
using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	int t, max, fr, sum, idx; cin>>t;
	for(int j=1; j<=t; j++){
		cout<<"Case #"<<j<<": ";
		cout.flush();
		cin>>max;
		string arr;
		fr = 0, sum = 0;

		cin>>arr;

		if(arr[0]==0)
			fr++, sum++;
		for(int k=1; k<=max; k++){
			sum+=(arr[k-1]-'0');
			if(sum-k < 0){
				fr++, sum++;
			}
		}
		cout<<fr<<endl;
	}
}