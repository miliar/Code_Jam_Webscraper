#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
double c,f,x;
double deal(double n)
{
	if(n==0)
		return x/2;
	else
	{
		double ans=x/(2+f*n);
		for(double i=0;i<n;i++)
			ans+=c/(2+f*i);
		return ans;
	}
}
int jude()
{
	return  (f*x-f*c-2*c)/(f*c);
}
int main()
{
	int T;
	fstream in("B-large.in");
	fstream out("ans.out");
	in>>T;
	for(int kcase=1;kcase<=T;kcase++)
	{
		in>>c>>f>>x;
		double ans=deal(0);
		double tmp=jude();
		if(tmp>=0)
		{
			ans=min(ans,deal(tmp));
			ans=min(ans,deal(tmp+1));
		}
		if(tmp>=1)
			ans=min(ans,deal(tmp-1));
		//cout<<ans<<endl;
		out<<"Case #"<<kcase<<": "<<fixed<<setprecision(7)<<ans<<endl;
		cout<<"Case #"<<kcase<<": "<<fixed<<setprecision(7)<<ans<<endl;
	}
}

			