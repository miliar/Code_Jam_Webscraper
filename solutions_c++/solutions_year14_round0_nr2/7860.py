#include<iostream>
#include<cstdio>
#include<iomanip>

using namespace std;

int main()
{
	freopen ("B-large.in","r",stdin);
    freopen ("B-large.out","w",stdout);
	
	int t,k;
	long double c,f,x,min,ca,xa,tm,i,w;
	
	cin>>t;
	
	for(k=1;k<=t;k++)
	{
		cin>>c>>f>>x;
		
		min=xa= x/2;
		ca=c/2;
		w=1;
		
		for(i=1;w && xa>(c/(2 + (i-1)*f));i++)
		{
			xa= x/(2 + i*f);
			//cout<<"xa:"<<xa<<" ca:"<<ca<<" min:"<<min<<endl;
			
			tm=ca+xa;
			
			if(min>tm)
			{
				min=tm;
			}
			else
			w=0;
			
			ca+= c/(2 + i*f);
			
		}
		
		cout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<min<<endl;
		//printf("Case #%d: %15.7f\n",k,min);
	}
	
	return 0;
}

