#include<bits/stdc++.h>
using namespace std;

bool isSleeping(int a[])
{
    bool flag = true;
    for(int i=0; i<10; i++)
    {
        if(a[i]<1)
            flag = false;
    }
    return flag;
}
main()
{
    freopen( "A-large.in", "r", stdin );
	freopen( "output.out", "w", stdout );

    int t,n,t0;
    cin>>t;
    t0=t;
    while(t--)
    {
        int a[10]= {0};
        int tempNum,temp=0,i=1,k;
        cin>>n;
        k=n;
        if(n==0)
            cout<<"Case #"<<t0-t<<": INSOMNIA"<<endl;
        else
        {
            while(!isSleeping(a))
            {
                tempNum=n;
                //cout<<n<<endl;
                while(tempNum>0)
                {
                    temp=tempNum%10;
                    tempNum=tempNum/10;
                    a[temp]++;
                    //cout<<"a["<<temp<<"] = "<<a[temp]<<"\t";
                }
                //cout<<endl;
                i++;
                n=k*i;
            }
            cout<<"Case #"<<t0-t<<": "<<k*(i-1)<<endl;
        }

    }
}
