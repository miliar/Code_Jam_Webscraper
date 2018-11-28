#include<bits/stdc++.h>
using namespace std;
char arr[200];
void flip(int n)
{
    for(int i=0;i<=n;i++)
    {
        if(arr[i]=='-')
            arr[i]='+';
        else
        arr[i]='-';
    }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("pancakessmall123456789.out","w",stdout);
    int t,siz;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>arr;
        int j;
        for(j=0;j<200;j++)
        {
            if(arr[j]=='\0')
                break;
        }
        siz=j;
        int ans=0;
        for(int k=siz-1;k>=0;k--)
        {
            if(arr[k]=='-')
            {
                flip(k);
                ans++;
            }
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
}
