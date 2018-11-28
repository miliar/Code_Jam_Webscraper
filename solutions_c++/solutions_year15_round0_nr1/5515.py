#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int n,t,k;
    freopen("/Users/saravanakumars/program0.txt","r",stdin);
    freopen("/Users/saravanakumars/program0.ans","w",stdout);
    int requiredFriendsCount = 0,currentCount = 0;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n;
       /* if(n==0)
        {
            cout<<"Case #"<<i+1<<": "<<0<<endl;
            continue;
        }*/
        vector<int> s(n+1);
        requiredFriendsCount = 0,currentCount = 0;
        string temp;
        cin>>temp;
        for(int j=0;j<=n;j++)
        {
            s[j] = temp[j] - '0';
            if(currentCount < j && s[j] > 0)
            {
                int diff = (j-currentCount);
                currentCount = j;
                requiredFriendsCount += diff;
            }
            currentCount += s[j];
        }
        cout<<"Case #"<<i+1<<": "<<requiredFriendsCount<<endl;
    }
}
