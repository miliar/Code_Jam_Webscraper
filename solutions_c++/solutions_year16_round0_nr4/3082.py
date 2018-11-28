#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    in.open("E:\\project\\D-small-attempt0.in");
    out.open("E:\\project\\d-small.txt");
    int t,k,c,s,x=0;
    in>>t;
    while(t--){
        x++;
        in>>k>>c>>s;
        out<<"Case #"<<x<<": ";
        for(int i=1;i<=k;i++){
            if(i>1)out<<" ";
            out<<i;
        }
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
