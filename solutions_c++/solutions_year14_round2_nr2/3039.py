#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <fstream>
#define lli long long int
#define inpi(n) scanf("%d",&n)
#define inplli(n) scanf("%lld",&n)
#define inpf(n) scanf("%f",&n)
#define inpd(n) scanf("%lf",&n)
#define rep(i,n) for(i = 0; i < n; i++)
using namespace std;
int main(){
    int a, b , k,t,c;
    ifstream myfile("input.in");
    ofstream out("output.out");
    myfile>>t;
    for(int q = 1; q <=t; q++){
        myfile>>a>>b>>k;
        c = 0;
        for(int i = 0; i < a; i++){
            for(int j = 0; j < b;j++){
                if(int(i & j) < k)
                    c++;
            }
        }
        out<<"Case #"<<q<<": "<<c<<endl;
    }

}


