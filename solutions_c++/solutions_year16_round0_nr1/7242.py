/****************************************************************
*    sonu kumar
*    MNNIT allahabad
*    computer science and engineering
****************************************************************/
#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define pb(i) push_back(i)
#define mp(i,j) make_pair(i,j)
#define line printf("\n")
#define space printf(" ")
#define sci(i) scanf("%d",&i)
#define scl(i) scanf("%lld",&i)
#define chk(a) cerr << endl << #a << " : " << a << endl
#define chk2(a,b) cerr << endl << #a << " : " << a << "\t" << #b << " : " << b << endl
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int sonu=1;sonu<=t;sonu++)
    {
        ll n;
        scanf("%lld",&n);
        printf("Case #%d: ",sonu);
        if(n==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        map<ll,ll>ind;
        set<ll>make;
        int x=1;
        ll temp=n;
        bool flag=0;
        while(!ind.count(temp))
        {
             //cout<<"taking digits of temp= "<<temp<<endl;
             while(temp)
                make.insert(temp%10),temp/=10;
            if(make.size()==10)
            {
            //chk(x*n);
                flag=1;
                break;
            }
            x++;
            temp=x*n;
        }
        if(flag)
            printf("%lld\n",x*n);
        else
            printf("INSOMNIA\n");
    }
    return 0;
}
