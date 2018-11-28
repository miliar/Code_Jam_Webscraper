#include<bits/stdc++.h>
using namespace std;
int mark[29];
vector<pair<int,int> > arr;
int main()
{
    
    //  freopen("A-large.in","r",stdin);
    // freopen("CJ2AL.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        int n;
        cin>>n;
        arr.clear();
        arr.resize(n);
        int sum=0;
        for(int j=0;j<n;j++)
        {
            cin>>arr[j].first;
            arr[j].second=j;
            sum+=arr[j].first;
        }
        while(1)
        {
            if(sum==0)
                break;
            sort(arr.rbegin(),arr.rend());
            int c=arr[0].first;
            int sump=arr[1].first*2;
            int sub=sum-sump;
            if(sub==0)
            {
                
                char ch1=arr[0].second+'A';
                char ch2=arr[1].second+'A';
                while(c--)
                {
                    cout<<ch1<<ch2<<" ";
                }
                sum=0;
                arr[0].first=0;
                arr[1].first=0;
                continue;
            }
            sub=min(c,sub);
            arr[0].first-=sub;
            int q=sub/2;
            int r=sub%2;
            char ch=arr[0].second+'A';
            while(q--)
            {
                
                cout<<ch<<ch<<" ";
            }
            while(r--)
            {
                cout<<ch<<" ";
            }
            sum-=sub;
        }
        
        
        cout<<endl;
        
    }
    return 0;
}
