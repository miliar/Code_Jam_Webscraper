#include<iostream>
#include<fstream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

template <typename T>
inline void upd_min(T& dest, const T& src){if(src<dest)dest=src;}
template <typename T>
inline void upd_max(T& dest, const T& src){if(dest<src)dest=src;}

template <typename T, int n>
struct Queue
{
    T q[n];
    int qf, qr;
    Queue():qf(0), qr(0){}
    inline void clear(){qf=qr=0;}
    inline bool empty(){return qf==qr;}
    inline void push(const T& data){q[qr]=data;if(++qr==n)qr=0;}
    inline void pop(){if(++qf==n)qf=0;}
    inline T& front(){return q[qf];}
};

template <int maxN>
struct Disjoint
{
    int N;
    int p[maxN];
    inline void init(int n) { N=n; for(int i=0;i<N;++i) p[i]=i; }
    inline int root(int i){for(;i!=p[i];i=p[i]) p[i]=p[p[i]]; return i;}
    inline void unite(int a, int b){p[root(b)]=root(a);}
    inline bool query(int a, int b){return root(a)==root(b);}
};

template <typename T,int N>
struct Stack
{
    T s[N];
    int index;
    Stack():index(0){}
    inline void clear(){index=0;}
    inline T& top(){return s[index];}
    inline void pop(){--index;}
    inline bool empty(){return index==0;}
    inline void push(T data){s[++index] = data;}
};

int nextInt()
{
    int ret;char c;
    while(c=getchar(),c<'0'||c>'9');
    ret=c-'0';
    while(c=getchar(),c>='0'&&c<='9')ret=ret*10+c-'0';
    return ret;
}

const int inf=0x7f7f7f7f;

int T;

char map[5][5];
int a[5][5];
bool unc(0);

int xixi()//1==O 2==T 0==D
{
	for(int i=1;i<=4;i++)
	{
		for(int j=1;j<=4;j++)		
		{
			if(map[i][j]-'.'==0)
			{
				unc=1;
				a[i][j]=-1;	
			}
			else
			a[i][j]=map[i][j]-'A'+1;
		}
	}
	int tt=0;
	for(int i=1;i<=4;i++)
		tt+=a[i][i];
	if(tt==65||tt==60)return 1;
	if(tt==96||tt==92)return 2;
	tt=0;
	for(int i=1;i<=4;i++)
		tt+=a[i][5-i];
	if(tt==65||tt==60)return 1;
	if(tt==96||tt==92)return 2;
	
	for(int i=1;i<=4;i++)
	{
		tt=0;
		for(int j=1;j<=4;j++)
			tt+=a[i][j];
		if(tt==65||tt==60)return 1;
		if(tt==96||tt==92)return 2;
		tt=0;
		for(int j=1;j<=4;j++)
			tt+=a[j][i];
		if(tt==65||tt==60)return 1;
		if(tt==96||tt==92)return 2;
	}
	return 0;
}

int main()
{
//	freopen("A.in","r",stdin);
//	freopen("A.out","w",stdout);
	
	cin>>T;
	for(int ttt=1;ttt<=T;ttt++)
	{
		memset(a,0,sizeof(a));
		unc=0;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				cin>>map[i][j];
		int ans=xixi();
		if(ans==1)
			cout<<"Case #"<<ttt<<": O won"<<endl;
		if(ans==2)
			cout<<"Case #"<<ttt<<": X won"<<endl;
		if(ans==0&&unc)
			cout<<"Case #"<<ttt<<": Game has not completed"<<endl;
		if(ans==0&&(!unc))
			cout<<"Case #"<<ttt<<": Draw"<<endl;
	}
	return 0;
}
