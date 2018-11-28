#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;

ofstream myfile;

int main(){
	myfile.open ("out.txt");
	int t;
	int no=1;
	double c,f,x,r,ans=0,d,d1,s;
	cin>>t;
	while(t--){
		cin>>c>>f>>x;
		r=0;
		d=2.0;
		d1=d;
		ans=0;
		/*
		if(x<=f){
			ans=ans+x/d;
		}
		*/
		//else{
			d=d+f;
			s=x-c;
			while(r!=1){
				if((x/d)<(s/d1)){
					ans=ans+c/d1;
				}
				else{
					ans=ans+x/d1;
					r=1;
				}
				d=d+f;
				d1=d-f;
			}
		//}
		myfile<<"Case #"<<no<<": "<<setprecision(7)<< fixed <<ans<<endl;
		no++;
	}
}
