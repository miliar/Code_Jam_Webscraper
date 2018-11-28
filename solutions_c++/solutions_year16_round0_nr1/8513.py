#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("codejam1.out", "w", stdout);
    int testcases,y;
    cin>>testcases;
    for(y=1;y<=testcases;y++)
    {
        int n,i=1,j,k,x;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<y<<": INSOMNIA"<<endl;
        }
        else
        {
        int flag=0;
        int hashi[10];
        memset(hashi,0,sizeof(hashi));
        while(flag==0)
        {
            k=i*n;
            while(k>0)
            {
                x=k%10;
                if(hashi[x]==0)
                    hashi[x]++;
                k=k/10;
            }
            for(j=0;j<10;j++)
            {
                if(hashi[j]==0)
                    break;
            }
            if(j==10)
            {
                flag=1;
                cout<<"Case #"<<y<<": "<<i*n<<endl;
            }
            i++;
        }
        }
    }
}
