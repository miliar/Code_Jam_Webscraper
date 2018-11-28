#include <bits/stdc++.h>

#define digits(num) (num == 0 ? 0 : (int)((log(abs(num))/log(10))+1))
#define first_bit_index(num) (num == 0 ? 0 : __builtin_ctz(abs(num))) // count trailing zeros (e.g: 8 1000, so ans: 4)
#define last_bit_index(num) (num == 0 ? 0 : __builtin_clz(abs(num))) // count leading zeros (e.g: 8 0x27 1000, so ans: 28)
#define check_bit(num, bit) ((num & 1 << bit) != 0)
#define num_bits(num) __builtin_popcount(num) //count 1 bits
#define get_low_bit(x) ((x)&((x)^((x)-1))) //get the lowest bit of x
#define set_bit(num, bit) num |= (1 << bit);
#define reset_bit(num, bit) num &= ~(1 << bit);
#define flip_bit(num, bit) num ^= (1 << bit);
#define fi first
#define se second
#define mp make_pair
#define IOS ios_base::sync_with_stdio(0); 
#define therms(type, func) type, vector<type>, func //usefull with priority queues
#define in(a,b) ( (b).find(a) != (b).end())
#define EPS 1e-9
#define INF 1000000000
#define DIM 5
#define MOD 100000009
#define is_pow2(num) (int)(num && !(num & (num - 1)))
#define cls(arr) memset(arr, 0, sizeof arr);

using namespace std;

typedef struct t { int a; bool operator<(const t &cpy) const { return a < cpy.a; } } t; //usefull with sort and sets
typedef struct cmp { bool operator()(const int& a, const int& b) const { return a > b; } } cmp; //usefull with priority queues

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

template<typename T> void swap(T *f, T *s) { *f = *f ^ *s; *s = *f ^ *s; *f = *f ^ *s; }
template<typename F,typename S> ostream& operator<<(ostream &s, pair<F,S> t) { return s<<"("<<t.fi<<","<<t.se<<")"; } //print pair
template<typename T> ostream& operator<<(ostream &s, vector<T> t){ //print vector
	for(int i = 0, sz = t.size(); i < sz; i++) s << t[i] <<" ";return s; }


typedef struct compare { bool operator()(const ii& a, const ii& b) const { return a.se < b.se; } } compare; //usefull with priority queues


int main()
{
	IOS
	int T, N, p[26], aux;
	priority_queue<therms(ii, compare)> pq;

	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ":";
		cin >> N;

		for(int i = 0; i < N; i++) {
			cin >> p[i];
			pq.push(mp(i,p[i]));
		}
		int n = 1; string s;
		while(!pq.empty()) {
			ii front = pq.top(); pq.pop();
			
			if(n++%2==1) s+= " ";
			s+=(char)(front.fi+'A');
			
			front.se -= 1;
			if(front.se > 0) pq.push(mp(front.fi, front.se));
		}

		int x = 0, size = s.size(); string ss;
		for(int i = size-1; s[i] >= 'A' && s[i] <= 'Z'; i--) x++;
		if(x == 1) {
			for(int i = 0; i < size - 4; i++)
				cout << s[i];
			cout << s[size-1];
			cout << " " << s[size-3] << s[size-4];
		} else {
			cout << s;
		}
		cout << endl;
	}

	return 0;
}
