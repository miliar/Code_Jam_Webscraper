#include<bits/stdc++.h>
using namespace std;
int p[105];
char inp[105][105];
inline int fun(char str[],int p)
{
	char temp = str[p];
	if(temp=='\0')
		return -1;
	while(str[p]==temp)
		p++;
	return p;
}
inline int solve(vector<int> v,int n)
{
	if(v.size()!=n)return -1;
	int i,sum=0,avg=0,res1=0,res2=0;
	for(i=0;i<v.size();i++)sum+=v[i];
	avg = sum/n;
	for(i=0;i<v.size();i++)
	{
		if(v[i]<=avg)res1+=(avg-v[i]);
		else res1-=(avg-v[i]);
		if(v[i]<=(avg+1))res2+=(avg+1-v[i]);
		else res2-=(avg+1-v[i]);
	}
	return min(res1,res2);
}
int main()
{
	int tt,t,n,i;
	scanf("%d",&t);
	for(tt=0;tt<t;tt++)
	{
		memset(p,0,sizeof(p));
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",inp[i]);
		int res = 0;
		vector<int> v;
		while(1)
		{
			int temp;	
			char ch = inp[0][p[0]];
			v.clear();
			for(i=0;i<n;i++)
			{
				temp = fun(inp[i],p[i]);
				if(temp!=-1 && inp[i][p[i]]==ch){ v.push_back(temp-p[i]);
				p[i] = temp;}
				else if(inp[i][p[i]]!=ch){res=-1;break;}
			}
			if(v.size()==0)break;
			temp = solve(v,n);
			if(res==-1||temp==-1){res=-1;break;}
			res+=temp;
			//cout<<p[0]<<" "<<p[1]<<endl;
		}
		if(res==-1)printf("Case #%d: Fegla Won\n",tt+1);
		else printf("Case #%d: %d\n",tt+1,res);
	}
	return 0;	
}
