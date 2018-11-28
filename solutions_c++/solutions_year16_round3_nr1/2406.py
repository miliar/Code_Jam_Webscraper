#include<iostream>
#include<stdio.h>
#include<cstring>
#include<algorithm>
using namespace std;

struct arr{
int x;
char y;
};
bool compare(arr w,arr e)
{
    return w.x<e.x;
}
int cz(arr a[],int n)
{
    int ans=0;
    for(int i=0;i<n;i++)
    {if(a[i].x==0)
        ans++;
    }
    return ans;
}
int main()
{
    freopen("A-large (3).in","r",stdin);
    freopen("1c1large.txt","w",stdout);
    int t;
    cin>>t;
    for(int q=0;q<t;q++)
    {
        int n;
        cin>>n;
        arr a[n];
        for(int i=0;i<n;i++)
        {
            cin>>a[i].x;
            a[i].y=(char)(65+i);
        }
        cout<<"Case #"<<q+1<<": ";
        if(n==2)
        {
            while(a[0].x--)
            {cout<<"AB";
            if(a[0].x>0)
                cout<<" ";
            }
        }
        else
        {
            while(cz(a,n)<n-2)
            {
                sort(a,a+n,compare);
                if(a[n-1].x>=a[n-2].x)
                    {cout<<a[n-1].y<<" ";
                    a[n-1].x--;}
            }
            arr d[2];int r=0;
            for(int y=0;y<n;y++)
            {
                if(a[y].x!=0)
                {d[r].x=a[y].x;
                d[r].y=a[y].y;
                r++;}
            }
            while(d[0].x--)
            {
                cout<<d[0].y<<d[1].y;
                if(d[0].x>0)
                    cout<<" ";
            }
        }
        cout<<"\n";
    }

    return 0;
}
