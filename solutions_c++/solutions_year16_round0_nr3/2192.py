#include <bits/stdc++.h>
using namespace std;

long long numberofsetbits(long long x, long long m){
    long long ans = 0, temp = x&m;
    while(temp){
        ans += temp%2;
        temp /= 2;
    }
    return ans;
}

int main(){
    freopen("Cin.txt", "r", stdin);
    freopen("Cout.txt", "w", stdout);
	ios::sync_with_stdio(false); cin.tie(0);
	int T;
	cin>>T;
    cout<<"Case #1:\n";
    long long n, k;
    cin>>n>>k;
    long long printed = 0;
    for(long long i=((1LL<<(n - 1))|1) ; i<(1LL << n)&&printed<k ; i+=2){
        if(numberofsetbits(i,733007751850) != numberofsetbits(i,366503875925))
            continue;
        long long x = i;
        vector<int> v;
        while(x){
            v.push_back(x%2);
            x /= 2;
        }
        while(v.size()<n)
            v.push_back(0);
        for(int j = v.size()-1 ; j>=0 ; --j)
            cout<<v[j];
        cout<<" ";
        for(int j=3; j<=11 ; ++j)
            cout<<j<<" ";
        cout<<"\n";
        printed++;
    }
}
