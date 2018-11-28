#include<iostream>
using namespace std;
int main()
{
    int Test_case;
    long long n;
    cin>>Test_case;
    int y,i,j,p;
    for(i=1; i<=Test_case; i++)
    {
        cin>>n;
        int c=10;
        if(!n) cout<<"Case #"<<i<<": INSOMNIA\n";
        else
        {
            int a[10]={0};
            for(j=1; ;j++)
            {
                y=n*j;
                p=y;
                while(p)
                {
                    if(a[p%10]==0)
                    {
                        a[p%10]=1;
                        c--;
                    }
                    p/=10;
                }
                if(!c) break;
            }
            cout<<"Case #"<<i<<": "<<y<<"\n";
        }
    }
    return 0;
}