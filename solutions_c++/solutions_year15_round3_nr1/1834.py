#include<iostream>
#include<fstream>
using namespace std;
int main(){
    fstream in,out;
    in.open("input.txt",fstream::in);
    out.open("output.txt",fstream::out);
    int t,i=1;
    in>>t;
    while(i<=t) {
        int r,c,w;
        in>>r>>c>>w;
        int res = r*(c/w);
        if(w==c)
            res=w;
        //res+=c-(c/w)*w;
        else {
            res+=w-1;
            if(c%w>0)
                res+=1;
        }
        out<<"Case #"<<i<<": "<<res<<endl;
        i++;
    }
    return 0;
}
