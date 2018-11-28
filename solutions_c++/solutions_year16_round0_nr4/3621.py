#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

ifstream in("d.in");
ofstream out("d.out");

int main()
{
    int t;
    in>>t;
    for(int i=1;i<=t;++i){
        long long k,c,s;
        in>>k>>c>>s;

        out<<"Case #"<<i<<":";
        for(int j=1;j<=k;++j)out<<" "<<j;
        out<<endl;
        /*long long ans=k/c;
        if(k%c!=0)++ans;
        if(s<ans)out<<"Case #"<<i<<": IMPOSSIBLE";
        else{
            out<<"Case #"<<i<<":";
            for(long long j=0;j<k;j+=c){
                long long n=1;
                for(long long l=0;l<c;++l)n+=((j+l)%k)*(long long)pow(k,c-l-1);
                out<<" "<<n;
            }
        }
        out<<endl;*/
    }
    return 0;
}
