#include<bits/stdc++.h>
using namespace std;
#define vi vector<int> 
#define rep(i,j, n) for(int i=j; i<n; i++)
void solve(){
	string line;
	getline(cin, line);
	int count=0;
	int no=line.find_last_of("-");
	while(no!=-1){
		rep(i, 0, no+1){
			if(line[i]=='-'){
				line[i]='+';
			}
			else{
				line[i]='-';		
			}
		}
		count++;
		no=line.find_last_of("-");
	}
	cout << count <<endl;
}
main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	string w;
	getline(cin, w);
	rep(i,0, t){
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
	
}
