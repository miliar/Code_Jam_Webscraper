#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int n,i,f1,f,k,t;
    cin>>t;
    int a[10];
    for(i=0;i<t;i++)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
            continue;
        }
        fill(a,a+10,0);
        f=1;
        for(f=1;;f++)
        {
            k=n*f;
            while(k)
            {
                a[k%10]++;
                k=k/10;
            }
            f1=1;
            for(int j=0;j<10;j++)
            {
                if(a[j]==0)
                {
                    f1=0;
                    break;
                }
            }
            if(f1)
            {
                cout<<"Case #"<<i+1<<": "<<f*n<<endl;
                break;
            }
        }
    }
    return 0;
}
