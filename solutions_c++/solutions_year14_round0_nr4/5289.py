#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstring>
using namespace std;
int war(int a[],int b[],int n)
{
    sort(b,b+n,greater<int>());
    int point=0,begin=0,end=n-1;
    int i=0;
    while(begin<=end)
    {
        if(a[i]>b[begin])
        {
            point++;
            end--;
        }
        else
        {
            begin++;
        }

        i++;
    }

return point;


}


int dwar(int a[],int b[],int n)
{
    sort(b,b+n);
    sort(a,a+n);
    int point=0,begin=0,end=n-1,i=0;

bool used[20];
memset(used,0,sizeof(used));

    for(i=0;i<n;i++)
    {
        while(begin<=end && b[i]>a[begin])
        {
            begin++;
        }
        if(begin>end)
        {
            break;
        }
        else
        {
            //cout<<b[i]<<" "<<a[begin]<<endl;
            point++;
            begin++;
        }
    }



    return point;

}
int main()
{
    freopen("in3.txt","r",stdin);
    //freopen("out3.txt","w",stdout);
    int a[20],b[20],n,t,i,test;
    float a1[20],b1[20];
    cin>>t;
    for(test=1;test<=t;test++)
    {
    cin>>n;
    for(i=0;i<n;i++)
    {
    cin>>a1[i];
    a[i]=a1[i]*1000000;
    }

    for(i=0;i<n;i++)
    {
    cin>>b1[i];
    b[i]=b1[i]*1000000;
    }
    sort(a,a+n,greater<int>());
    cout<<"Case #"<<test<<": "<<dwar(a,b,n)<<" "<<war(a,b,n)<<endl;
    }
return 0;
}
