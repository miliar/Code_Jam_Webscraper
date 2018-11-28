#include<bits/stdc++.h>
#define ll long long
#define FOR(i,n) for(i=0;i<n;i++)
#define FORS(i,a,b) for(i=a;i<b;i++)
#define FORR(i,a,b) for(i=a;i>=b;i--)
#define REP(i,n) for(int i=0;i<n;i++)
#define REPS(i,a,b) for(int i=a;i<b;i++)
#define REPR(i,a,b) for(int i=a;i>=b;i--)
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii>
#define TRvii(v,it) for(vii::iterator it=v.begin();it!=v.end();++it)
#define TRvi(v,it) for(vi::iterator it=v.begin();it!=v.end();++it)
#define gc getchar_unlocked
#define pc putchar_unlocked
//#define cin fin
#define cout fout
#define INF 999999999
#define MAX 100010
using namespace std;
ifstream fin("t2.in");
ofstream fout("out.txt");


bool iscomplete(bool a[10])
{
	REP(i,10)if(a[i]==0)return 0;
	return 1;
}

ll f(int n)
{
	bool L[10]={0,0,0,0,0,0,0,0,0,0};
	ll c=0;
	ll k=0;
	while(!iscomplete(L))
	{
		c++;k+=n;
		int temp=k;
		while(temp!=0)
		{
			L[temp%10]=1;
			temp/=10;
		}
	}
	return c;
}

ll ans[1000010];

int main()
{
	REPS(i,1,1000001)
	{
		ans[i]=f(i);
	}
	int start;
	REP(i,1)
	{
		cin>>start;
		int tc;int n;
		fin>>tc;
		REP(t,tc)
		{
			fin>>n;
			if(n==0)fout<<"Case #"<<t+1<<": INSOMNIA"<<endl;
			else fout<<"Case #"<<t+1<<": "<<n*f(n)<<endl;
		}
	}
}


