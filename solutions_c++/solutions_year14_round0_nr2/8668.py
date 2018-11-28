#include<iostream>
#include<fstream>
#include <iomanip>

using namespace std;

int main(){
	freopen("output.txt","w",stdout);
	freopen("input.txt","r",stdin);
	int t;
	cin>>t;
	double c,f,x,T,r;
	for (int k = 1; k <=t; k++)
	{
		T=0;
		r=2;
		cin>>c>>f>>x;
		while(true){
			if(x/r<=(c/r+x/(r+f))){
				T+=x/r;
				break;
			}
			T+=c/r;
			r+=f;
		}
		cout<<"Case #"<<k<<": ";
		cout.precision(7);
		cout<<fixed<<T<<endl;
	}
	
}