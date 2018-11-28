#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>

using namespace std;

int main()
{
    FILE *fin = freopen("A-small-attempt0.in.txt", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-small.out.txt", "w", stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long int n,ans;
        cin>>n;
        if(n==0)
        {
            cout << "Case #" << i << ": "<<"INSOMNIA"<< endl;
            continue;
        }
        if(n==1)
        {
            cout<<"Case #"<<i<<":"<<" "<<10<<endl;
            continue;
        }
        if(n==2)
        {
            cout<<"Case #"<<i<<": "<<90<<endl;
            continue;
        }
        bool h[10];
        memset(h,0,sizeof(h));
        int c=0,j=1,d;
        long int num;
        do
        {
           num=n*j;
           ans=num;
           while(num>0)
           {
               d=num%10;
               if(h[d]==0)
               {
                   h[d]=1;
                   c++;
               }
               num=num/10;
           }
           if(c==10)
            break;
            //cout<<i<<" "<<j<<" "<<d<<" "<<c<<endl;
           j++;
        }while(1);

        cout<<"Case #"<<i<<": "<<ans<<endl;


    }
    exit(0);
}
