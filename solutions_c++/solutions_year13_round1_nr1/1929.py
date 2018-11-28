#include <fstream>
using namespace std;

int main()
{
    ifstream in("F:\\A-small-attempt0.in");
    ofstream out("F:\\output.txt");

    int T=0;
    in>>T;

    int r,t;
    for(int i=0;i<T;i++){
        in>>r;
        in>>t;
        int num=0;
        int tmp = (r+1)*(r+1)-r*r;
        while(t>=tmp){
            t -=tmp;
            num++;
            r+=2;
            tmp = (r+1)*(r+1)-r*r;
        }
        out<<"Case #"<<i+1<<": "<<num<<endl;
    }
    return 0;
}
