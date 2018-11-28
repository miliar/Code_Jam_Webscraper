#include<bits/stdc++.h>

using namespace std;

#define sd(x) scanf("%d",&x);
#define slld(x) scanf("%lld",&x);
#define LL long long
#define LD long double
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define Fill(a, b) memset(a, b, sizeof(a))
#define INF 2000000009

typedef pair<int,int> PII;
typedef vector<int> VI;

#define N 300010

map<char,int> mp;

string sr[8] = {"1","-1","i","-i","j","-j","k","-k"};

int a[8][8] =  {{0,1,2,3,4,5,6,7},{1,0,3,2,5,4,7,6},{2,3,1,0,6,7,5,4},{3,2,0,1,7,6,4,5},{4,5,7,6,1,0,2,3},{5,4,6,7,0,1,3,2},{6,7,4,5,3,2,1,0},{7,6,5,4,2,3,0,1}};

int ar[N];

void print()
{
    for(int i=0;i<8;i++)
    {
        for(int j=0;j<8;j++)
        {
            cout<<sr[a[i][j]]<<" ";
        }
        cout<<endl;
    }
}

void solve()
{
    int l;
    LL x;
    sd(l);
    slld(x);
    string s,str="";
    cin>>s;
    if(x>12)
    {
        x = 12 + (x%12);
    }
    //cout<<x<<endl;
    while(x>0)
    {
        x--;
        str += s;
    }
    //cout<<str<<endl;
    int n=str.length(),pre=0,suf=0,i=0,mid=0;
    for(i=0;i<n;i++)
    {
        ar[i] = mp[str[i]];
    }
    for(i=0;i<n;i++)
    {
        if(pre==2)break;
        pre = a[pre][ar[i]];
    }
    if(i==n)
    {
        printf("NO\n");
        return ;
    }
    for(i;i<n;i++)
    {
        if(mid==4)break;
        mid = a[mid][ar[i]];
    }
    if(i==n)
    {
        printf("NO\n");
        return ;
    }
    for(i;i<n;i++)
    {
        suf = a[suf][ar[i]];
    }
    if(suf==6)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
}

int main()
{
    //freopen("in5.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    mp['1']=0;
    mp['i']=2;
    mp['j']=4;
    mp['k']=6;
    //print();
	int t=1;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
        printf("Case #%d: ",i);
		solve();
	}
}

