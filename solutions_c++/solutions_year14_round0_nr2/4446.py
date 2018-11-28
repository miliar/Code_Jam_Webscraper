#include <iostream>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		double C, F, X;
		cin>>C>>F>>X;
		int nFnum=0;
		double primarytime=X/2;
		nFnum=1;
		double newtimefront=C/2;
		double newtime=newtimefront+X/(nFnum*F+2);
		while(primarytime>newtime)
		{
			primarytime=newtime;
			newtimefront+=C/(nFnum*F+2);
			nFnum++;
			newtime=newtimefront+X/(nFnum*F+2);
		}
		cout<<"Case #"<<t<<": ";
		printf("%.7f\n",primarytime);
	}
	return 0;
}