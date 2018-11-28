#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include<vector>
#include<fstream>

int main() {
    using namespace std;
    freopen("/Users/prakul/Dropbox/codes/codeJam/A-small-attempt1.in","rt",stdin);
    freopen("/Users/prakul/Dropbox/codes/codeJam/mgk.out","wt",stdout);

    int n,m;
    string w;
    cin>>n;
    m=n;
    while(n--)
    {
        int a,b,x,cnt=0,cnt_x,mp[17]={0};
        cin>>a;

        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            scanf("%d",&x);
            if((i+1)==a)
            {
                mp[x]++;
               // cout<<"L "<<x<<endl;
            }

        }
        cin>>b;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            scanf("%d",&x);
            if((i+1)==b && mp[x]>0){
                cnt++;
                cnt_x=x;
                }

        }

    cout<<"Case #"<<m-n<<": ";
    if(cnt==0)
    printf("%s\n","Volunteer cheated!");
    else if(cnt==1)
    printf("%d\n",cnt_x);
    else
    printf("%s\n","Bad magician!");

    }
}
