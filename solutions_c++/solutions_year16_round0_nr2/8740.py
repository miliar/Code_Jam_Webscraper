#include<bits/stdc++.h>
#define N 1000000007
#define maxs 300005
#define mins 1005
#define pf printf
#define sc scanf
#define ll long long
#define pb push_back
using namespace std;

int main()
{
	int t;
	sc("%d",&t);
	for(int l1=1;l1<=t;l1++)
	{
		string s;
		cin>>s;
		int n=s.length();
		cout<<"Case #"<<l1<<": ";
	//	cout<<n<<endl;
		int k=n-1;
		int i;
		for(i=n-1;i>=0;i--)
		{
			if(s[i]=='-')
			{
				k=i;
				break;
			}
		}
		int l,j;
		int fl,fl1;
		int c=0;
		for(i=0;i<n;i++)
		{
			fl=0;
			fl1=0;
			for(j=0;j<=k;j++)
			{
				if(s[j]=='-')
				{
					fl1=1;
					break;
				}
				else
				{
					s[j]='-';
					fl=1;
				}
			}
			if(fl1==0)
			break;
			if(fl==1)
			c++;
			string str="",s1="",str1="";
			for(j=0;j<=k;j++)
			{
				if(s[j]=='+')
				{
					l=j;
					break;
				}
				else
				str+="+";
			}
			for(j=k;j>=l;j--)
			{
				if(s[j]=='+')
				s1+="-";
				else
				s1+="+";
			}
			s=s1+str;
			k=s.length()-l-1;
			c++;
		//	cout<<s<<" "<<k<<" "<<c<<endl;
		}
		printf("%d\n",c);
	}
	return 0;
}
