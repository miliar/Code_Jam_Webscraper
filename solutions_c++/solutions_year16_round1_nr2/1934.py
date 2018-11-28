#include <iostream>
#include <fstream>
using namespace std;

ifstream in("data.in");
ofstream out("data.out");

const int N = 2501;
int f[N];
int t, n, x;

void init(){
    for(int i=0;i<N;i++)
        f[i]=0;
}

int main()
{
    in>>t;
    for(int i=0;i<t;i++){
        init();
        in>>n;
        for(int j=0;j<2*n - 1;j++){
            for(int k=0;k<n;k++) {
                in>>x;
                f[x]++;
            }
        }
        int c=0;
        out<<"Case #"<<i+1<<": ";
        for(int j=0;j<N;j++){
            if(f[j]%2 == 1){
                out<<j<<' ';
            }
        }
        out<<"\n";
    }
    return 0;
}
