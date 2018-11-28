//
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MOD 1000000007
#define INF 2147483647
#define PI 3.1415926535897932384626433832795
#define all(cont) cont.begin(),cont.end()
#define init(a,val) memset(a,val,sizeof(a))
#define F first
#define S second
#define mp make_pair
//GLOBAL

int main()
{
    freopen("1.in","r",stdin);//freopen("1.out","w",stdout);
    int test_cases,Testno;

    int n,ext,cou,i;
    string s;

    cin>>test_cases;
    for(Testno=1;Testno<=test_cases;Testno++)
    {
        printf("Case #%d: ",Testno);
//___________________________________________
        cin>>n>>s;
        ext=0;cou=0;
        for(i=0;i<=n;i++){
            if(i>cou){
                ext+=i-cou;
                cou=i;
                //cout<<cou<<' ';
            }
            cou+=s[i]-'0';
        }
        cout<<ext;

//___________________________________________
        Done: printf("\n");
    }

return 0;
}
