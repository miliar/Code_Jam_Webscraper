#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <math.h>
using namespace std;

int main()
{
    ifstream file("1.in");
    ofstream o("1.out");
    if (!file.is_open())
        cout<<"error";
    string t;
    getline(file,t);
    long long  _t = atoi( t.c_str() );

    string str[101];
    for(int i=0; i<_t; i++) {
        long int a,b,k,ans=0;
        file>>a;
        file>>b;
        file>>k;
        for(int j=0;j<a;j++){
            for(int l=0;l<b;l++){
                if((j&l)<k) {
                    ans++;
                }
            }
        }
        o<<"Case #"<<i+1<<": "<<ans<<'\n';
        }
    return 0;
}
 
