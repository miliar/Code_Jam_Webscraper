#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;
typedef long long int ll;
int dict[4][4] = {{1, 2,  3,  4}, 
                  {2, -1, 4, -3}, 
                  {3, -4, -1, 2}, 
                  {4, 3, -2, -1}};

int multi(int x, int y) {
    if(x * y < 0) {
        if(x<0) x = -x;
        if(y<0) y = -y;
        x = x - 1;
        y = y - 1;
        return -dict[x][y];
    } else {
        x = x - 1;
        y = y - 1;
        return dict[x][y];
    }
}

string process(string str, long long int x) {
    int L = str.size();
    int *data = new int[L];
    for(int i=0; i<L; i++) {
        data[i] = str[i] - 'i' + 2;
    } 
    int re = 1;
    bool findi = false, findj = false, findk = false;
    ll total = x * L;
    for(ll i=1; i<=total; i++) {
            re = multi(re, data[(i-1)%L]);
            if(re == 2) findi = true;
            if(findi && re == 4) findj = true;
            //if(re == 1 && i>=L) i = total / i * i;
    }

    delete data;
    if(findi && findj && re == -1) return "YES";
    else return "NO";
}

int main() {
    int T;
    cin>>T;
    for(int tcas=1; tcas<=T; tcas++) {
        long long int L, X;
        cin>>L>>X;
        string str;
        cin>>str;
        cout<<"Case #"<<tcas<<": "<<process(str, X)<<endl;
    }
}
        
