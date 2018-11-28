#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.txt","w",stdout);
	int a,b,c,d,e,f,mn;
	char s1[10],s2[10],s3[10],s4[10];
	string ans1,ans2;
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin>>a;
	for(b=0;b<a;b++)
	{
		cin>>s1>>s2;
		mn=10000;
		if(strlen(s1)==1)c=10;
		else if(strlen(s1)==2)c=100;
		else c=1000;
		for(d=0;d<c;d++)
		{
			if(strlen(s1)==1)sprintf(s3,"%01d",d);
			else if(strlen(s1)==2)sprintf(s3,"%02d",d);
			else sprintf(s3,"%03d",d);
			for(e=0;s1[e]&&(s1[e]==s3[e]||s1[e]=='?');e++);
			if(!s1[e])
			{
				for(e=0;e<c;e++)
				{
					if(strlen(s2)==1)sprintf(s4,"%01d",e);
					else if(strlen(s2)==2)sprintf(s4,"%02d",e);
					else sprintf(s4,"%03d",e);
					for(f=0;s2[f]&&(s2[f]==s4[f]||s2[f]=='?');f++);
					if(!s2[f])
					{
						if(mn>abs(d-e))
						{
							mn=abs(d-e);
							ans1=s3;
							ans2=s4;
						}
					}
				}
			}
		}
		cout<<"Case #"<<b+1<<": "<<ans1<<" "<<ans2<<"\n";
	}
}
