#include <iostream>
#include <string.h>
#include <cstdio>
#include <stack>
#include <string>
using namespace std;
#define M 105
#define LL long long 
#define BB
int c,n,m;
string s,t;
int main()
{
#ifdef BB	
	freopen("E:\\11.in","r",stdin);
	freopen("E:\\11.out","w",stdout);
#endif
	int cc=1;
		cin>>n;
		while (n--)
		{	
			s.clear();
			t.clear();
			cin>>s;
			int l=s.length(),pos=0;
//			cout<<s<<endl;
			for (int i=0;i<l;i++)
			{
//				cout<<s[i]<<endl;
				if (pos==0||s[i]>=t[0])
				{
					t=s[i]+t;
				}
				else 
				{
					t+=s[i];
				}
				pos++;
			}
			cout<<"Case #"<<cc++<<": "<<t<<endl;	
		}
#ifdef BB
	fclose(stdin);
	fclose(stdout);
#endif
	return 0;
}
