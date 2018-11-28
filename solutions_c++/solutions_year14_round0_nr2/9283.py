#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int t,i;
	double c,f,x,l;
	double g,h,d,a;
	cin>>t;
	i=t;
	while(t--)
	{
		cin>>c>>f>>x;
		g=2;
		l=2+f;
		h=0;
		while(1)
		{
		 		 if((x/g)>((c/g)+(x/l)))
					{	h+=c/g;
						g=l;
						l+=f;
					}
					else
						break;
		}
		cout<<"Case #"<<(i-t)<<": ";
		cout<<std::fixed<<setprecision(7)<<(h+x/g)<<"\n";
		
	}
	return 0;
}
