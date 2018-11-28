#include<bits/stdc++.h>
using namespace std;
int main()
{
	FILE *f=fopen("A-large.in","r");
	FILE *f1=fopen("op","w");
	int t,n;
	char s[1010];
	deque<char> v;
	fscanf(f,"%d",&t);
	for(int j=1;j<=t;j++)
	{
		fprintf(f1,"Case #%d: ",j);
		fscanf(f,"%s",s);
		n=strlen(s);
		for(int i=0;i<n;i++)
		{
			if(i==0)
			v.push_back(s[i]);
			else
			{
				if(s[i]>=v[0])
				v.push_front(s[i]);
				else
				{
					v.push_back(s[i]);
				}
			}
		}
		for(int i=0;i<v.size();i++)
		fprintf(f1,"%c",v[i]);
		fprintf(f1,"\n");
		v.clear();
	}
	return 0;
}
