#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <stdio.h>
#include <string.h>
using namespace std;
typedef long long ll;
int arr[10005]={0};
int main()
{
    freopen("mn.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    cin>>t;
    for(int q=1;q<=t;q++)
    {
        int n;
        cin>>n;
        char a[10000];
         scanf("%s",&a);
         int len=strlen(a);
        for(int i=0;i<len;i++)
        {

            arr[i]=a[i]-'0';
            //cout<<arr[i];
        }
        ll cnt=arr[0],sum=0;
        for(int i=1;i<n+1;i++)
        {
            //cout<<" cnt"<<cnt<<" sum "<<sum<<endl;
            if(cnt<i)
            {
                sum+=(i-cnt);
                cnt+=(i-cnt);
            }
            cnt+=arr[i];
        }
        cout<<"Case #"<<q<<": "<<sum<<endl;
    }
}
