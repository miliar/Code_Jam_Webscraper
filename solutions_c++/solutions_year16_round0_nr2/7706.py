#include<bits/stdc++.h>
using namespace std;

void solve(string &str,int n){
	for(int i=n; i>=0; i--)
	  if(str[i]=='-')
	     str[i]='+';
	  else
	     str[i]='-';
}



int main() {
	ios_base::sync_with_stdio(0);
	
	int tt,cc=1;
	cin>>tt;
	while(cc<=tt){
		string cake;
		cin>>cake;
		int l = cake.size();
		bool done = false;
		int ans = 0;
		
		while(!done){
			bool call_solve = false;
			int n=0;
			for(int i = l-1; i>=0; i-- ){
				if(cake[i]=='-'){
					n = i;
					call_solve = true;
					break;
				}
			}
			
			if(call_solve){
				solve(cake,n);
				ans++;
			}
			else{
				done = true;
			}
		}
		
		cout<<"Case #"<<cc<<": "<<ans<<"\n";
		cc++;
		
	}
	
	return 0;
}
