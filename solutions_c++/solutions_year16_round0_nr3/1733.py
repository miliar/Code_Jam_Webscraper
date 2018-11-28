#include <bits/stdc++.h>

using namespace std;
int main(){
//	freopen("c.out","w+t",stdout);
	int tc;
	cin>>tc;
	int n,j;
	cin>>n>>j;
	cout<<"Case #1:"<<endl;
	for(int i=0;i<j;i++){
		string ans="";
		for(int pw=0;pw<(n-4)/2;pw++){
			ans+=(i&(1<<pw))?"11":"00";
		}
		ans="11"+ans+"11";
		cout<<ans<<" 3 4 5 6 7 8 9 10 11\n";
	}
	return 0;
}
