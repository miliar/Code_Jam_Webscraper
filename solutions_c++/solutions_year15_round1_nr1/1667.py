#include<iostream>
#include<vector>
using namespace std;
int main()
{
    freopen("/Users/saravanakumars/program0.txt","r",stdin);
    freopen("/Users/saravanakumars/program0.out","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin>>n;
        vector<long long> c(n);
        long long maxDiff = 0;
        long long randomEating = 0;
        long long constantEating = 0;
        for(int j=0;j<n;j++)
        {
            cin>>c[j];
            if(j>0 && c[j-1] > c[j])
            {
                randomEating += (c[j-1] - c[j]);
                maxDiff = max(maxDiff, c[j-1] - c[j]);
            }
        }
        for(int j=0;j<n-1;j++)
        {
            constantEating += min(maxDiff,c[j]);
        }
        cout<<"Case #"<<(i+1)<<": "<<randomEating<<" "<<constantEating<<endl;
    }
}
