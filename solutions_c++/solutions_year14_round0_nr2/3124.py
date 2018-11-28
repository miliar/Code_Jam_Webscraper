#include<iostream>
#include<conio.h>
#include<cstdio>
#include<algorithm>
#include<iomanip>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	//freopen("Inp1.txt","r",stdin);
	freopen("Out.out","w",stdout);
	static long T, p;
	long double tmp1, tmp2, tmp3, X, R, C, ANS, F;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		R=2.0000000;
		cin>>C>>F>>X;
    	ANS=0.0000000000;
    	p=0;
    	while(p==0)
    	{
			tmp1=X/R; tmp3=C/R; tmp2 = tmp3 + (X/(R+F));
        	if (tmp2<tmp1)
            {
				ANS = ANS+tmp3; R=R+F;
            }
        	else
            {
				ANS = ANS+tmp1;
				cout<<"Case #"<<i<<": "<<setprecision(12)<<ANS<<endl;
				p=1;
			}
		}
	}
	return 0;
}
