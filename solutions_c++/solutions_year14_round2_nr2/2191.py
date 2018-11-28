#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>

using namespace std;

bool subA[10];
bool subB[10];

int main(){
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    cin>>T;
    int pot[10];
    pot[0]=1;
    for(int i=1;i<10;i++) pot[i]=pot[i-1]*2;
    for(int i=1;i<=T;i++){
        int A, B, K;
        cin>>A>>B>>K;
        int res=0;
        for(int subA=0;subA<A;subA++){
            for(int subB=0;subB<B;subB++){
                int numA=subA, numB=subB;
                int nuevo=0;
                for(int j=9;j>=0;j--){
                    bool posA=false, posB=false;
                    if(numA>=pot[j]){
                        numA-=pot[j];
                        posA=true;
                    }
                    if(numB>=pot[j]){
                        numB-=pot[j];
                        posB=true;
                    }
                    if(posA && posB) nuevo+=pot[j];
                }
                if(nuevo<K) res++;
            }
        }
        cout<<"Case #"<<i<<": "<<res<<endl;
    }
    return 0;
}
