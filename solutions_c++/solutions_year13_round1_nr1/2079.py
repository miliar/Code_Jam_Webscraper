#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;



int main(){
    fstream input("input.txt"),output("out.txt");
    long long T,n;
    long long r,t;
    input >> T;
    int *a=new int[T];
    for(int i=0;i<T;i++){
        input>>r>>t;
        n=0;
        while((1+4*n+2*r)<=t){
            t-=(1+4*n+2*r);
            n++;
        }
        a[i]=n;
    }
    for(int i=0;i<T;i++)
        output<<"Case #"<<i+1<<": "<<a[i]<<endl;

    return 0;
}
