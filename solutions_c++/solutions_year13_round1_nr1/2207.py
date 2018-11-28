#include<cstdio>
#include<iostream>
#include<cstring>
#include<list>
#include<cmath>
#include<fstream>
#include<algorithm>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("Asmall.out","w",stdout);
    int t,x,y;
    int r,k;
    scanf("%d",&t);
    int i=0,j=0;
    while(i<t)
    {
        cin>>r>>k;
        j=0;
        x=2*r+1;
        y=2*r+1;
        while(y<=k)
        {
            x=x+4;
            y=y+x;
            j++;
        }
        cout<<"Case #"<<i+1<<": "<<j<<endl;
        i++;
    }
    return 0;
}
