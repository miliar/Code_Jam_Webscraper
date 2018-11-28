#include<bits/stdc++.h>

using namespace std;

int main()
{
        
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
        int t;
        int test;
        cin>>test;
        for(int t=0;t<test;t++)
        {
                cout<<"Case #"<<t+1<<": ";
                int n,size;
                cin>>n>>size;
                int arr[10000];
                for(int i=0;i<n;i++)
                {       
                        cin>>arr[i];
                }
                sort(arr,arr+n);
                int beg=0,end=n-1;
                int ans=0;
                while(beg<=end)
                {
                        if(beg==end)
                        {ans++;
                        break;}
                        if(arr[beg]+arr[end]<=size)
                                {
                                        beg++;
                                        end--;
                                        ans++;
                                }
                        else
                        {
                                ans++;
                                end--;
                        }
                }
                cout<<ans<<"\n";
        }
        
}
