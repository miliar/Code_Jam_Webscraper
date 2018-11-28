#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input4.in","r",stdin);
    freopen("output4.txt","w",stdout);
    int a,b,c,d,e,f,g,h,i,j,k,l;
    cin>>a;
    char str[100000],arr[100000];
    for(i=1;i<=a;i++)
    {
        cin>>str;
        j=k=1000;
        l=strlen(str);
        arr[j]=str[0];
        for(d=1;d<l;d++)
        {
            if(arr[j]<=str[d])
                arr[--j]=str[d];
            else
                arr[++k]=str[d];
        }
        cout<<"Case #"<<i<<": ";
        for(d=j;d<=k;d++)
            cout<<arr[d];
        cout<<"\n";
    }
    return 0;
}
