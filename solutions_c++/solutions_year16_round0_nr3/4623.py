#include <iostream>
#include <math.h>
#include <bits/stdc++.h>
#include <set>
#include <map>
using namespace std;

typedef unsigned long long ull;
set <ull> prev;
map <ull,int> PREV;

ull get_factor(ull x){
    /////for small dataset
    if(x==2 || x==3)
        return 0;
    else if(x%2 ==0)
        return 2;
    int limit = ull(ceil(sqrt(x)));
    for(int i=3;i<=limit;i+=2){
        if(x%i == 0)
            return i;
    }
    return 0;
}

ull get_in_base_10 (ull x, int base){
    ull res = 0;
    ull cumulation_base = 1;
    while(x!=0){
        if(x%10 == 1)
            res += cumulation_base;
        cumulation_base *= base;
        x /= 10;
    }
    return res;
}

bool try_bases(ull x){
    int factors[9];
    ull temp;
    for(int i=2;i<=10;i++){
        temp = get_factor(get_in_base_10(x,i));
        if(!temp)
            return false;
        factors[i-2] = temp;
    }
    cout<<x<<" ";
    for(int i=0;i<8;i++)
        cout<<factors[i]<<" ";
    cout<<factors[8]<<endl;
    return true;
}

void perm(int N,int &J,ull res){
    if(!J)
        return;
    if(!N){
        if(PREV.count(res)>0 /*prev.find(res) == prev.end()*/)
                return;
        if(try_bases(res)){
            PREV[res] = 0;
            J--;
        }
        return;
    }
    //cout<<N<<","<<pow(10,N)<<endl;
    perm(N-1,J,res+10*pow(10,N));
    perm(N-1,J,res);
}

int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-large.in", "r", stdin);
    //freopen("Input.txt", "r", stdin);
    freopen("OutputC.txt", "w", stdout);
    int T,N,J;
    cin>>T>>N>>J;
    //for small test
    ull alternatives = 1000000000000001;

    for(int i=1;i<=T;i++){
        cout<<"Case #"<<i<<":"<<endl;
        perm(N-3,J,alternatives);
    }
    return 0;
}
