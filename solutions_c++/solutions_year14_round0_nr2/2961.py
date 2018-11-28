

#include <iostream>
#include <cstdio>
using namespace std;

int main() {

//	freopen("B.in","r",stdin);
//	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);


	int t,tt;
	cin>>t;
	tt=t;
	while(t--)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double co=0.0,in=2.0,ret=0.0,fl=1.0;
		while(fl)
		{
			if(x/in<((c/in)+(x/(in+f))))
			{
				ret+=x/in;
				fl=0.0;
			}
			else
			{
				ret+=(c/in);
				in+=f;
			}
		}
		
		
		cout<<"Case #"<<tt-t<<": ";
		printf("%.7f",ret);
		cout<<endl;
	}
	return 0;
}