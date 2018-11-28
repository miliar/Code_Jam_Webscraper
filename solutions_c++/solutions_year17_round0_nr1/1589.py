#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A_large.txt","w",stdout);
	int a,b,c,T,num,K;
	char s[1010];
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin>>T;
	for(c=0;c<T;c++)
	{
		cin>>s>>K;
		num=0;
		for(a=0;s[a+K-1];a++)
		{
			if(s[a]=='-')
			{
				num++;
				for(b=0;b<K;b++)
				{
					if(s[a+b]=='-')s[a+b]='+';
					else s[a+b]='-';
				}
			}
		}
		for(a=0;s[a];a++)if(s[a]=='-')num=-1;
		if(num==-1)cout<<"Case #"<<c+1<<": IMPOSSIBLE\n";
		else cout<<"Case #"<<c+1<<": "<<num<<"\n";
	}
}
