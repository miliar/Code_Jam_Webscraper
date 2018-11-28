#pragma warning(disable:4786)
#include<fstream>
using namespace std;
#include<cstring>
#include<set>
FILE*fin=fopen("input.txt","r");
FILE*fout=fopen("output.txt","w");
int n,x,y,d[10][10]={{0},{0,-1,0},{0,0,1},{0,1,0},{0,0,-1}},a[110][110],out;
pair<int,int> p[110][110];
set<pair<int,int> > s;
pair<int,int> back(int r,int c)
{
	int i;
	if(p[r][c].first!=0)return p[r][c];
	p[r][c]=make_pair(-1,-1);
	for(i=1;;++i)
	{
		if(r+i*d[a[r][c]][1]<1||r+i*d[a[r][c]][1]>x||c+i*d[a[r][c]][2]<1||c+i*d[a[r][c]][2]>y)break;
		if(a[r+i*d[a[r][c]][1]][c+i*d[a[r][c]][2]])return p[r][c]=back(r+i*d[a[r][c]][1],c+i*d[a[r][c]][2]);
	}
	return p[r][c]=make_pair(r,c);
}
bool check(int r,int c)
{
	int i,j,t=a[r][c];
	pair<int,int> res;
	for(i=1;i<=4;++i)
	{
		if(i==t)continue;
		memset(p,0,sizeof(p));
		a[r][c]=i;
		if(back(r,c)!=make_pair(r,c))return true;
	}
	return false;
}
int main()
{
	int i,j,k;
	char ch;
	set<pair<int,int> >::iterator it;
	fscanf(fin,"%d",&n);
	for(i=1;i<=n;++i)
	{
		s.clear();
		memset(p,0,sizeof(p));
		fscanf(fin,"%d%d\n",&x,&y);
		for(j=1;j<=x;++j)
		{
			for(k=1;k<=y;++k)
			{
				fscanf(fin,"%c",&ch);
				switch(ch)
				{
				case '^':
					a[j][k]=1;
					break;
				case '>':
					a[j][k]=2;
					break;
				case 'v':
					a[j][k]=3;
					break;
				case '<':
					a[j][k]=4;
					break;
				default:
					a[j][k]=0;
					break;
				}
			}
			fscanf(fin,"\n");
		}
		for(j=1;j<=x;++j)for(k=1;k<=y;++k)if(a[j][k])s.insert(back(j,k));
		s.erase(make_pair(-1,-1));
		for(it=s.begin();it!=s.end();++it)if(!check(it->first,it->second))break;
		if(it!=s.end())fprintf(fout,"Case #%d: IMPOSSIBLE\n",i);
		else fprintf(fout,"Case #%d: %d\n",i,s.size());
	}
	return 0;
}