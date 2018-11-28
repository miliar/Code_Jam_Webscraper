#include <iostream>
using namespace std;
int main(){
	
	int ntest;
	cin>>ntest;
	for(int k=0;k<ntest;k++){
  		double c,f,x,min;
		min=0;
  		cin>>c>>f>>x;
  		if(x<c){
			cout.precision(7);
cout.setf(ios::fixed,ios::floatfield);
			cout<<"Case #"<<k+1<<": "<<x/2<<endl;}
  	else{int n=(x*f/c-2)/f;
  	for(int i=0;i<n;i++)
  	{
 		min=min+(c/(2+(i*f)));
  	}
  	min=min+(x/(2+n*f));
cout.precision(7);
cout.setf(ios::fixed,ios::floatfield);
cout<<"Case #"<<k+1<<": "<<min<<endl;
}
		}
		}
	
		
