#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input5.in","r",stdin);
    freopen("output5.txt","w",stdout);
    int a,b,c,d,e,f,g,h,i,j,k,l;
    cin>>a;
    for(d=1;d<=a;d++)
    {
        cin>>b;
        int arr[2501],brr[b];
        memset(arr,0,sizeof(arr));
        for(i=0;i<2*b-1;i++)
        {
            for(j=0;j<b;j++)
            {
                cin>>c;
                arr[c]++;
            }
        }
        e=0;
        for(i=0;i<2501;i++)
        {
            if(arr[i]%2!=0)
                brr[e++]=i;
        }
        sort(brr,brr+b);
        cout<<"Case #"<<d<<": ";
        for(i=0;i<b;i++)
            cout<<brr[i]<<" ";
        cout<<"\n";
    }
    return 0;
}
