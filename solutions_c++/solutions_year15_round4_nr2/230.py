#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<cstring>
using namespace std;


int N;
long double V,X;
long double epsilon = 1e-10;

struct pipe {
    long double r,c;
    bool operator<(const pipe& o) const {
        return c<o.c;
    }
};


vector<pipe> p;

long double low_end(long double t) {
    long double amount=0;
    long double sum = 0;
    for(int i=0;i<N;i++) {
        if(p[i].r * t + amount < V) {
            amount += p[i].r * t;
            sum += p[i].r * t * p[i].c;
        } else {
            sum += (V-amount) * p[i].c;
            break;
        }
    }
    return sum/V;
}
long double high_end(long double t) {
    long double amount=0;
    long double sum = 0;
    for(int i=N-1;i>=0;i--) {
        if(p[i].r * t + amount < V) {
            amount += p[i].r * t;
            sum += p[i].r * t * p[i].c;
        } else {
            sum += (V-amount) * p[i].c;
            break;
        }
    }
    return sum/V;
}

bool possible(long double time) {
    if(low_end(time) - epsilon < X && high_end(time) + epsilon > X) return true;
    return false;
}


void f() {
    cin>>N;
    cin>>V>>X;
    p.resize(N);
    for(int i=0;i<N;i++) {
        cin>>p[i].r>>p[i].c;
    }

    sort(p.begin(),p.end());
    long double low = epsilon;
    long double high = 1e10;
    if(!possible(high)) {
        cout<<"IMPOSSIBLE\n";
        return;
    }
    while(high-low > epsilon) {
        long double mid = (high+low)/2;
        if(possible(mid)) high=mid;
        else low=mid;
    }

    cout<<low<<endl;




}


int main() {
    int t;
    cin>>t;
    cout<<setprecision(20);
    for(int a=1;a<=t;a++) {
     cout<<"Case #"<<a<<": ";
     f();
    }
}
