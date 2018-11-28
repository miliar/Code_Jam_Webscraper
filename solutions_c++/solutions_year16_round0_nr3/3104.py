#include<bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)

using namespace std;

typedef long long ll;

const int mn = 0b1000000000000001;
const int mx = 0b1111111111111111;

int is_prime(ll n){
    for(int i = 2; i*1ll*i < n; i++)if(n % i == 0)return i;
    
    return -1;
}

ll read_in_base(int num, int base){
    ll ret = 0;
    ll mult = 1;
    for(int i = 0; num > 0; i++){
        ret+=mult*(num&1);
        num>>=1;
        mult*=base;
    }
    return ret;
}

int rnd(int a, int b){
    return a + (rand() % (b-a+1));
}

set<pair<int, vector<int> > > nums;

void test_jamcoin(int n){
    vector<int> divs;
    for(int b = 2; b <= 10; b++){
        int div = is_prime(read_in_base(n, b));
        if(div == -1)return;
        divs.push_back(div);
    }
    nums.insert(make_pair(n, divs));
    cerr << "Found " << n << endl;
}




int main(){
    srand(time(NULL));
    assert(RAND_MAX >= mx);

    cerr << mn << " " << mx << endl;
    while(nums.size() < 50){
        int n = rnd(mn, mx);
        n|=1;
        test_jamcoin(n);
    }


    for(auto x : nums){
        printf("%lld", read_in_base(x.first, 10));
        for(auto d : x.second)printf(" %d", d);
        printf("\n");
    }

	return 0;
}
