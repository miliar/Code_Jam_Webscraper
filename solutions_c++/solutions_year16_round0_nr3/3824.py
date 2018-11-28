//Pranet Verma
#include <bits/stdc++.h>
using namespace std;
// To get the next higher number with the same number of 1 bits:
unsigned long long nexthi_same_count_ones(unsigned long long a) {
  /* works for any word length */
  unsigned long long c = (a & -a);
  unsigned long long r = a+c;
  return (((r ^ a) >> 2) / c) | r;
}
int done;
string bin(unsigned long long curr) {
    string bin;
    do {
        bin+=('0' + (curr & 1));
        curr >>= 1;
    }
    while(curr);
    reverse(bin.begin(), bin.end());
    return bin;
}
vector<int> primes;
bool isCool(const string &s, int base, int p) {
    int ret = 0;
    for (auto c : s) {
        ret = (ret * base + c - '0' ) % p;
    }
    return ret == 0;
}
void process(const string& s) {
    vector<int> ans;
    for (int i = 2; i <= 10; ++i) {
        int ret = -1;
        for (auto p : primes) {
            if (isCool(s, i, p)) {
                ret = p;
                break;
            }
        }
        if(ret == -1) {
            return;
        }
        ans.push_back(ret);
    }
    cout<<s<<" ";
    for (auto c : ans)
        cout<<c<<" ";
    cout<<endl;
    ++done;
}
bool* isPrime;
void generatePrimeSieve(const int lim)
{
  isPrime=(bool *)malloc(lim+1);
  memset(isPrime,true,lim+1);
  isPrime[0]=false;
  isPrime[1]=false;
  for(int i=2;i<=lim;++i)
    if(isPrime[i]) {
        primes.push_back(i);
      for(int j=i+i;j<=lim;j+=i)
        isPrime[j]=false;
    }
}
int main()
{
    generatePrimeSieve(100);
    int t;
    scanf("%d", &t);
    while (t--) {
        cout<<"Case #1:\n";
        int n, j;
        scanf("%d %d", &n, &j);        
        unsigned long long mask = (1LL << (n - 1)) | 1;
        unsigned long long lim = (1LL << (n - 2));
        for (int sb = 1; sb <= n - 2; sb += 2) {
            unsigned long long curr = (1LL << sb) - 1;
            while (curr < lim) {
                unsigned long long temp = curr;
                temp <<= 1;
                temp |= mask;
                process(bin(temp));
                if (done == j) {
                    return 0;
                }
                curr = nexthi_same_count_ones(curr);
            }
        }
    }     
    assert(false);
}