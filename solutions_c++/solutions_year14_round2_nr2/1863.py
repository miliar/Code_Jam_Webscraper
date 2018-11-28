#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;

ofstream myfile;

int main(){
	myfile.open ("out1.txt");
	int t,no=1;
	int ans=0;
	int a,b,k,i,j;
	cin>>t;
	while(t--){
		cin>>a>>b>>k;
		ans=0;
		for(i=0;i<a;i++){
			for(j=0;j<b;j++){
				if((i&j) <k){
					ans++;
				}
			}
		}
		myfile<<"Case #"<<no<<": "<<ans<<endl;
		no++;
	}
}
