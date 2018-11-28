#include <iostream>
#include <string.h>
#include <cstdio>
#include <stack>
using namespace std;
#define M 105
#define LL long long 
#define BB
int c,n,m,t;
int s[15];
int main()
{
#ifdef BB	
	freopen("E:\\A-small-attempt0.in","r",stdin);
	freopen("E:\\A-small-attempt0.out","w",stdout);
#endif
	int cc=1;
	cin>>t;
	while (t--)
	{
		memset(s,0,sizeof(s));
		cin>>n;
		if (n==0)
			cout<<"Case #"<<cc++<<": INSOMNIA"<<endl;
		else
		{
			int sum=0,f=0;
			LL temp=n;
			while (f==0)
			{
				LL tt=temp;
				while (tt>0)
				{
					s[tt%10]=1;
					tt/=10;
				}
				f=1;
				for (int i=0;i<10;i++)
				{
					if (s[i]==0)
						f=0;
				}
				temp+=n;
			}
			cout<<"Case #"<<cc++<<": "<<temp-n<<endl;
		}
	}
#ifdef BB
	fclose(stdin);
	fclose(stdout);
#endif
	return 0;
}
