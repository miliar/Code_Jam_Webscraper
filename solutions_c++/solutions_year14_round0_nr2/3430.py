#include<iostream>
#include<fstream>
#include<algorithm>
#include<iomanip>

using namespace std;

double laik[1000005];
double kiek[1000005];

double C=0.0, F=0.0, X=0.0;

inline double farm(int K);
inline double rask(int N){
    if(laik[N]!=-1) return laik[N];
    if(N==0) return X/2;
    laik[N]=farm(N)+X/(N*F+2);
    return laik[N];
}

inline double farm(int K){
    if(kiek[K]!=-1) return kiek[K];
    if(K==0) return 0;
    if(K==1) return C/2;
    kiek[K]=farm(K-1)+C/((K-1)*F+2);
    return kiek[K];
}

int main()
{
    ifstream input("test.txt");
    ofstream output("output.txt");
    int T=0;
    input >> T;
    double ats=0.0;
    for(int i=0;i<T;i++){
            fill(laik,laik + 1000005,-1);
             fill(kiek,kiek + 1000005,-1);
            input >> C >> F >> X;
            ats=rask(0);
            for(long long int y=1;y<1000005;y++){
                ats=min(rask(y),ats);
                if(rask(y)==0) cout << y << endl;
                //cout << rask(y+1) << endl;
                //if(rask(y+1)>ats) break;
            }
            output  << "Case #" << i+1 << ": " <<fixed<<setprecision(20) << ats << endl;
    }
}
