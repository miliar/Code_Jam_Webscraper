#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define IT(a,it) for(auto it=a.begin(); it != a.end(); it++)
#define REV_IT(a,it) for(auto it=a.rbegin(); it != a.rend(); it++)
#define LL long long
#define ll long long
#define LD long double
#define MP make_pair
#define FF first
#define SS second
#define PB push_back
#define INF (int)(1e9)
#define EPS (double)(1e-9)

#ifndef ONLINE_JUDGE
#  define LOG(x) cerr << #x << " = " << (x) << endl
#else
#  define LOG(x) 0
#endif

#define MAXX 100000008

using namespace std;

typedef pair <int, int> pi_i;
typedef pair<int, pi_i> pi_ii;

bool cmp(int a, int b){ return a>b; }
template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> T lcm(T a, T b) { return a * (b / gcd(a, b)); }

LL n, J;

LL mulmod(LL a, LL b, LL mod){
    LL x = 0,y = a % mod;
    while (b > 0)
    {
        if ((b % 2LL) == 1LL)
        {    
            x = (x + y) % mod;
        }
        y = (y * 2LL) % mod;
        b /= 2LL;
    }
    return x % mod;
}

LL modulo(LL base, LL exponent, LL mod){
    LL x = 1LL;
    LL y = base;
    while (exponent > 0)
    {
        if (exponent % 2LL == 1)
            x = (x * y) % mod;
        y = (y * y) % mod;
        exponent = exponent / 2LL;
    }
    return x % mod;
}
 
bool Miller(LL p,int iteration){
    if (p < 2LL)
    {
        return false;
    }
    if (p != 2LL && p % 2LL==0)
    {
        return false;
    }
    ll s = p - 1;
    while (s % 2LL == 0)
    {
        s /= 2LL;
    }
    for (int i = 0; i < iteration; i++)
    {
        ll a = rand() % (p - 1) + 1, temp = s;
        ll mod = modulo(a, temp, p);
        while (temp != p - 1 && mod != 1 && mod != p - 1)
        {
            mod = mulmod(mod, mod, p);
            temp *= 2LL;
        }
        if (mod != p - 1 && temp % 2LL == 0)
        {
            return false;
        }
    }
    return true;
}

LL factor(LL no){
	for(LL i = 2;i*i <= no;i++){
		if(no % i == 0) return i;
	}
	return -1;
}

LL getNo(LL vv, LL base){
	LL ans = 0, poww = 1LL;
	while(vv > 0){
		if(vv & 1LL) ans += poww;
		vv = vv >> 1LL;
		poww = poww * base;
	}
	return ans;
}

int main(){
	ios_base::sync_with_stdio(false);
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T, casee = 1;
	cin >> T;
	for(casee=1;casee<=T;casee++){
		cout << "Case #" << casee << ": " ;
		cout << endl;
		cin >> n >> J;
		int ct = 0;
		vector<string> ans;
		vector<LL> ans2[1000], ans3;
		for(LL i = (1LL << (n-1));i < ((1LL << (n))-1);i++){
			//if(i < (1LL << (n-1))) continue;
			if((i & 1) == 0) continue;
			if(ct == J) break;
			bool fd = true;
			vector<LL> ttt;
			for(LL j = 2;j <= 10;j++){
				LL candidate = getNo(i, j);
				if(Miller(candidate, 10) == true) fd = false;
				else{
					LL oooo = factor(candidate);
					if(oooo == -1) fd = false;
					else ttt.push_back(oooo), ans3.push_back(candidate);
				}
			}
			if(fd == true){
				LL val = i;
				string temp = "";
				while(val > 0){
					if(val & 1) temp += '1';
					else temp += '0';
					val = val >> 1LL;
				}
				reverse(temp.begin(), temp.end());
				ans.push_back(temp);
				//cout << temp << " : ";

				for(int ii = 0;ii < ttt.size();ii++) /*cout << ans3[ii] << " " << ttt[ii] << " ", */ans2[ct].push_back(ttt[ii]);
				ct++;
			}
		}
		for(LL i = 0;i < ans.size();i++){
			cout << ans[i] << " ";
			for(LL j = 2;j <= 10;j++){
				cout << ans2[i][j-2] << " ";
			}
			cout << endl;
		}
	}
	fclose(stdin);
	fclose(stdout);
return 0;	
}

