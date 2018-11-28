#include <iostream>
#include <cstdio>

using namespace std;
int t;
int n;
double a[1001];
double b[1001];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for(int q=1;q<=t;q++)
    {
        cin >> n;
        for(int i=0;i<n;i++)
            cin >>a[i];
        for(int i=0;i<n;i++)
            cin >>b[i];
        for(int i=0;i<n;i++)
        for(int j=i+1;j<n;j++)
            if(a[i]>a[j]) {double t=a[i]; a[i]=a[j];a[j]=t;}
        for(int i=0;i<n;i++)
        for(int j=i+1;j<n;j++)
            if(b[i]>b[j]) {double t=b[i]; b[i]=b[j];b[j]=t;}
        int res1=0;
        int k=0;
        for(int i=0;i<n;i++)
        {
            while(k<n && b[k]<a[i]) k++;
            if(k==n){res1=n-i;}
            k++;
        }
        int i=0;
        int j=0;
        int res2=0;
        while(1)
        {
            while(i<n && a[i]<b[j]) i++;
            if(i==n) break;
            i++;j++;res2++;
        }
        printf("Case #%d: %d %d\n",q,res2,res1);
    }
    return 0;
}
