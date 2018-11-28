#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <fstream>
typedef long long ll;
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    ifstream cn;
    cn.open("A-large.in");

    ofstream cot;
    cot.open("OutPut.txt");

    int n;
    cn>>n;
    for(int i=0;i<n;i++){
    ll k;
    cn>>k;

    if(k==0){
    cot<<"Case #"<<i+1<<": INSOMNIA"<<endl;
    continue;
    }

    int aray[10];
    for(int j=0;j<10;j++)
        aray[j]=0;

    int c=1;
    bool flag=true;

    while(flag){
        ll t=k*c++;
        while(1){
            aray[t%10]=1;
            t/=10;
            if(t==0)
            break;
        }
        flag=false;
        for(int j=0;j<10;j++)
            if(aray[j]==0)
                flag=true;
    }
    cot<<"Case #"<<i+1<<": "<<k*(c-1)<<endl;
    }
    return 0;
}
