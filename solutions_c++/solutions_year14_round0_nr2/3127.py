#include<cstdio>
#include<iomanip>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
//		freopen("a.in","r",stdin);
//		freopen("aa.out","w",stdout);
		int t;
		cin >> t;
		for(int i=1;i<=t;i++)
		{
			printf("Case #%d: ",i);
		    double c,f,x;
		    cin >> c >> f >> x;
		    double d=c-x;
		    double ans=x/2;
		    double j=2;
		    while(1)
			{
				double e=x/(j+f)+d/j;
				if(e<0)
				{
						ans+=e;
						j+=f;
				}
				else break;
			}
			cout <<fixed << setprecision(7) << ans << endl;
		}
//		fclose(stdin);
//		fclose(stdout);
		return 0;
}
