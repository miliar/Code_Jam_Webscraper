#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios::sync_with_stdio(false);
	int t=1,T;
	cin>>T;
	while(t<=T)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double timegone=0;
		double currate=2;
		while(1)
		{
			double nextfarm=c/currate;
			double nextwin=x/currate;
			if(nextfarm+(x/(currate+f))<nextwin)
			{
				currate+=f;
				timegone+=nextfarm;
			}
			else
			{
				timegone+=nextwin;
				break;
			}
		}
		cout<<"Case #"<<t<<": ";
		cout<<fixed<<setprecision(7)<<timegone<<endl;
		t++;
	}
	return 0;
}
