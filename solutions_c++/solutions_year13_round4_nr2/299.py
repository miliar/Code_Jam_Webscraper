#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<iomanip>
#include<fstream>
#include<ctime>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair <int,int> ii;
typedef long long LL;
#define pb push_back
const int INF = 2147483647;

LL p,musi,d,moze;
int n,z,q;

int zk (int n, LL p) {
    if (p <= (1LL << (n-1))) return 1; 
    return 1 + zk(n-1, p-(1LL << (n-1)));
}

int main() {
scanf("%d",&z);
for (q=1;q<=z;q++) {
    cin >> n >> p;
    if (p==(1LL<<n)) musi = (1LL<<n) - 1; else musi = (1LL << zk (n,p)) - 2;
    if (p==1) moze = 0; else {
       d = 2;
       while (d*2<=p) d*=2;
       moze = 0;
       for (d=d;d>=2;d/=2) moze+=(1LL<<n)/d;
    }
    cout << "Case #" << q << ": " << musi << " " << moze << endl;
}
return 0;
}
