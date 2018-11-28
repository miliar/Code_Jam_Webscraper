#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
    int T,j=1;
    ofstream out;
    out.open("output.txt");
    ifstream in;
    in.open("input.txt");
    in>>T;
    while(j<=T) {
        int Smax;
        string lis;
        in>>Smax>>lis;
        int count=0,tot=0;
        tot+=lis[0]-'0';
        for(int i=1;i<lis.size();i++) {
           if(i>tot) {
                count+=i-tot;
                tot=i;
           }
           tot+=lis[i]-'0';
        }
        out<<"Case #"<<j<<": "<<count<<endl;
        j++;
    }
    out.close();
    in.close();
    return 0;
}
