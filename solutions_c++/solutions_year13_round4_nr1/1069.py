#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>

#define Debug

using namespace std;

const int MOD = 1000002013;
const int MAX = 1001;

typedef long long LL;

int N,M;
int res;
struct In
{
    int oi,ei,pi;
}s[MAX];

int len;
struct E
{
    int v;
    LL num;
    int left;
}t[MAX*2];

bool cmp(In a,In b)
{
    if(a.oi!=b.oi) return a.oi<b.oi;
    else return a.ei<b.ei;
}

bool cmpt(E a,E b)
{
    if(a.v!=b.v) return a.v<b.v;
    else return a.left<b.left;
}

void doit()
{
    int i,j,k;
    for(i=j=1;i<len;i++)
    {
        if(t[i].v == t[i-1].v && t[i].left == t[i-1].left)
        {
            t[j-1].num += t[i].num;
        }
        else
        {
            t[j] = t[i];
            j++;
        }
    }
    len=j;
    /*
    for(i=0;i<len;i++)
    cout<<t[i].v<<' '<<t[i].left<<' '<<t[i].num<<endl;
    */
    res=0;
    LL w;
    for(i=0;i<len;i++)
    if(t[i].left==1)
    {
    	for(j=i-1;j>=0;j--)
    	if(t[j].left==0 && t[j].num)
    	{
    		if(t[i].num<=t[j].num)
    		{
    			w=(N+N-t[i].v+t[j].v+1)%MOD;
    			w=(w*(t[i].v-t[j].v)/2)%MOD;
    			w=(w*(t[i].num%MOD))%MOD;
    			res=(res+w)%MOD;
    			t[j].num-=t[i].num;
    			t[i].num=0;
    			break;
    		}
    		else
    		{
    			w=(N+N-t[i].v+t[j].v+1)%MOD;
    			w=(w*(t[i].v-t[j].v)/2)%MOD;
    			w=(w*(t[j].num%MOD))%MOD;
    			res=(res+w)%MOD;
    			t[i].num-=t[j].num;
    			t[j].num=0;
    		}
    	}
    }
    
    
    for(i=0;i<M;i++)
    {
    	w=(N+N-s[i].ei+s[i].oi+1)%MOD;
		w=(w*(s[i].ei-s[i].oi)/2)%MOD;
		w=(w*s[i].pi)%MOD;
		res=(res-w)%MOD;
		if(res<0) res+=MOD;
    }
    res = (MOD - res)%MOD;
}

int main()
{
    #ifdef Debug
        freopen("A-small-attempt0.in","r",stdin);
        freopen("A-small-attempt0.out","w",stdout);
    #endif

    int T,cas;
    scanf("%d",&T);
    for(cas=1;cas<=T;cas++)
    {
        scanf("%d%d",&N,&M);
        len=0;
        for(int i=0;i<M;i++)
        {
            scanf("%d%d%d",&s[i].oi,&s[i].ei,&s[i].pi);
            t[len].v = s[i].oi;
            t[len].left = 0;
            t[len].num = s[i].pi;
            len++;

            t[len].v = s[i].ei;
            t[len].left = 1;
            t[len].num = s[i].pi;
            len++;
        }
        sort(s,s+M,cmp);
        sort(t,t+len,cmpt);
        doit();
        printf("Case #%d: %d\n",cas,res);
    }
    return 0;
}
