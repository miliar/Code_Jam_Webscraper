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

bool huiwen(int s)
{
	int a[10],ind(0);
	int tt=s;
	while(s)
	{
		a[++ind]=s%10;
		s/=10;
	}
	for(int i=1,j=ind;i<j;i++,j--)
		if(a[i]!=a[j])return false;
	return true;
}

int T;
int A,B;
int ans(0);

int main()
{
//	freopen("C.in","r",stdin);
//	freopen("C.out","w",stdout);
	
	T=nextInt();
	for(int ttt=1;ttt<=T;ttt++)
	{
		ans=0;
		A=nextInt();
		B=nextInt();
		int l,r;
		if(A==((int)sqrt(A))*((int)sqrt(A)))l=(int)sqrt(A);else l=(int)sqrt(A)+1;
		r=(int)sqrt(B);
		for(int i=l;i<=r;i++)
			if(huiwen(i))
				if(huiwen(i*i))ans++;
		cout<<"Case #"<<ttt<<": "<<ans<<endl;
	}
	
	return 0;
}
