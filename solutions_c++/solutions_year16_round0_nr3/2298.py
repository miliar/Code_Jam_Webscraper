#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef pair<ii, ii> iiii;
typedef pair<int, bool> ib;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vb> vvb;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<pll> vpll;

#ifdef __APPLE__
    ifstream fin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream fout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
#endif

int BIG_NUMBER = 1000000; // Small Dataset: 100,000      Large: 4,500,000,000

int T, N, J, counter = 0;
vb prime(BIG_NUMBER, true);

void genPrime() {
    prime[0] = false;
    prime[1] = false;
    for (ll i = 2; i < BIG_NUMBER; i++) {
        if (!prime[i]) continue;
        for (ll j = i * 2; j < BIG_NUMBER; j += i) {
            prime[j] = false;
        }
    }
}

bool isPrime(ll num) {
    if (num < BIG_NUMBER)
        return prime[num];
    if (num % 2 == 0) return false;
    for (int i = 3; i <= sqrt(num) + 1; i += 2)
        if (num % i == 0) return false;
    return true;
}

string gen = "10000000000000000000000000000000000000000000000001";

void checkJam() {
    string printer = "";
    for (int i = 2; i <= 10; i++) {
        ll num = strtoll(gen.substr(0, N).c_str(), NULL, i);
        if (isPrime(num)) return;
        ll div = -1;
        for (int j = 2; j < num; j++) {
            if (num % j == 0) {
                div = j;
                break;
            }
        }
        printer += " " + to_string(div);
    }
    fout << gen.substr(0, N) << printer << endl;
    counter++;
}

void generate(int pos) {
    if (counter >= J) return;
    if (pos == N - 1) {
        //fout << gen.substr(0, N) << endl;
        checkJam();
        return;
    }
    gen[pos] = '0';
    generate(pos+1);
    
    gen[pos] = '1';
    generate(pos+1);
}

int main() {
    fin >> T >> N >> J;
    genPrime();
    
    fout << "Case #1:" << endl;
    gen[N-1] = '1';
    generate(1);
    
    return 0;
}