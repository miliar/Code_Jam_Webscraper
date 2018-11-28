#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;



void megold(istream& in, ostream &out)
{
    int cnt;
    in>>cnt;
    int num[cnt];
    for(int i=0; i<cnt; i++) {
        in>>num[i];
    }

//    for(int i=0; i<cnt; i++) {
//        cout<<num[i]<<' ';
//    }

    int best=2000;
    for(int max=1; max<=1000; max++) {
        int time=max;
        for(int i=0; i<cnt; i++) {
            time+=(num[i]-1)/max;
        }

        if(time<best) {
            best=time;
            //cout<<"best at mx="<<max<<" t="<<time<<endl;
        }
    }

    out<<best;
}

int main()
{
    ifstream in("B-large.in");
    ofstream out("pancake.out");
    int n;
    in>>n;
    //out<<setprecision(12);
    for(int i=1; i<=n; i++)
    {
        out<<"Case #"<<i<<": ";
        megold(in, out);
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
