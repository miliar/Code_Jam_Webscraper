# include<bits/stdc++.h>
#define gc getchar_unlocked

using namespace std;

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

int main()
{
    int t,d[1002],p,n,j,i,max,lk,k;
    scanint(t);
    for(k=1;k<=t;k++)
    {
        scanint(n);
        for(i=0;i<n;i++)
           scanint(d[i]);
        sort(d,d+n);
        max=d[n-1];
        lk=max; 
        for(i=1;i<=max;i++)
        {
            p=i;
            for(j=0;j<n;j++)
            {
                if( d[j]>i && d[j]%i==0)
                   p=p+d[j]/i-1;
                else if(d[j]>i)
                   p=p+d[j]/i;         
            }
            if( lk>p)
              lk=p;   
        }
        cout<<"Case #"<<k<<": "<<lk<<endl;;
    }                                 
    return 0;
}
