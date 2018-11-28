#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
typedef pair<long long,long long> pll;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define ll long long
int GCD(int a, int b)
{
    return b? GCD(b,a%b) : a;
}
long long prim(long long n)
{
    long long num,i;
    num=n;
    for(i=2; i*i<=n; i++)
    {
        if(num%i==0)
        {
            while(num%i==0)
            {
                num/=i;
            }
        }
    }
    if(num==n)
        return 1;
    else
        return 0;
}
long long chhotu(long long n)
{
    long long num,i;
    num=n;
    for(i=2; i*i<=n; i++)
    {
        if(num%i==0)
        {
            break;
        }
    }
    return i;
}
long long POW(long long Base, long long Exp)
{
    long long y,ret=1;
    y=Base;
    while(Exp)
    {
        if(Exp&1)
            ret=(ret*y);
        y = (y*y);
        Exp/=2;
    }
    return ret;
}
string str;
vi Aajao[70007];
vi Huzoor[1007];
vector < vi > Po;
int main()
{
    int t,tc;
    cin>>t;
    for(tc=1; tc<=t; tc++)
    {
        long long i,j,n,tmp,k,Hukum;
        cin>>n>>Hukum;

        long long Max = POW(2,n);
        long long Min = POW(2,n-1);

        for(i=0; i<Max; i++)
        {
            for(j=0, tmp=1; j<n; j++ )
            {
                if(tmp&i && i>0)
                {
                    Aajao[i].pb(1);
                }
                else
                {
                    Aajao[i].pb(0);
                }
                tmp = tmp<<1;
            }
        }
        /*for(i=0; i<Max; i++)
        {
        	for(j=0; j<Aajao[i].size(); j++)
        	{
        		cout<<Aajao[i][j];
        	}
        	cout<<endl;
        }	*/
        int siz=0,bkc=0;
        for(i=0; i<Max; i++)
        {
            int ctr=0;
            bkc = Aajao[i].size();

            if(Aajao[i][0]!=1 || Aajao[i][bkc-1]!=1)
            										continue;
            for(j=2; j<11; j++)
            {
                ll temp=0;
                for(k=0; k<Aajao[i].size(); k++)
                {
                    if(Aajao[i][k])
                    {
                        temp+= POW(j,k);
                    }
                }
                if(!prim(temp))
                    ctr++;
            }
            if(ctr==9)
            {
                Po.pb(Aajao[i]);
                siz++;
            }
            if(siz==57)
                break;
        }
        /*cout<<"Yahan toh pahuche!"<<siz<<endl;
        for(i=0; i<siz; i++)
        {
        	int lim=Po[i].size();
        	for(j=lim-1; j>=0; j--)
        	{
        		cout<<Po[i][j];
        	}
        	cout<<endl;
        }*/
        for(i=0; i<Hukum; i++)
        {
            for(j=2; j<11; j++)
            {
                ll temp=0;
                for(k=0; k<Po[i].size(); k++)
                {
                    if(Po[i][k])
                    {
                        temp+= POW(j,k);
                    }
                    //printf("temp: %lld\n",temp);
                }
                cout<<"div: "<<j<<" temp: "<<temp<<endl;
                Huzoor[i].pb(chhotu(temp));
            }
        }
        printf("Case #%d:\n",tc);
        for(i=0; i<Hukum; i++)
        {
            for(j=Po[i].size()-1; j>=0; j--)
            {
                cout<<Po[i][j];
            }
            cout<<" ";
            for(j=0; j<Huzoor[i].size(); j++)
            {
                cout<<Huzoor[i][j]<<" ";
            }
            cout<<endl;
        }
    }
    return 0;
}
