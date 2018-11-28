#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin>>n;
        double a[n],b[n];
        for(int j=0;j<n;j++)
            cin>>a[j];
        for(int j=0;j<n;j++)
            cin>>b[j];
        sort(a,a+n);
        sort(b,b+n);
        int ts=0,p1=n-1,p2=n-1,k=0,x=0;
        while(p1>=0&&p2>=k)
        {
            if(a[p1]>b[p2])
            {
                ts++;
                p1--;
                k++;
            }
            else
                {
                    p2--;
                    p1--;
                }
        }
        p1=n-1;
        p2=n-1;
        k=0;
        while(p1>=k&&p2>=0)
        {
            if(a[p1]<b[p2])
            {
                p2--;
                k++;
            }
            else
                {
                    x++;
                    p2--;
                    p1--;
                }
        }
        printf("Case #%d: %d %d\n",(i+1),x,ts);
    }
}