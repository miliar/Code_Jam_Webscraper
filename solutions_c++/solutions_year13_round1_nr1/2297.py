#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
using namespace std;
 
int main()
{
    int e,i,j;
    long long a,b,c,d;
    cin>>e;
    i=1;
    while(e!=0)
    {
        cin>>b>>c;
        a=0;
        d=0;
        for(j=0;j<c;j=j+2)
        {
            a=a+(((b+j+1)*(b+j+1)-(b+j)*(b+j)));
            if(a>c)
                break;
            else
            d++;
        }
        cout<<"Case #"<<i<<":"<<" "<<d<<"\n";
        e--;
        i++;
    }
return 0;
}