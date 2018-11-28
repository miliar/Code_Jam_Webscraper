#include<stdio.h>
#include<string.h>
#include<queue>
#include<set>
#include<string>
using namespace std;
struct st
{
	char s[105];
	int t;
}fr,tp;
set<string>se;
queue<st>Q;
int len;
bool chk(st x)
{
	int i;
	for(i=0;i<len;i++)
	if(x.s[i]=='-')return false;
	return true;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int t,cas,i,j;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%s",fr.s);
		len=strlen(fr.s);
		fr.t=0;
		while(!Q.empty())Q.pop();
		se.clear();
		Q.push(fr);
		string ts(fr.s);
		se.insert(ts);
		while(!Q.empty())
		{
			fr=Q.front();
			Q.pop();
			if(chk(fr))
			{
				printf("Case #%d: %d\n",cas,fr.t);
				break;
			}
			for(i=1;i<=len;i++)
			{
				tp=fr;
				for(j=0;j<i;j++)
				{
					tp.s[j]='+'+'-'-tp.s[j];
				}
				int p=0,q=i-1;
				while(p<q)
				{
					char tmp=tp.s[p];
					tp.s[p]=tp.s[q];
					tp.s[q]=tmp;
					p++;
					q--;
				}
				string ts(tp.s);
				if(se.find(ts)==se.end())
				{
					se.insert(ts);
					tp.t++;
					Q.push(tp);
				}
			}
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
