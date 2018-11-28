#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<list>
#include<math.h>
#include<algorithm>
#include<string>
#include<set>
#include<queue>
#include<fstream>
#define limit 1048576
#define inf 9223372036854775807ll
#define iinf 2147483647
#define mp make_pair
#define pb push_back
using namespace std;
int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w",stdout);
    cout.precision(12);
    int t;
    double tim,C,F,X;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>C >> F >>X;
        tim=0;
        int k=0;
        while(F*X-2*C>(k+1)*F*C){
            tim+=C/(2+k*F);
            k++;
        }
        tim+=X/(2+k*F);
        cout<<"Case #"<<i<<": "<<tim<<"\n";
    }
    return 0;
}
