#pragma warning(disable:4786)
#include<fstream>
using namespace std;
#include<map>
#include<string>
#include<vector>
FILE*fin=fopen("input.txt","r");
FILE*fout=fopen("output.txt","w");
int n,x,b[210]={0,1,2},cnt,chk1[1510],chk2[1510],out;
vector<int> a[210];
map<string,int> m;
void back(int p)
{
	int i,j,t=0;
	if(p>x)
	{
		memset(chk1,0,sizeof(chk1));
		memset(chk2,0,sizeof(chk2));
		for(i=1;i<=x;++i)if(b[i]==1)for(j=0;j<a[i].size();++j)chk1[a[i][j]]=1;
		for(i=1;i<=x;++i)if(b[i]==2)for(j=0;j<a[i].size();++j)chk2[a[i][j]]=1;
		for(i=1;i<=1500;++i)if(chk1[i]&&chk2[i])t++;
		if(t<out)out=t;
		return;
	}
	b[p]=1;
	back(p+1);
	b[p]=2;
	back(p+1);
}
int main()
{
	int i,j,k,l;
	char str[15010],word[20];
	string words;
	fscanf(fin,"%d\n",&n);
	for(i=1;i<=n;++i)
	{
		m.clear();
		out=999999999;
		cnt=0;
		fscanf(fin,"%d\n",&x);
		for(j=1;j<=x;++j)
		{
			fgets(str,15000,fin);
			l=strlen(str);
			a[j].clear();
			for(k=0;k<l;++k)
			{
				sscanf(str+k,"%s",word);
				words=(string)word;
				if(m.find(words)==m.end())m[words]=++cnt;
				a[j].push_back(m[words]);
				k=k+strlen(word);
			}
		}
		back(3);
		fprintf(fout,"Case #%d: %d\n",i,out);
	}
	return 0;
}