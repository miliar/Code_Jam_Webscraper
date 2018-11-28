#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<ctime>
#include<cstdlib>
using namespace std;

vector<double> k,n;
set<double> ken;
int size;
int cse;
double kc(double n) {
    set<double>::iterator it = ken.lower_bound(n);
    if(it==ken.end()) {
        it = ken.begin();
    }
    double val = *it;
    ken.erase(it);
    return val;
}
bool can(int goal) {
    int kstart = 0;
    int nstart = size - goal;
    for(int i=0;i<goal;i++) {
        if(k[kstart++] > n[nstart++]) return false;
    }
    return true;
}
void t() {
    cin>>size;
    k.resize(size);
    n.resize(size);

    for(int i=0;i<size;i++) cin>>n[i];
    for(int i=0;i<size;i++) cin>>k[i];
    sort(k.begin(),k.end());
    sort(n.begin(),n.end());
    ken.clear();
    for(int i=0;i<k.size();i++) ken.insert(k[i]);

    int honest=0;
    for(int i=0;i<size;i++) {
        double nchoose = n[i];
        double kchoose = kc(nchoose);
        if(nchoose > kchoose) honest++;
    }

    int low=0;
    int high = size;
    while(high-low>1) {
        int mid = (low+high)/2;
        if(can(mid)) {

            low = mid;
        } else high=mid;
    }
    if(can(high)) cout<<high;
    else cout<<low;
    cout<<" ";
    cout<<honest<<"\n";

}
int main() {
    int tt;
    cin>>tt;
    for(int i=1;i<=tt;i++) {
        cse=i;
        cout<<"Case #"<<i<<": ";
        t();
    }
}
