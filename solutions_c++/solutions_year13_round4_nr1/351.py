#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <memory.h>
#include <cmath>
#include <pthread.h>
#include <semaphore.h>
#include <iomanip>

#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <algorithm>

#define ABS(a) ((a)<0?(-(a)):(a))
#define SIGN(a) (((a)>0)-((a)<0))
#define SQR(a) ((a)*(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define PI (3.1415926)
#define INF (2147483647)
#define INF2 (1073741823)
#define EPS (0.00000001)

#define MOD (1000002013)

#define y1 stupid_cmath
#define y0 stupid_cmath_too

using namespace std;

typedef long long LL;
template<typename T1,typename T2> ostream& operator<<(ostream &O,pair<T1,T2> t) {return O<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream& operator<<(ostream &O,vector<T> t){for(int _=0;_<(int)t.size();++_)O<<t[_]<<" ";return O; }

ifstream in("input.txt");
ofstream out("output.txt");

#define MAX_T 21
#define MAX_Threads 4
sem_t sem[MAX_T], sem_count;
pthread_t pthread[MAX_T];

class Answer{
public:
	int ans;
	friend ostream& operator <<(ostream& out, const Answer &a){
		out<<a.ans;
		return out;
	}
};


const int BI_base = 1e9;
const int BI_digits = 9;

class BI {
    vector<int> a;
    int sign;
public:
    BI() : sign(1) {}

    BI(long long v) {
        *this = v;
    }

    BI(const string &s) {
        read(s);
    }

    void operator=(const BI &v) {
        sign = v.sign;
        a = v.a;
    }

    void operator=(long long v) {
        sign = 1;
		a.clear();
        if (v < 0)
            sign = -1, v = -v;
        for (; v > 0; v = v / BI_base)
            a.push_back(v % BI_base);
    }
    BI operator+(const BI &v) const {
        if (sign == v.sign) {
            BI res = v;

            for (int i = 0, carry = 0; i < (int) max(a.size(), v.a.size()) || carry; ++i) {
                if (i == (int) res.a.size())
                    res.a.push_back(0);
                res.a[i] += carry + (i < (int) a.size() ? a[i] : 0);
                carry = res.a[i] >= BI_base;
                if (carry)
                    res.a[i] -= BI_base;
            }
            return res;
        }
        return *this - (-v);
    }

    BI operator-(const BI &v) const {
        if (sign == v.sign) {
            if (abs() >= v.abs()) {
                BI res = *this;
                for (int i = 0, carry = 0; i < (int) v.a.size() || carry; ++i) {
                    res.a[i] -= carry + (i < (int) v.a.size() ? v.a[i] : 0);
                    carry = res.a[i] < 0;
                    if (carry)
                        res.a[i] += BI_base;
                }
                res.trim();
                return res;
            }
            return -(v - *this);
        }
        return *this + (-v);
    }
    void operator*=(int v) {
        if (v < 0)
            sign = -sign, v = -v;
        for (int i = 0, carry = 0; i < (int) a.size() || carry; ++i) {
            if (i == (int) a.size())
                a.push_back(0);
            long long cur = a[i] * (long long) v + carry;
            carry = (int) (cur / BI_base);
            a[i] = (int) (cur % BI_base);
        }
        trim();
    }

    BI operator*(int v) const {
        BI res = *this;
        res *= v;
        return res;
    }
    friend pair<BI, BI> divmod(const BI &a1, const BI &b1) {
        int norm = BI_base / (b1.a.back() + 1);
        BI a = a1.abs() * norm;
        BI b = b1.abs() * norm;
        BI q, r;
        q.a.resize(a.a.size());

        for (int i = a.a.size() - 1; i >= 0; i--) {
            r *= BI_base;
            r += a.a[i];
            int s1 = r.a.size() <= b.a.size() ? 0 : r.a[b.a.size()];
            int s2 = r.a.size() <= b.a.size() - 1 ? 0 : r.a[b.a.size() - 1];
            int d = ((long long) BI_base * s1 + s2) / b.a.back();
            r -= b * d;
            while (r < 0)
                r += b, --d;
            q.a[i] = d;
        }

        q.sign = a1.sign * b1.sign;
        r.sign = a1.sign;
        q.trim();
        r.trim();
        return make_pair(q, r / norm);
    }

    BI operator/(const BI &v) const {
        return divmod(*this, v).first;
    }

    BI operator%(const BI &v) const {
        return divmod(*this, v).second;
    }
    void operator/=(int v) {
        if (v < 0)
            sign = -sign, v = -v;
        for (int i = (int) a.size() - 1, rem = 0; i >= 0; --i) {
            long long cur = a[i] + rem * (long long) BI_base;
            a[i] = (int) (cur / v);
            rem = (int) (cur % v);
        }
        trim();
    }

    BI operator/(int v) const {
        BI res = *this;
        res /= v;
        return res;
    }

    int operator%(int v) const {
        if (v < 0)
            v = -v;
        int m = 0;
        for (int i = a.size() - 1; i >= 0; --i)
            m = (a[i] + m * (long long) BI_base) % v;
        return m * sign;
    }
    void operator+=(const BI &v) {
        *this = *this + v;
    }
    void operator-=(const BI &v) {
        *this = *this - v;
    }
    void operator*=(const BI &v) {
        *this = *this * v;
    }
    void operator/=(const BI &v) {
        *this = *this / v;
    }

    bool operator<(const BI &v) const {
        if (sign != v.sign)
            return sign < v.sign;
        if (a.size() != v.a.size())
            return a.size() * sign < v.a.size() * v.sign;
        for (int i = a.size() - 1; i >= 0; i--)
            if (a[i] != v.a[i])
                return a[i] * sign < v.a[i] * sign;
        return false;
    }
    bool operator>(const BI &v) const {
        return v < *this;
    }
    bool operator<=(const BI &v) const {
        return !(v < *this);
    }
    bool operator>=(const BI &v) const {
        return !(*this < v);
    }
    bool operator==(const BI &v) const {
        return !(*this < v) && !(v < *this);
    }
    bool operator!=(const BI &v) const {
        return *this < v || v < *this;
    }

    void trim() {
        while (!a.empty() && !a.back())
            a.pop_back();
        if (a.empty())
            sign = 1;
    }

    bool isZero() const {
        return a.empty() || (a.size() == 1 && !a[0]);
    }

    BI operator-() const {
        BI res = *this;
        res.sign = -sign;
        return res;
    }

    BI abs() const {
        BI res = *this;
        res.sign *= res.sign;
        return res;
    }

    long long longValue() const {
        long long res = 0;
        for (int i = a.size() - 1; i >= 0; i--)
            res = res * BI_base + a[i];
        return res * sign;
    }

    friend BI gcd(const BI &a, const BI &b) {
        return b.isZero() ? a : gcd(b, a % b);
    }
    friend BI lcm(const BI &a, const BI &b) {
        return a / gcd(a, b) * b;
    }
    void read(const string &s) {
        sign = 1;
        a.clear();
        int pos = 0;
        while (pos < (int) s.size() && (s[pos] == '-' || s[pos] == '+')) {
            if (s[pos] == '-')
                sign = -sign;
            ++pos;
        }
        for (int i = s.size() - 1; i >= pos; i -= BI_digits) {
            int x = 0;
            for (int j = max(pos, i - BI_digits + 1); j <= i; j++)
                x = x * 10 + s[j] - '0';
            a.push_back(x);
        }
        trim();
    }

    friend istream& operator>>(istream &stream, BI &v) {
        string s;
        stream >> s;
        v.read(s);
        return stream;
    }
	friend ostream& operator<<(ostream &stream, const BI &v) {
		if (v.sign == -1)
			stream << '-';
		stream << (v.a.empty() ? 0 : v.a.back());
		for (int i = (int) v.a.size() - 2; i >= 0; --i)
			stream << setw(BI_digits) << setfill('0') << v.a[i];
		return stream;
	}

    static vector<int> convert_base(const vector<int> &a, int old_digits, int new_digits) {
        vector<long long> p(max(old_digits, new_digits) + 1);
        p[0] = 1;
        for (int i = 1; i < (int) p.size(); i++)
            p[i] = p[i - 1] * 10;
        vector<int> res;
        long long cur = 0;
        int cur_digits = 0;
        for (int i = 0; i < (int) a.size(); i++) {
            cur += a[i] * p[cur_digits];
            cur_digits += old_digits;
            while (cur_digits >= new_digits) {
                res.push_back(int(cur % p[new_digits]));
                cur /= p[new_digits];
                cur_digits -= new_digits;
            }
        }
        res.push_back((int) cur);
        while (!res.empty() && !res.back())
            res.pop_back();
        return res;
    }
    static vector<LL> karatsubaMultiply(const vector<LL> &a, const vector<LL> &b) {
        int n = a.size();
        vector<LL> res(n + n);
        if (n <= 32) {
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    res[i + j] += a[i] * b[j];
            return res;
        }

        int k = n >> 1;
        vector<LL> a1(a.begin(), a.begin() + k);
        vector<LL> a2(a.begin() + k, a.end());
        vector<LL> b1(b.begin(), b.begin() + k);
        vector<LL> b2(b.begin() + k, b.end());

        vector<LL> a1b1 = karatsubaMultiply(a1, b1);
        vector<LL> a2b2 = karatsubaMultiply(a2, b2);

        for (int i = 0; i < k; i++)
            a2[i] += a1[i];
        for (int i = 0; i < k; i++)
            b2[i] += b1[i];
        vector<LL> r = karatsubaMultiply(a2, b2);
        for (int i = 0; i < (int) a1b1.size(); i++)
            r[i] -= a1b1[i];
        for (int i = 0; i < (int) a2b2.size(); i++)
            r[i] -= a2b2[i];

        for (int i = 0; i < (int) r.size(); i++)
            res[i + k] += r[i];
        for (int i = 0; i < (int) a1b1.size(); i++)
            res[i] += a1b1[i];
        for (int i = 0; i < (int) a2b2.size(); i++)
            res[i + n] += a2b2[i];
        return res;
    }
    BI operator*(const BI &v) const {
        vector<int> a6 = convert_base(this->a, BI_digits, 6);
        vector<int> b6 = convert_base(v.a, BI_digits, 6);
        vector<LL> a(a6.begin(), a6.end());
        vector<LL> b(b6.begin(), b6.end());
        while (a.size() < b.size())
            a.push_back(0);
        while (b.size() < a.size())
            b.push_back(0);
        while (a.size() & (a.size() - 1))
            a.push_back(0), b.push_back(0);
        vector<LL> c = karatsubaMultiply(a, b);
        BI res;
        res.sign = sign * v.sign;
        for (int i = 0, carry = 0; i < (int) c.size(); i++) {
            long long cur = c[i] + carry;
            res.a.push_back((int) (cur % 1000000));
            carry = (int) (cur / 1000000);
        }
        res.a = convert_base(res.a, 6, BI_digits);
        res.trim();
        return res;
    }
};



LL price(int a, int b, int N){
	int n = b-a;
	return (2*N - n + 1)*1LL*n/2;
}

Answer ans[MAX_T];

void* solve(void *_id){
	int id = *(int*)_id;
	// считывание данных

	//cout<<"ok"<<endl;
	int N, M, mm[1009][3], i, j;
	in>>N>>M;
	for(i=0;i<M;++i) for(j=0;j<3;++j) in>>mm[i][j];

	//cout<<"ok"<<endl;
	// завершение считывания
	sem_post(&sem[id+1]);
	// основное решение

	BI r1=0, r2=0, bi;
	//int tmp_bi;
	vector<pair<int,int> > v;
	for(i=0;i<M;++i){
		v.push_back(make_pair(mm[i][0], -mm[i][2]));
		v.push_back(make_pair(mm[i][1], mm[i][2]));
		bi = price(mm[i][0], mm[i][1], N);
		//tmp_bi = price(mm[i][0], mm[i][1], N);
		//cout<<"bi = "<<bi<<" "<<tmp_bi<<endl;
		r1 += bi * mm[i][2];
		//cout<<bi<<" "<<r1<<endl;
	}
	sort(v.begin(), v.end());

	//cout<<r1<<endl;

	//cout<<v<<endl;

	stack<pair<int,int> > st;
	pair<int,int> p;

	//cout<<"ok"<<endl;
	for(i=0; i<(int)v.size(); ++i){
		if(v[i].second > 0){
			int t = v[i].second;
			//cout<<i<<" "<<t<<endl;
			while(t>0){
				p = st.top();
				st.pop();
				int tmp = min(t, -p.second);
				bi = price(p.first, v[i].first, N);
				r2 += bi * tmp;
				t -= tmp;
				p.second += tmp;
				if(p.second < 0) st.push(p);
				//cout<<"   "<<tmp<<" "<<t<<endl;
			}
		}else{
			st.push(v[i]);
		}
	}

	// окончание решения
	//sem_wait(&sem[id]);
	// вывод данных

	//out<<"Case #"<<id<<": ";

	ans[id].ans = (r1-r2)%MOD;

	cout<<"Write in "<<id<<endl;
	// окончание вывода
	sem_post(&sem[id+1]);
	sem_post(&sem_count);
	pthread_exit(0);
}

void gcj_solve(){
	cout<<"Start solver.\n";
	int T;
	char s[99];
	in>>T;

	sem_init(&sem_count, 0, MAX_Threads);
	sem_init(&sem[1], 0, 2);
	for(int ii=2; ii<=T; ++ii) sem_init(&sem[ii], 0, 0);

	for(int ii=0; ii<T;){
		cout<<"Wait start "<<ii<<" thread.\n";
		sem_wait(&sem[ii+1]);
		sem_wait(&sem_count);
		++ii;
		cout<<"Go "<<ii<<" thread.\n";
		if(pthread_create(&pthread[ii], NULL, solve, &ii) != 0){
			sprintf(s, "Creating the %d thread", ii);
			perror(s);
			return ;
		}
	}
	for(int ii=1; ii<=T; ++ii){
		if(pthread_join(pthread[ii], NULL) != 0){
			sprintf(s, "Joining the %d thread", ii);
			perror(s);
			return ;
		}
	}
	for(int ii=1; ii<=T; ++ii) out<<"Case #"<<ii<<": "<<ans[ii]<<endl;
	cout<<"End solver.\n";
}

int main()
{
	ios_base::sync_with_stdio(0);

	gcj_solve();

	return 0;
}

int cpp4cf_main()
{
	freopen("A.cpp","r",stdin);

	char s[99];
	bool f;

	while(true) {
		cin>>s;
		if(cin.eof()) break;
		if(strstr(s,"/*")) {
			cin>>s;
			if(strstr(s,"Test")) {
				cin>>s;
				if(strstr(s,"on")) {
					cout<<"Output: ";
					cpp4cf_main();
					cout<<"\nAnswer: ";
					f = false;
					while(true) {
						cin>>s;
						if(strstr(s,"*/")) break;
						if(strstr(s,"//")) {
							if(f) cout<<endl;
							else f = true;
						}else cout<<s<<" ";
					}
					cout<<"\n\n";
				}
			}
		}
	}

	return 0;
}


