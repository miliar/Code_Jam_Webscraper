#include<iostream>
#include<cstdio>
using namespace std;
int n,a,b,out;
int main()
{
    ios_base::sync_with_stdio(0);
    cin>>n;
    for(int i=1;i<=n;i++)
    {
            cin>>a>>b;
            out=0;
            if(a<=1 && b>=1)
            out++;
            if(a<=4 && b>=4)
            out++;
            if(a<=9 && b>=9)
            out++;
            if(a<=121 && b>=121)
            out++;
            if(a<=484 && b>=484)
            out++;
            cout<<"Case #"<<i<<": "<<out<<endl;
    }
    return 0;
}
