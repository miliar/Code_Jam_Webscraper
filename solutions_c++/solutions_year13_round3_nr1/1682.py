#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<sstream>
#include<queue>
#include<algorithm>
#include<string>
using namespace std;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int n;
	int tc;
	cin>>tc;
	string s;
	for(int i=1; i<=tc; i++){
		cin>>s>>n;
		string aux;
		int ans=0;
		for(int j=0; j<s.length(); j++){
			for(int l=1; l+j<=s.length(); l++){
				aux=s.substr(j,l);
				int cons=0;
				bool sirve=false;
				
				for(int c=0; c<aux.length(); c++){
					if(aux[c]!='a' && aux[c]!='e' && aux[c]!='i' & aux[c]!='o' && aux[c]!='u'){
						cons++;
					}			
					else{
						cons=0;
					}		
					if(cons>=n){
						sirve=true;						
						break;						
					}
				}
				if(sirve)
					ans++;
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}	
}
