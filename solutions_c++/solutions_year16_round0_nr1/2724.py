// template.cpp : Defines the entry point for the console application.
//
#include <climits>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <list>
#include <tuple>
#include <ctime>
#include <cassert>
using namespace std;


//type shortcuts
typedef long long ll;
typedef vector<ll> VI;
typedef long double DOUBLE;
typedef vector<DOUBLE> VD;
typedef vector<VD> VVD;


//constants
const DOUBLE EPS=1e-9;
const DOUBLE PI = atan(1) * 4;
const ll M = 1000000007;


bool bm[10]={};
void clear(){
    for (int i=0;i<10;++i){
        bm[i]=false;
    }
}
void updatewith(int x){
    if (x==0){
        bm[x]=true;
        return;
    }
    while (x>0){
        int d=x%10;
        bm[d]=true;
        x/=10;
    }
}
bool fulfilled(){
    for (int i=0;i<10;++i){
        if (bm[i]==false) return false;
    }
    return true;
}
int main()
{
    int TN;cin>>TN;
    for (int TI=1;TI<=TN;++TI)
    {
        int n;cin>>n;
        if (n==0) {
            cout<<"Case #"<<TI<<": INSOMNIA"<<endl;
            continue;
        }
        ll i=1;
        clear();
        while (true) {
            ll crt=i*n;
            updatewith(crt);
            if (fulfilled()) {
                cout<<"Case #"<<TI<<": "<<crt<<endl;
                break;
            }
            ++i;
        }
    }
    return 0;
}
