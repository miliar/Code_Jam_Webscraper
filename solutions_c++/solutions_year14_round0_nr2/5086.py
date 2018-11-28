#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	int v=0;
	double c,f,k,f1=2.0;
	double ans=0.0;
	while(t--)
	{
		ans=0.0;
		f1=2.0;
		cin>>c;
		cin>>f;
		cin>>k;
		
		double a1=0,a2=0,atemp=0;
		a1 = c/f1;
		atemp = k/(f1+f);
		atemp +=a1;
		a2 = k/f1;
		while(atemp<a2)
		{
			ans+=a1;
			f1+=f;
			a1= c/f1;
				
			atemp = k/(f1+f);
			atemp += a1;
			a2= k/f1;
			
		}
		ans+= a2;
		cout<<"CASE #"<<(v+1)<<": ";
		cout<<fixed<<setprecision(7)<<ans<<endl;
		v++;
	}
	return 0;
}