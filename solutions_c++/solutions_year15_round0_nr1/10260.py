#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int Smax;
string buffer;
int P[1005];
int cal(){
    int add=0;
    int n=P[0];
    for(int i=1;i<=Smax;i++){
        if(P[i]>0){
            if(n>=i)n+=P[i];
            else {
               add+=i-n;
               n+=add+P[i];
            }
        }
    }
    //cout<<P[0]<<endl;
    return add;
}
int main()
{
    ifstream in;in.open("A-small-attempt2.in",ifstream::in);
    if(!in.is_open())return -1;
    ofstream out("A-small-output.txt");
    if(!out.is_open())return -1;
    int T;in>>T;
    int t=1;
    while(T--){
        in>>Smax;
        in>>buffer;
        for(int i=0;i<=Smax;i++){
            P[i]=buffer[i]-48;
        }
        int ans=cal();
        out<<"Case #"<<t++<<": "<<ans<<endl;
    }
    in.close();
    out.close();
}
