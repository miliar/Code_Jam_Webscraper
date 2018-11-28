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
    int t,i,cs=0,ans;
    string s;
    int ara[101];
    scanf("%d",&t);
    while (t--)
    {
        cin>>s;
        ans = 0;
        for (i=0;i<s.size();i++)
        {
            if (s[i] == '-') ara[i] = 0;
            else ara[i] = 1;
        }
        int flag = 0;
        for (i=s.size() - 1;i>=0;i--)
        {
            if (ara[i] == flag)
            {
                ans++;
                flag = !flag;
            }
        }
        cout<<"Case #"<<++cs<<": "<<ans<<endl;
    }
    return 0;
}
