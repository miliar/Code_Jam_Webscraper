#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;

int main()
{ 
	int t,a,n,ig,c;
	FILE*fin=fopen("input.txt","r");
	FILE*fout=fopen("output.txt","w");
	fscanf(fin,"%d",&t);
	for(int i=0;i<t;i++)
	{
		int r=0,d=0,ans;
	fscanf(fin,"%d%d",&a,&n);
	c=a;
	vector<int>m;
	for(int j=0;j<n;j++)
	{	fscanf(fin,"%d",&ig);
	m.push_back(ig);
	}
	sort(m.begin(),m.end());
	int v=a;
	bool f=1;

	for(int k=0;k<m.size();k++)
	{
	if(a>m[k])
	a+=m[k],v=a;
	else 
		{
		
 if(v+v-1>m[k])
 {
 d++;
 v+=(v-1);
 a=v;
 k--;
 }
 else r++;
	}
	}
	ans=r+d;
	int ans2=0;
	for(int k=0;k<m.size();k++)
	{if(c>m[k])
	c+=m[k];
	else {if(c==1){ans2=ans+1;break;}
	c+=c-1,ans2++,k--;
	if(ans2>ans)
		break;

	}
	}
		ans=min(ans,ans2);
	fprintf(fout,"Case #%d: %d\n",i+1,ans);
	
	}
	return 0;
}