#include<bits/stdc++.h>
#define mp make_pair
#define PII pair<int,int>
#define fi first
#define se second
using namespace std;

const int NMAX=5005;

int t,n,R,P,S,nr[5],pw[15];
int sol[NMAX],a[NMAX],b[NMAX];
int op[]={3,1,2};

void Extend(int x)
{
    int i,len=pw[x],gud=pw[x+1];
    for (i=1;i<=len;i++)
    {
        b[2*(i-1)+1]=a[i];
        b[2*i]=op[a[i]-1];
    }
    len=gud;
    for (i=1;i<=len;i++) a[i]=b[i];
}

int Cmp()
{
    int i,len=pw[n];
    for (i=1;i<=len;i++)
    {
        if (sol[i]<a[i]) return -1;
        if (a[i]<sol[i]) return 1;
    }
    return 0;
}

int Cm(int x,int y)
{
    if (a[x]==a[y]) return 0;
    if (a[x]==3 && a[y]==1) return 1;
    if (a[x]==3 && a[y]==2) return 1;
    if (a[x]==1 && a[y]==2) return 1;
    return -1;
}

void Ver(int x,int y)
{
    int i,ok=0;
    for (i=x;i<y && !ok;i++)
        {
             if (a[i]==a[y+(i-x)]) ok=0;
             else
            if (a[i]==3 && a[y+(i-x)]==1) ok=1;
            else
            if (a[i]==3 && a[y+(i-x)]==2) ok=1;
            else
            if (a[i]==1 && a[y+(i-x)]==2) ok=1;
            else ok=-1;
        }
    if (ok==1)
        for (i=x;i<y;i++) swap(a[i],a[y+(i-x)]);
}

int main()
{
    int i,j,l,k,ok;
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    cin.sync_with_stdio(false);
    cin>>t;
    pw[0]=1;
    for (i=1;i<15;i++) pw[i]=pw[i-1]<<1;
    for (k=1;k<=t;k++)
    {
        cin>>n>>R>>P>>S;ok=0;
        for (i=1;i<=3;i++)//incerc cu i
        {
            a[1]=i;
            for (j=1;j<=n;j++)
                Extend(j-1);
            nr[1]=nr[2]=nr[3]=0;
            for (j=1;j<=pw[n];j++) nr[a[j]]++;
           /* for (j=1;j<=pw[n];j++)
                if (a[j]==1) cout<<"R";
                else if (a[j]==2) cout<<"P";
                else cout<<"S";
            cout<<"\n";*/
            for (j=1;j<=n;j++)//sortez grupuri
            {
                for (l=1;l<=pw[n];l+=1<<j)
                    Ver(l,l+(1<<(j-1)));
            }
            if (nr[1]==R && nr[2]==P && nr[3]==S)
            {
                if (ok==0)
                {
                    ok=1;
                    for (j=1;j<=pw[n];j++) sol[j]=a[j];
                }
                else if (Cmp()==1)
                {
                    for (j=1;j<=pw[n];j++) sol[j]=a[j];
                }
            }
        }
        cout<<"Case #"<<k<<": ";
        if (ok==0) cout<<"IMPOSSIBLE\n";
        else
        {
            for (i=1;i<=pw[n];i++)
                if (sol[i]==1) cout<<"R";
                else if (sol[i]==2) cout<<"P";
                else cout<<"S";
            cout<<"\n";
        }
    }
    return 0;
}

