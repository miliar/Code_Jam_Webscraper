#include<iostream>
#include<cstdio>

using namespace std;



int main()
{
    freopen ("google1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int l,r,c=0,m=1;
    int a[5]={1,4,9,121,484};
    while(t--)
    {
        c=0;
        scanf("%d%d",&l,&r);
        for(int i=0;i<5;i++)
        {
            if(a[i]>=l && a[i]<=r)
            c++;
        }
    cout<<"Case #"<<m<<": "<<c<<endl;
    m++;
    }

}
