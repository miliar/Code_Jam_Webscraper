#include <iostream>
#include <fstream>

using namespace std;

ifstream f("A-large.in");
ofstream g("output.txt");
int main()
{
    long long T,n,viz[10]={0};
    f>>T;
    for (long long i=1;i<=T;i++){
        f>>n;
        long long ok=1,nr=n;
        if (n==0){
            g<<"Case #"<<i<<": INSOMNIA"<<'\n';
        }
        else {
            while (ok){
                long long cn=nr;
                ok=0;
                int ok1=0;
                while (cn){
                    if (viz[cn%10]==0){
                        viz[cn%10]=1;
                        ok1=1;
                    }
                    cn/=10;
                }
                for (long long i=0;i<=9;i++){
                    if (!viz[i]){
                        ok=1;
                    }
                }
                nr+=n;
            }
            for (long long i=0;i<=9;i++){
                viz[i]=0;
            }
            g<<"Case #"<<i<<": "<<nr-n<<'\n';
        }
    }
    return 0;
}
