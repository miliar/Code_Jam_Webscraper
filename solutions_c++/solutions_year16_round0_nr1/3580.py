#include<bits/stdc++.h>
#include<fstream>

using namespace std;


int main(){
	ofstream archivo;
	archivo.open("codejamAlarge.out");
	int t;cin>>t;
	for(int i=1;i<=t;i++){
		int n;cin>>n;
		archivo<<"Case #"<<i<<": ";
		int caso[10]={0,0,0,0,0,0,0,0,0,0};
		if(n==0) archivo<<"INSOMNIA"<<endl;
		else{
			int j=n;
			//cout<<"prueba..."<<endl;
			for( n;n<=1000000000;n+=j){
				int aux=n;
				while(aux>0){
					caso[aux%10]=1;aux/=10;
				}
			//	cout<<n<<endl;
				if((caso[0] + caso[1] + caso[2] + caso[3] + caso[4] + caso[5] + caso[6] + caso[7] + caso[8] + caso[9] ) == 10) {archivo<<n<<endl;break;}
			}
		}
	}
	archivo.close();
}

