#include<bits/stdc++.h>
using namespace std;

// #defines
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define sz(x) ((int)(x).size())
#define ms0(x) memset(x,0,sizeof(x))
#define ms1(x) memset(x,-1,sizeof(x))
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define f first
#define s second
#define mp make_pair
#define pb push_back
#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;
#define FILEIOS ;
#endif
#define inf 1001001001
typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;
const double eps = 1e-9;
const double pi = acos(-1.0);
const int maxn = (int)1e5 + 10;
const int mod = (int)1e9;
int fastMax(int x, int y) { return (((y-x)>>(32-1))&(x^y))^y; }
int fastMin(int x, int y) { return (((y-x)>>(32-1))&(x^y))^x; }

#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);

int main(){
    //FILEIO("B-small-practice");
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);

    long  ch,ck,p,t;
    long long i,k,j,m,n,l,x;
    int tab[200][200];
    tab[1][1]=1;tab[1]['i']='i';tab[1]['j']='j';tab[1]['k']='k';
    tab['i'][1]='i';tab['i']['i']=-1;tab['i']['j']='k';tab['i']['k']=-'j';
    tab['j'][1]='j';tab['j']['i']=-'k';tab['j']['j']=-1;tab['j']['k']='i';
    tab['k'][1]='k';tab['k']['i']='j';tab['k']['j']=-'i';tab['k']['k']=-1;
   int a[]={'i','j','k'};
    string s;
    cin>>t;

    for(i=1;i<=t;i++)
    {
        cin>>l>>x;
        cin>>s;
        n=l;
        m=n;
        j=1;
         k=0;ch=1;p=0;
           while(j<=x)
           {

               if(k==m)
               {
                 j++;
                 m=m+n;
                 continue;
               }
               if(ch<0)
               ch=(-1)*tab[ch*(-1)][s[k-(j-1)*n]];
               else
               ch=tab[ch][s[k-(j-1)*n]];
               if(ch==a[p])
               {
                   p++;
                   ch=1;
               }
               k++;
               if(p==3)
               {
                   for(;k<m;k++)
                   if(ch<0)
                    ch=(-1)*tab[ch*(-1)][s[k-(j-1)*n]];
                   else
                    ch=tab[ch][s[k-(j-1)*n]];
                    if(j==x)
                    {
                        if(ch==1)
                        break;
                        else
                        {
                            p=0;
                            break;
                        }
                    }
                    else
                    {
                        ck=1;
                        for(k=0;k<l;k++)
                        if(ck<0)
                         ck=(-1)*tab[ck*(-1)][s[k]];
                       else
                        ck=tab[ck][s[k]];
                        j=x-j;
                        j=j%4;
                        for(k=0;k<j;k++)
                        if(ch<0&&ck<0)
                        ch=tab[ch*(-1)][ck*(-1)];
                        else if(ch<0&&ck>0)
                        ch=(-1)*tab[ch*(-1)][ck];
                        else if(ch>0&&ck<0)
                        ch=(-1)*tab[ch][ck*(-1)];
                        else
                        ch=tab[ch][ck];

                        if(ch==1)
                        break;
                        else
                        {
                            p=0;
                            break;
                        }
                    }
               }

           }
           if(p<3)
           cout<<"Case #"<<i<<": NO"<<endl;
           else
           cout<<"Case #"<<i<<": YES"<<endl;
    }

    return 0;
}


