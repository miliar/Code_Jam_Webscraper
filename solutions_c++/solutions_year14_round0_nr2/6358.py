#include<iostream>
#include<fstream>
#include<vector>
#include<iomanip>
using namespace std;

int main(){
	ifstream cin("B-large.in");
	ofstream cout("bbb.txt");
	int T,cases=1;
	cin>>T;
	while(T--){
		double C,F,X;
		double v=2;
		cin>>C>>F>>X;
		double t=0;
		while(1){
			t+=C/v;
			X-=C;
			if((X+C)/(v+F)>=X/v){
				break;
			}else{
				X+=C;
				v+=F;
			}
		}
		t+=X/v;
		cout<<"Case #"<<cases++<<": "<<fixed<<setprecision(7)<<t<<endl;

	}
	
}