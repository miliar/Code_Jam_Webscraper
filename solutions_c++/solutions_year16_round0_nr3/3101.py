#include<bits/stdc++.h>
#include<fstream>
typedef long long ll;

using namespace std;


int main(){
	ofstream archivo;
	archivo.open("codejamCsmall.out");
	int t;cin>>t;int n,m;cin>>n>>m;
	int cant=1;
	archivo<<"Case #1:"<<endl;
	archivo<<"1000000000000001 3 4 5 6 7 8 9 10 11"<<endl;
	for(int i=2;i<n;i+=2){
		for(int j=1;j<(n-i);j++){
			archivo<<"1";
			for(int k=1;k<(n-1);k++){
				if((k-j)<i && k>=j ) archivo<<"1";
				else archivo<<"0";
			}
			archivo<<"1 3 4 5 6 7 8 9 10 11"<<endl;
		}
	}
//	archivo<<"1100100000000001 3 4 5 6 7 8 9 10 11"<<endl;
	archivo.close();
}
