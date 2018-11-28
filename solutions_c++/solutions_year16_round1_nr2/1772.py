#include <bits/stdc++.h>
using namespace std;

int main() {
freopen("B-large (1).in","r",stdin);
freopen("output3.out","w",stdout);
    int t,ti,i,n;
    char str[1000];
    cin>>t;
    for(ti=1;ti<=t;ti++)
    {
        int count[2501]={0},i,j;
        cout<<"Case #"<<ti<<": ";
        cin>>n;
        int a;
        for(i=0;i<2*n-1;i++)
        {
            for(j=0;j<n;j++)
            {
                cin>>a;
                count[a]++;
            }
        }
        int arr[n];
        int p=0;
        
            for(j=0;j<2501;j++)
            {
                if(count[j]%2)
                {
                    arr[p++]=j;
                }
            }
        
        sort(arr,arr+n);
        for(i=0;i<n;i++)
        {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }
    
	return 0;
}

