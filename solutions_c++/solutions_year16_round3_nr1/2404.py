#include<bits/stdc++.h>
using namespace std;
int f1max(int a[],int s)
{
    int n=a[0],l=0,i;
    for(i=1;i<s;i++)
    {
        if(a[i]>=n&&a[i]!=0)
        {
            n=a[i];
            l=i;
        }
    }
    return l;
}
int f2max(int a[],int s)
{
    int n=a[0],l=0,pre=0,i;
    for(i=1;i<s;i++)
    {
        if(a[i]>=n&&a[i]!=0)
        {
            pre=l;
            n=a[i];
            l=i;
        }
    }
    return pre;
}
int main()
{
    int t,i,si,s,a[100],n,v,b;
    fstream fp;
    fp.open("A.in",ios::in);
    ofstream fo;
    fo.open("out.txt",ios::out);

    fp>>t;

    for(int q=0;q<t;q++)
    {
        s=0;
        fp>>n;
        for(i=0;i<n;i++)
        {
            fp>>a[i];
            s+=a[i];
        }
        //cout<<s;
        fo<<"Case #"<<q+1<<": ";
        while(s!=0)
        {
            v=f1max(a,n);
            b=f2max(a,n);
            //cout<<v<<" "<<b<<endl;
            if(s==3)
            {
                fo<<char(v+65)<<' ';
                s--;
                a[v]--;
            }
            else if(a[v]>a[b]+1)
            {
                fo<<char(v+65)<<char(v+65)<<' ';
                s-=2;
                a[v]-=2;
            }
            else
            {
                fo<<char(v+65)<<char(b+65)<<' ';
                s-=2;
                a[v]--;
                a[b]--;
            }


        }
        //cout<<endl;
        fo<<endl;
    }
}
