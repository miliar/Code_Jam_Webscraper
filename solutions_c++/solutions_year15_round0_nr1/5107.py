#include <iostream>
#include <fstream>
using namespace std;
ifstream f("input");
ofstream o("output");
int main()
{
    int i,t,l,j,nr,total,toAdd=0;
    char c;
    f>>t;
    for(i=1;i<=t;i++){
        f>>l;
        f.get();
        total=0;
        toAdd=0;
        for(j=0;j<=l;j++){
            f.get(c);
            nr=c-48;
            if(total<j){
                toAdd+=j-total;
                total+=j-total;
            }
            total+=nr;
        }
        o<<"Case #"<<i<<": "<<toAdd<<endl;
    }
    return 0;
}
