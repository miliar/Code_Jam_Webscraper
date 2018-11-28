#include <iostream>
#include <queue>
#include <string>
using namespace std;

#define DBG(x) cout<<#x<<" = "<<x<<"\n";

int main()
{
	int t,m,n,i,j,x,poc1;
	bool chyba,vysl;
	cin>>t;
	for(x=0;x<t;x++){
		cin>>n>>m;
		int pole[m][n];
		poc1=0;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				cin>>pole[j][i];
				if(pole[j][i]==1) poc1++;
			}
		}
		//riesenie
		for(i=0;i<m;i++){
			chyba=false;
			for(j=0;j<n;j++){ //zisti ci v celom stlpci su jednotky
				if(pole[i][j]==2) chyba=true;
			}
			if(chyba==false){
				for(j=0;j<n;j++){ //oznaci za vyriesene 1
				pole[i][j]=0;
			}}
		}
		for(i=0;i<n;i++){
			chyba=false;
			for(j=0;j<m;j++){ //zisti ci v celom stlpci su jednotky
				if(pole[j][i]==2) chyba=true;
			}
			if(chyba==false){
				for(j=0;j<m;j++){ //oznaci za vyriesene 1
				pole[j][i]=0;
			}}
		}
		vysl=true;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(pole[j][i]==1) vysl=false;
				//cout<<pole[j][i];

			}
			//cout<<endl;
		}
		cout<<"Case #"<<x+1<<": ";
		if(vysl) cout<<"YES";
		else cout<<"NO";
		cout<<"\n";
			
	}
}
