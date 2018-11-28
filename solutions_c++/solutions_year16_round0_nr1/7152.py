/**


  ######                                                                     ######   #     #  #######
  #     #    ##    #####   #    #  #    #  #    #  #   ####   #    #  #####  #     #  #     #       #
  #     #   #  #   #    #  #   #   #   #   ##   #  #  #    #  #    #    #    #     #  #     #      #
  #     #  #    #  #    #  ####    ####    # #  #  #  #       ######    #    ######   #######     #
  #     #  ######  #####   #  #    #  #    #  # #  #  #  ###  #    #    #    #   #    #     #    #
  #     #  #    #  #   #   #   #   #   #   #   ##  #  #    #  #    #    #    #    #   #     #   #
  ######   #    #  #    #  #    #  #    #  #    #  #   ####   #    #    #    #     #  #     #  #######



**/
/*

    BismiLLAHIR RAHMANIR RAHIM
    It's not how you look or who you are underneath, it's what you do that defines you

                                ------********-------

    Status : ;
    TC: xxx/xxx;
    DOS: ;
    OJ: ;

*/

#include <bits/stdc++.h>

using namespace std;

#define PB          push_back
#define PF          push_front
#define  V          vector
#define PII         pair <int,int>

typedef long long int           LL;

const double EPS = 1e-9;
const double PI = acos(-1.0);

int GCD (int x, int y){if (x%y==0) return y; else return (GCD(y,x%y));}

int main()
{
    #ifdef O_Amay_Valo_Basheni
        freopen("get.txt","r",stdin);
        freopen("got.txt","w",stdout);
    #endif // O_Amay_Valo_Basheni
    int t,cs=0,cnt;
    bool ara[10];
    LL x,y,a,b,j;
    int i;
    scanf("%d",&t);
    while (t--)
    {
        cin>>x;
        memset(ara,0,sizeof ara);
        cnt=0;
        if (x == 0) printf("Case #%d: INSOMNIA\n",++cs);
        else
        {
            y = 1;
            for (a = 1;cnt<10;a++)
            {
              y = x*a;
              j = y;
              while (y>0 && cnt<10)
              {
                  b = y%10;
                  y/=10;
                  if (!ara[b])
                  {
                      ara[b] = 1;
                      cnt++;
                  }
              }
            }
            cout<<"Case #"<<(++cs)<<": "<<j<<endl;
        }
    }
    return 0;
}
