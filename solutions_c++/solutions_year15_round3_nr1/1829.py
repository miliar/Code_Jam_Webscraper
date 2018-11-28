#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

int main()
{
    int t,iCase=0;
    int r,c,w;
    FILE *out=fopen("1.out","w");
    fstream in("A-small-attempt0.in");
    //cin>>t;
    in>>t;
    while(t--)
    {
        //cin>>r>>c>>w;
        in>>r>>c>>w;
        int co=0;
        for (int i=1;i<=c;i+=w)
            co++;
        fprintf(out,"Case #%d: %d\n",++iCase,co*r+(w-1));
    }
    return 0;
}
