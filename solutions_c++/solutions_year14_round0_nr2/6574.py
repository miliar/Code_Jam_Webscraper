#include<iostream>
#include <iomanip>
#include<fstream>
using namespace std;
int main(){
	ifstream cin("b.in");
	ofstream cout("b.txt");
	int t,u;
	double c,f,x,i=0,r=0;
	double a,b,sec;
	cin>>t;
	u=t;
	while(t--){r=2;; sec=0;
		cin>>c>>f>>x;
		do{
			
		
		sec+=(c*1.0/r);
	a=(x-c)*1.0/r;
	b=x*1.0/(r+f);
	//cout<<a<<b;
	if(a>=b)
	{
		r=r+f;
	}
	if(b>a){
	sec+=((x-c)*1.0/r);
	break;
	}
	}while(1);
	 cout<<"Case #"<<u-t<<": ";
    cout<<setprecision(7)<<fixed;
    cout<<sec<<endl;
}return 0;
}
