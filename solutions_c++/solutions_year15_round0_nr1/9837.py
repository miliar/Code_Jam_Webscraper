///HH_ace
#include<bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

typedef pair<int, int> pii;
typedef vector<int> vi;

typedef pair<long long int, long long int> PLL;
typedef vector<long long int> VL;


#define sd(x) scanf("%d", &x)
#define sdd(y) scanf("%lld", &y)

#define F first
#define S second
#define mp make_pair
#define pb push_back
#define MOD 1000000007

#define N 1123
#define M 52

int X[8]={0,-1,0,1,-1,-1,1,1};

int Y[8]={-1,0,1,0,-1,1,-1,1};

int n,m;
struct node
{
    int a;
    int b;
};

bool v_p(int a,int b)
{
    return ((a<n && a>=0) && ((b<m && b>=0)))?true:false ;
}



int main()
{
freopen("at.in","r",stdin);
freopen("atul.out","w",stdout);

int t;
sd(t);
for(int m=1;m<=t;m++)
{
    int n;
    sd(n);
    n++;
    int a[n];

    string s;
    cin>>s;
    for(int i=0;i<n;i++)
    {
        a[i]=s[i]-'0';
        //cout<<a[i]<<" ";
    }



    int c=0,ans=0;


    for(int i=0;i<n;i++)
    {
      if(c>=i)
            c+=a[i];
      else
      {
          ans+=abs(c-i);
          c+=a[i]+abs(c-i);
      }

        //cout<<" ans is"<<ans<<" c is"<<c<<endl;

    }

    cout<<"Case #"<<m<<": "<<ans<<endl;
}

 return 0;
}

