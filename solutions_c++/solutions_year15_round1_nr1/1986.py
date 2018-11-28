#include<iostream>
#include<cstdio>

using namespace std;

int a[1001],n;
int method1()
{
    int i,sum=0;
    for(i=1;i<n;i++)
        if(a[i]<a[i-1])
            sum+=a[i-1]-a[i];
    return sum;
}
int method2()
{
    int i,diff=0,sum=0;
    for(i=1;i<n;i++)
        if(a[i-1]-a[i]>diff)
            diff=a[i-1]-a[i];
    for(i=0;i<n-1;i++)
        sum+=min(diff,a[i]);
    return sum;
}
int main()
{
    freopen("C:\\Users\\Saurabh Prakash\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\Saurabh Prakash\\Desktop\\out.txt","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--)
    {
        int i;
        cin>>n;
        for(i=0;i<n;i++)
            cin>>a[i];
        int ans1=method1();
        int ans2=method2();
        cout<<"Case #"<<cas++<<": "<<ans1<<" "<<ans2<<endl;
    }

    return 0;
}
