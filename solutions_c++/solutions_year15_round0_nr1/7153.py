#include <fstream>
using namespace std;

ifstream in("ovation.in");
ofstream out("ovation.out");

int T;

int main()
{
    int i, smax, nr,nrsup,priet,j,x;
    char s[1105],c;
    in>>T;
    for(i=1;i<=T;i++){
        in>>smax;
        in.get(s,1105);
        //out<<s<<"\n";
        x=(int)s[1]-48;
        nrsup=0;
        nr=x;
        for(j=1;j<=smax;j++){
            x=(int)s[j+1]-48;
            priet=0;
            //out<<x<<" "<<j<<" "<<nr<<"\n";
            if(x!=0 && nr<j){
                priet=j-nr;
                nrsup+=priet;
            }
            nr=nr+x+priet;
        }
        out<<"Case #"<<i<<": "<<nrsup<<"\n";
    }

    return 0;
}
