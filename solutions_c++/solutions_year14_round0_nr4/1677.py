#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <unordered_set>
#include <stdio.h>
#include <string.h>
#include <unordered_map>
#include <fstream>
#include <set>
using namespace std;

#define MOD 1000000007
#define ll long long

ifstream fin("in.txt");
ofstream fout("out.txt");


int main(){
    int t;
    fin>>t;
    for(int asdasd=0; asdasd<t; asdasd++){
        set<double> A,B;

        int n;
        fin>>n;

        for(int i=0; i<n; i++){
            double a;
            fin>>a;
            A.insert(a);
        }

        for(int i=0; i<n; i++){
            double a;
            fin>>a;
            B.insert(a);
        }
        set<double> A2=A,B2=B;

        int v2=0;
        while(A.size()){
            double a=*A.begin();
            A.erase(a);
            if(B.lower_bound(a)==B.end()){
                v2++;
                B.erase(*B.begin());
            }else{
                B.erase(*B.lower_bound(a));
            }
        }

        int v1=0;
        while(A2.size()){
            double a=*B2.begin();
            B2.erase(a);
            if(A2.lower_bound(a)==A2.end()){
                A2.erase(*A2.begin());
            }else{
                v1++;
                A2.erase(*A2.lower_bound(a));
            }
        }
        fout<<"Case #"<<asdasd+1<<": "<<v1<<" "<<v2<<endl;
    }
    return 0;
}
