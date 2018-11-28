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
    cn.open("B-large.in");

    ofstream cot;
    cot.open("OutPut.txt");

    int n;
    cn>>n;
    for(int i=0;i<n;i++){             //START
    string k;
    cn>>k;

    int c=1;
    int sz=k.size()-1;
    for(int j=sz;j>=0;j--){
        if(k[j]=='+' && j==sz)
            c--;
        if(j!=sz && k[j]!=k[j+1])
            c++;
    }
    cot<<"Case #"<<i+1<<": "<<c<<endl;
    }
    return 0;
}
