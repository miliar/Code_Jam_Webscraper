#include <bits/stdc++.h>
 
using namespace std;
#define input freopen("in.txt","r",stdin)
#define output freopen("output.txt","w",stdout)
int main() {
	input;
	output;
	int t;
	cin>>t;
	int cases=1;
	while(t--){
		int n;cin>>n;
		string cad;cin>>cad;
		//cout<<cad<<endl;
		int sol=0,par=0;
		par+=(cad[0]-'0');
		for(int i=1;i<=n;i++){
			if(i>par && cad[i]!='0'){
			//	cout<<cad[i]<<endl;
				sol+=(i-par);
				par+=(i-par);
			}
			par+=(cad[i]-'0');
		}
		printf("Case #%d: %d\n",cases++,sol);
	}
}