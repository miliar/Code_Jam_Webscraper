///HH_ace
#include<bits/stdc++.h>
using namespace std;

typedef long long int lli;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef pair<long long int, long long int> PLL;
typedef vector<long long int> VL;

#define sdd(y) scanf("%lld", &y)
#define sd(x)  scanf("%d", &x)
#define F first
#define S second
#define pb push_back
#define MOD 1000000007

int a[500005];
int b[500005];

int main()
{
freopen("at.txt","r",stdin);
freopen("att.txt","w",stdout);
// ios_base::sync_with_stdio(false);

int t;
sd(t);
for(int ct=1;ct<=t;ct++){
        lli n;

        int arr[10];
        for(int i=0;i<10;i++)
            arr[i]=0;

        sdd(n);

        int i=0;
        if(!n)
        {
        cout<<"Case #"<<ct<<": INSOMNIA"<<endl;    continue;
        }

        lli tmp;
        for(i=1;;i++){

             tmp=n;
            int f=0;
               tmp=i*n;
              // cout<<tmp<<" ";
               while(tmp){
                ++arr[tmp%10];
                tmp=tmp/10;
               }
               for(int i=0;i<10;i++){

                if(!arr[i])
                {f=0 ; break;}
                else
                    f=1;
               }
               if(f)break;
          }

          cout<<"Case #"<<ct<<": "<<i*n<<endl;




}



return 0;
}
