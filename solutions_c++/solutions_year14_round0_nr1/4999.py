#include<iostream>
#include<cstdio>
#include<cmath>
#include<sstream>
#include<ctime>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<map>
#include<set>
#define mp make_pair
#define pb push_back
#define max(a,b)a>b?a:b
#define min(a,b)a<b?a:b
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

int main ()
{
    //freopen("out.txt","w",stdout);
    //freopen("in.txt","r",stdin);
    int testCase,x,y,now,ans,got;
    cin>>testCase;
    bool cards[20];
    for(int qq=1;qq<=testCase;qq++)
    {
        cin>>x;
        memset(cards,false,sizeof cards);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            {
                got=0;
                cin>>now;
                if(i==x)
                    cards[now]=true;
            }
        cin>>y;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            {
                cin>>now;
                if(i==y && cards[now])
                {
                    ans=now;
                    got++;
                }
            }
        printf("Case #%d: ", qq);
        if(!got)
            cout<<"Volunteer cheated!\n";
        else if(got==1)
            cout<<ans<<endl;
        else
            cout<<"Bad magician!\n";
    }
    return 0;
}




