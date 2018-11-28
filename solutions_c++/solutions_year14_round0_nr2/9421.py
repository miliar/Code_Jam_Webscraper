#include<bits/stdc++.h>

//#define fin cin
//#define fout cout
#define LL long long
#define pb push_back
#define pi acos(-1)
#define MOD 1000000007
#define MX 32622
#define eps 1e-7
using namespace std;

int main(){
    ofstream fout ("output.out");
    ifstream fin ("input.in");
    int test;
    fin>>test;
    for(int kase=1;kase<=test;kase++){
        double req,tar,in,rate=2.0;
        fin>>req>>in>>tar;
        double mn=tar/rate;
        double sum=0.0;
        while(1){
            double rt=req/rate;
            double nr=tar/(rate+in);
            if(sum+rt+nr+eps<mn){
                mn=sum+rt+nr;
                sum+=rt;
            }
            else break;
            rate+=in;
        }
        fout<<"Case #"<<kase<<": ";
        fout<<std::fixed;
        fout<<std::setprecision(7)<<mn<<endl;
    }
    return 0;
}
