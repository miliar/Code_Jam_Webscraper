#include <iostream>
#include<fstream>
#include<stdio.h>

using namespace std;

int main()
{
    int t;
    ifstream mcin("B-large.in");
    FILE* mcout=fopen("B-large.out","w");
    mcin>>t;
    for(int i=0;i<t;++i){
        double c,f,x,v;
        mcin>>c>>f>>x;
        v=2;
        double ts=0;
        double pts=x/v;
        while(true){
            ts+=c/v;
            v+=f;
            if(ts+x/v>=pts){
                break;
            }
            else{
                pts=ts+x/v;
                //cout<<pts<<endl;
            }
        }
        fprintf(mcout,"Case #%d: %.7f\n",i+1,pts);
    }
    mcin.close();
    fclose(mcout);
    return 0;
}
