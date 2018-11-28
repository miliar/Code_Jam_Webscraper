/*"The Woods are lovely dark and deep,
But i have promises to keep,
Miles to go before i sleep and Miles to go before i Sleep"
*/
#include<bits/stdc++.h>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<string.h>
#define pb(n) push_back(n)
unsigned long long mod=1000000007;
using namespace std;
#define GI ({long int t;scanf("%ld",&t);t;})
#define all(x) x.begin(),x.end() //sort(all(x))
#define sz(h1) h1.size()
int main()
{
int T,cards[4][4],check[20],num,test,ans,row,i,j;
T=GI;
test=T;
       while(T--)
        {
                memset(check,0,sizeof(check));
                ans=0;
                row=GI;
                for(i=0;i<4;i++)
                        for(j=0;j<4;j++)
                                scanf("%d",&cards[i][j]);
                for(i=0;i<4;i++)
                        check[cards[row-1][i]]=1; row=GI;
                for(i=0;i<4;i++)
                        for(j=0;j<4;j++)
                                scanf("%d",&cards[i][j]);
                for(i=0;i<4;i++)
                        if(check[cards[row-1][i]])
                        {
                                ans++;
                                num=cards[row-1][i];
                        }
                 if(ans==0)
                         cout<<"Case #"<<test-T<<": Volunteer cheated!"<<endl;
                else if(ans==1)
                        cout<<"Case #"<<test-T<<": "<<num<<endl;
                else 
                        cout<<"Case #"<<test-T<<": Bad magician!"<<endl;
}
return 0;
}
 
