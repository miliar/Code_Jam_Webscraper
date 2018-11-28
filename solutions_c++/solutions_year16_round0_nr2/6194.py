#include<bits/stdc++.h>

using namespace std;

string S;
int a[12],cnt;
int main(void)
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		cout<<"Case #"<<tt<<": ";
		
		cin>>S;
		int l=S.length();

		for(int i=l-1;i>=0;i--)
		{
			
			if(S[i]=='-')
			{
				cnt++;
				for(int k=0;k<=i;k++)
				{
					if(S[k]=='+')
					{
						S[k]='-';
					}
					else
					{
						S[k]='+';
					}
				}
			}
			
		}
		
		cout<<cnt;
		cout<<endl;
		cnt=0;
	}

	return 0;
}
