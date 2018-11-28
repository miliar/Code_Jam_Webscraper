#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;
main()
{
    freopen("C-small-attempt0.in", "r", stdin); freopen("a.out", "w", stdout);
    bool b[1001];
    for(int i=0;i<1001;i++)b[i]=false;
    int n,a,c;
    scanf("%d",&n);
    b[1]=b[4]=b[9]=b[121]=b[484]=true;
    for(int i=1;i<=n;i++)
    {
        int con=0;
        scanf("%d %d",&a,&c);
        for(int u=a;u<=c;u++)
        if(b[u])con++;
        cout<<"Case #"<<i<<": "<<con<<endl;
    }


}
