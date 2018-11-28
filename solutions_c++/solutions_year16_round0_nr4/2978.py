#include<bits/stdc++.h>
#include<fstream>

using namespace std;

int main(){
	ofstream archivo;
	archivo.open("codejamDsmall.out");
	int t;cin>>t;
	for(int i=1;i<=t;i++){
		archivo<<"Case #"<<i<<": ";
		int k,c,s;cin>>k>>c>>s;
		if(k==1) archivo<<"1";
		else{
			if(c==1){
				if(s<k) archivo<<"IMPOSSIBLE";
				else {
					for(int j=1;j<=k;j++){
						archivo<<j<<" ";
					}
				}
			}
			else{
				if(s<(k-1)) archivo<<"IMPOSSIBLE";
				else{
					for(int j=2;j<=k;j++){
						archivo<<j<<" ";
					}
				}
			}
		}
		archivo<<endl;
	}
	archivo.close();
}
