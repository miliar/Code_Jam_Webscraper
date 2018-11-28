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
    freopen("1.in","r",stdin);freopen("1.out","w",stdout);
    int test_cases,Testno;
    int m[7]={-1,0,0,1,2,2,2},x,r,c;

    cin>>test_cases;
    for(Testno=1;Testno<=test_cases;Testno++)
    {
        printf("Case #%d: ",Testno);
//___________________________________________
        cin>>x>>r>>c;
        if(r>c)swap(r,c);
        if((r*c)%x!=0 || x>6){
            cout<<"RICHARD";goto Done;
        }
        if(r<=m[x]){
                cout<<"RICHARD";
        }
        else cout<<"GABRIEL";

//___________________________________________
        Done: printf("\n");
    }

return 0;
}
