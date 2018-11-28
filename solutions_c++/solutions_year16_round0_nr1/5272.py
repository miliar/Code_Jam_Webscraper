#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int ntc;
    cin>>ntc;
    for (int tc=1; tc<=ntc; ++tc) {
        vector<bool> in(10, false);
        long long n, t, k;
        cin>>n;
        cout<<"Case #"<<tc<<": ";
        if (n==0) {
            cout<<"INSOMNIA\n";
            continue;
        }
        int i=1;
        do {
            t=k=i*n;
            do {
                in[t%10]=true;
                t/=10; 
            } while (t>0);
            ++i;
        } while(find(in.begin(), in.end(), false)!=in.end());
        cout<<k<<'\n';
    }
    return 0;
}