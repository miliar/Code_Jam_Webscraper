#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
vector<string>ve[300];
map<string,int>mm;
int vt,n,k,s,t,flow,head[300000],nowhead[300000],cnt[300000],sta[300000],path[300000],dis[300000],next[1000010],u[1000010],v[1000010],w[1000010];
void sap(){
	flow=0;
	memset(cnt,0,sizeof(cnt));
	memset(sta,0,sizeof(sta));
	memset(dis,0,sizeof(dis));
	memcpy(nowhead,head,sizeof(head));
	int p=s,f=10000000,flag;
	cnt[0]=t;
	while(dis[s]<t){
		sta[p]=f;flag=0;
		for(int i=nowhead[p];i;i=next[i])
			if(w[i]&&dis[p]==dis[v[i]]+1){
				path[v[i]]=i;flag=1;
				if(w[i]<f)f=w[i];
				nowhead[p]=i;p=v[i];
				if(p==t){
					flow+=f;
					for(;p!=s;p=u[path[p]]){
						w[path[p]]-=f;
						w[path[p]^1]+=f;
					}
					f=1000000000;
				}
				break;
			}
		if(flag)continue;
		int minx=t+1,tmp=0;
		for(int i=head[p];i;i=next[i])
			if(w[i]&&dis[v[i]]<minx){
				minx=dis[v[i]];
				tmp=i;
			}
		nowhead[p]=tmp;
		--cnt[dis[p]];
		if(cnt[dis[p]]==0)break;
		dis[p]=minx+1;
		++cnt[dis[p]];
		if(p!=s){
			p=u[path[p]];
			f=sta[p];
		}
	}
}
void add(int u1,int v1,int w1){
	u[++vt]=u1;v[vt]=v1;w[vt]=w1;next[vt]=head[u1];head[u1]=vt;
	u[++vt]=v1;v[vt]=u1;w[vt]=0;next[vt]=head[v1];head[v1]=vt;
}
void calc(){
	memset(head,0,sizeof(head));
	vt=1;mm.clear();
	int to=1;
	scanf("%d",&n);getchar();
	for(int i=1;i<=n;++i){
		char ch=getchar();
		string tt="";ve[i].clear();
		while(1){
			if(ch==' '||ch=='\n'){
				ve[i].push_back(tt);
				if(!mm.count(tt)){
					mm[tt]=to;
					to+=2;
				}
				tt="";
			}else tt+=ch;
			if(ch=='\n')break;
			ch=getchar();
		}
	}
	for(int i=1;i<to;i+=2)add(i,i+1,1);
	s=to;t=s+1;
	for(int i=0;i<ve[1].size();++i)
		add(s,mm[ve[1][i]],100000000);
	for(int i=0;i<ve[2].size();++i)
		add(mm[ve[2][i]]+1,t,100000000);
	for(int i=3;i<=n;++i)
		for(int j=0;j<ve[i].size();++j)
			for(int k=0;k<ve[i].size();++k)
				add(mm[ve[i][j]]+1,mm[ve[i][k]],100000000);
	sap();
	printf("%d\n",flow);
}
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;++test){
		printf("Case #%d: ",test);
		calc();
	} 
	return 0;		
}
