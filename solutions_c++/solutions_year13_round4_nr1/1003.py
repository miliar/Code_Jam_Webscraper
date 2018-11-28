#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
#define maxm 1001
struct Node
{
    int st,ed;
    int p;
    void input()
    {
	scanf("%d%d%d",&st,&ed,&p);
    }
    bool operator < (const Node &pe)const
    {
	if(st != pe.st)
	    return st < pe.st;
	else
	    return ed < pe.ed;
    }
}nd[maxm];
struct SS
{
    int flag;
    int p;
    int v;
    bool operator<(const SS &s)const
    {
	if(v == s.v)
	    return flag < s.flag;
	else 
	    return v < s.v;
    }
}ss[maxm*2];
int hp[maxm*2];
int cnt[1000];
bool cmp(const int &a,const int &b){
    return a < b;
}
int N,M;
long long int cal(int st,int ed)
{
    long long int cha = ed - st + 1;
    return (N + N - cha + 1) * cha / 2;
}
int main()
{
    int T;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    scanf("%d",&T);
    for(int csT = 1; csT <= T; csT++)
    {
	memset(cnt,0,sizeof(cnt));
	scanf("%d%d",&N,&M);
	int rear = 0;
	long long int precost = 0;
	for(int i = 0; i < M; i++){
	    nd[i].input();
	    precost += cal(nd[i].st,nd[i].ed)*nd[i].p;
	    ss[i*2].flag = 0;
	    ss[i*2].p = nd[i].p;
	    ss[i*2].v = nd[i].st;
	    ss[i*2 + 1].flag = 1;
	    ss[i*2 + 1].p = nd[i].p;
	    ss[i*2 + 1].v = nd[i].ed;
	}
	sort(ss,ss+M*2);
	long long int cost = 0;
	long long int left;
	for(int i = 0; i < M * 2; i++)
	{
	    if(ss[i].flag == 0)
	    {
		hp[rear++] = ss[i].v;
		cnt[ss[i].v] += ss[i].p;
		push_heap(hp,hp+rear,cmp);
	    }else
	    {
		left = ss[i].p;
		while(left != 0){
		    pop_heap(hp,hp+rear,cmp);
		    if(cnt[hp[rear-1]] >= left){
			cnt[hp[rear-1]] -= left;
			cost += left * cal(hp[rear-1],ss[i].v);
			left = 0;
			if(cnt[hp[rear-1]] == 0)
			    rear--;
			else
			    push_heap(hp,hp+rear,cmp);
			break;
		    }else
		    {
			cost += cnt[hp[rear-1]] * cal(hp[rear-1],ss[i].v);
			left -= cnt[hp[rear-1]];
			cnt[hp[rear-1]] = 0;
			rear--;
		    }
		}
	    }
	}
	printf("Case #%d: %lld\n",csT,precost - cost);
    }
    return 0;
}
