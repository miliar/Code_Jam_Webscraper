#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;

int N,R,P,S;
int q[1200000],p[1200000],ans;
int r[1200000];

void dfs(int st,int ed){
	int mid=(st+ed)/2;
	if(ed-st<2) return;
	dfs(st,mid);
	dfs(mid,ed);
	for (int i = 0; i < (ed-st)/2; ++i)
	{
		if (r[st+i]!=r[i+mid])
		{
			if(r[st+i]>r[i+mid]){
				for(int j=0;j<(ed-st)/2;j++){
					int tp = r[j+st];
					r[j+st]=r[j+mid];
					r[j+mid]=tp;
				}
			}
			break;
		}
	}
}

int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
    	scanf("%d%d%d%d",&N,&R,&P,&S);
    	ans = 0;

    	int m;
    	for (int i = 0; i < 3; ++i)
    	{
    		q[0]=(i==0?'R':i==1?'P':'S');
    		m=1;
    		for (int j = 0; j < N; ++j)
    		{
    			for(int k=0;k<m;k++){
    				if (q[k]=='R')
    				{
    					p[k*2]='R';
    					p[k*2+1]='S';
    				}
    				else if (q[k]=='S')
    				{
    					p[k*2]='P';
    					p[k*2+1]='S';
    				}
    				else if (q[k]=='P')
    				{
    					p[k*2]='P';
    					p[k*2+1]='R';
    				}
    			}
    			m *= 2;
    			for(int k=0;k<m;k++) q[k]=p[k];
    		}
    		int a=0,b=0,c=0;
    		for(int k=0;k<m;k++){
    				if (q[k]=='R')
    				{
    					a++;
    				}
    				else if (q[k]=='P')
    				{
    					b++;
    				}
    				else if (q[k]=='S')
					{
						c++;
					}    			
    		}
    		if(a==R&&b==P&&c==S){
    			if(ans == 1){
	    			int a1,a2;
	    			a1=0,a2=0;
			        for (int i = 0; i < m; i+=2){
			        	if(r[i+1]=='R') a1++;
			        	if(q[i+1]=='R') a2++;
			        }
			        if(a1>a2) continue;
			        if (a1==a2)
			        {
				        for (int i = 0; i < m; i+=2){
				        	if(r[i]=='P'&&r[i+1]=='S') a1++;
				        	if(q[i]=='P'&&q[i+1]=='S') a2++;
				        }
				        if(a1>=a2) continue;
			        }
    			}
    			ans = 1;
    			for(int k=0;k<m;k++) r[k]=q[k];
    		}
    	}

    	dfs(0,m);

        printf("Case #%d: ", tt);
        if (ans==0)
        {
        	printf("IMPOSSIBLE");
        }else {
	        for (int i = 0; i < m; i++)
	        	printf("%c",r[i]);
        }
        puts("");
    }
    return 0;
}

