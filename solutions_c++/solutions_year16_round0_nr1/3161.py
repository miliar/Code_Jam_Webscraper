#include <iostream>
#include <stdio.h>
#include <bits/stdc++.h>
#define pf printf
#define sf scanf
using namespace std;
int a[10];
int fin(int a1)
{
    int t2=a1;int rem;
    while(t2!=0)
    {
        rem=t2%10;
        a[rem]=1;
        t2=t2/10;
    }
    for(int i=0;i<10;i++)
    {
        if(a[i]!=1)
            return 0;
    }
    return 1;
}

int main()
{
    //cout << "Hello world!" << endl;
    freopen("A-small-attempt2.in","rt",stdin);
	freopen("a2.out","wt",stdout);
    int t;long long int n;
    cin>>t;

    for(int i=1;i<=t;i++)
    {
        cin>>n;

        pf("Case #%d: ",i);
        if(n==0)
        {
            pf("INSOMNIA\n");
        }
        else
        {
             memset(a,0,sizeof(a));
            int mul=2;long long int mt=n;int f=1;
            while(f==1)
            {
                int h=fin(mt);
                if(h==1)
                {

                    f=0;
                }
                else{
                mt=n*mul;//cout<<mt<<" ";
                mul++;
                }
            }
           cout<<mt<<"\n";
        }
        //lk:printf("t %d\n",t);

    }
    return 0;
}
