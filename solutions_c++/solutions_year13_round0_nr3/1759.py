/* ***************************
Author: Abhay Mangal (abhay26)
*************************** */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
 #define tr(container, it) \
	for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define maX(a,b) (a) > (b) ? (a) : (b)
#define pii pair< int, int >
#define pip pair< int, pii >
#define FOR(i,n) for(int i=0; i<(int)n ;i++)
#define pb push_back
//int dx[]= {-1,0,1,0};
//int dy[]= {0,1,0,-1};
class BigInt {
	public:
	string n;
	BigInt(string num = "0"){
		n = num;
		reverse(n.begin(), n.end());
	}
	BigInt(long long num){
		n = num ? "" : "0";
		while(num) n += num % 10 + '0', num /= 10;
	}
	BigInt operator +(BigInt b){
		BigInt r;
		r.n = n;
		int c, i, l1 = r.n.size(), l2 = b.n.size();
		for(i = l1; i < l2; ++i) r.n += '0';
		for(i = l2; i < l1; ++i) b.n += '0';
		for(c = i = 0; i < l1 || i < l2; ++i){
			r.n[i] = ((c = r.n[i] - '0' + b.n[i] - '0' + c) % 10) + '0';
			c /= 10;
		}
		if(c) r.n += c + '0', ++i;
		b.n = b.n.substr(0, l2);
		return r;
	}
	BigInt operator +=(BigInt b){
		return *this = *this + b;
	}
	BigInt operator +(long long a){
		return *this + BigInt(a);
	}
	BigInt operator +=(long long a){
		return *this = *this + BigInt(a);
	}
	BigInt operator -(BigInt b){
		BigInt r;
		if(*this == b) return BigInt("0");
		assert(*this >= b);
		int i, l1 = n.size(), l2 = b.n.size();
		for(i = 0; i < l2; ++i) b.n[i] = '9' - b.n[i] + '0';
		for(i = l2; i < l1; ++i) b.n += '9';
		r = *this + b;
		l1 = r.n.size();
		r.n[l1 - 1]--;
		r += 1;
		r.trim();
		for(i = 0; i < l2; ++i) b.n[i] = '9' - b.n[i] + '0';
		b.n = b.n.substr(0, l2);
		return r;
	}
	BigInt operator -=(BigInt b){
		return *this = *this - b;
	}
	BigInt operator -(long long a){
		return *this - BigInt(a);
	}
	BigInt operator -=(long long a){
		return *this = *this - BigInt(a);
	}
	BigInt operator *(BigInt b){
		BigInt r, s;
		int c, i, j, l1 = n.size(), l2 = b.n.size();
		for(i = 0; i < l1; ++i){
			s.n = string(i, '0');
			for(c = j = 0; j < l2; ++j){
				s.n += (c = (n[i] - '0') * (b.n[j] - '0') + c) % 10 + '0';
				c /= 10;
			}
			while(c) s.n += ((c % 10) + '0'), c /= 10;
			r = r + s;
		}
		r.trim();
		return r;
	}
	BigInt operator *=(BigInt b){
		return *this = *this * b;
	}
	BigInt operator *(long long a){
		return *this * BigInt(a);
	}
	BigInt operator *=(long long a){
		return *this = *this * BigInt(a);
	}
	BigInt operator >>(int x){
		BigInt r = *this;
		reverse(r.n.begin(), r.n.end());
		for(int i = 0; i < x; ++i){
			string result = "";
			int d = 0, sz = r.n.size();
			for(int i = 0; i < sz; ++i){
				d = d * 10 + r.n[i] - '0';
				result += (d >> 1) + '0';
				d &= 1;
			}
			r.n = result;
		}
		reverse(r.n.begin(), r.n.end());
		r.trim();
		return r;
	}
	BigInt sqroot(){
		string num = n; int l = n.size();
		reverse(num.begin(), num.end());
		BigInt r, rem, x(num.substr(0, 2 - (l & 1)));
		int f = l & 1 ? x.n[0] - '0' : 10 * (x.n[1] - '0') + (x.n[0] - '0');
		f = (int)sqrt(f);
		r = BigInt(f);
		rem = x - f * f;
		for(int i = 2 - (l & 1), d; i < l; i += 2){
			BigInt down = r * 20;
			rem = rem * 100 + num.substr(i, 2);
			rem.trim();
			for(d = 1; d < 10 && ((down + d) * d) <= rem; ++d);
			r.n = (char)(--d + '0') + r.n;
			rem = rem - (down + d) * d;
		}
		return r;
	}
	bool operator ==(BigInt b){
		return mycmp(b) == 0;
	}
	bool operator !=(BigInt b){
		return mycmp(b) != 0;
	}
	bool operator >(BigInt b){
		return mycmp(b) > 0;
	}
	bool operator >=(BigInt b){
		return mycmp(b) >= 0;
	}
	bool operator <(BigInt b){
		return mycmp(b) < 0;
	}
	bool operator <=(BigInt b){
		return mycmp(b) <= 0;
	}
	bool operator ==(long long a){
		return *this == BigInt(a);
	}
	bool operator !=(long long a){
		return *this != BigInt(a);
	}
	bool operator >(long long a){
		return *this > BigInt(a);
	}
	bool operator >=(long long a){
		return *this >= BigInt(a);
	}
	bool operator <(long long a){
		return *this < BigInt(a);
	}
	bool operator <=(long long a){
		return *this <= BigInt(a);
	}
	void trim(){
		int i; for(i = n.size(); --i && n[i] == '0'; )
		n = n.substr(0, i);
	}
	int mycmp(BigInt b){
		int i, l1 = n.size(), l2 = b.n.size();
		if(l1 != l2) return (l1 > l2) - (l1 < l2);
		for(i = l1; i-- && n[i] == b.n[i]; );
		if(i == -1) return 0;
		return (n[i] > b.n[i]) - (n[i] < b.n[i]);
	}
	void show(){
		printf("%s\n", to_string().c_str());
	}
	string to_string(){
		string s = n;
		reverse(s.begin(), s.end());
		return s;
	}
	bool ispalin(){
	string s = n;
	reverse(s.begin(), s.end());
	if(s == n)
	return true;
	return false;
	}
};
BigInt s,maxstr,prod;
vector<BigInt> V;
string str2,a,b;
char str[1000000];
void makepal(int len, int odd)
{
	int j, i = len-1, k = odd? len-1 : len, carry = 1, a;
	for(; i>=0 || carry; i--, k++)
	{
		a = (i>=0)? str[i] - '0' : 0;
		str[k] = (a + carry) % 10 + '0';
		carry = (a + carry) / 10;
	}
	str[k] = 0;
	for(i=0, j=k-1; i < j; i++, j--) str[i] = str[j];
}
void calc()
{
    int len, odd, mid, i, j, flag;
    while(1)
    {
        str2 = s.to_string();
        len = str2.length();
        for(i=0;i<len;i++)
            str[i] = str2[i];
        str[i] = '\0';
		mid = (len + 1) / 2;
		odd = (len & 1) ? 1 : 0;
		i = mid-1, j = mid, flag = 0;
		for(i=odd?i-1:i; i>=0 && j<len; i--, j++)
		{
			if(str[i] > str[j]) { str[j] = str[i]; flag = 1; }
			else if(str[i]==str[j]) str[j] = str[i];
			else break;
		}
		if(! flag) makepal(mid, odd);
		str2 = str;
		//cout << str2 << endl;
        s = str2;
        prod = s;
        prod = prod * s;
        if(prod > maxstr) break;
        if(prod.ispalin())
        {
            string ans = prod.to_string();
            V.pb(prod);
            //cout << ans << endl;
        }
    }
}
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("out.txt","w",stdout);
    string lol = "1";
    s = lol;
    string maxs;
    maxs = "1000000000000000";
    maxstr = maxs;
    V.pb(s);
    calc();
	int t;
	scanf("%d",&t);
	BigInt low,high;
	int cas=0;
	while(t--)
	{
        cin >> a >> b;
        cas++;
        low = a;
        high = b;
        int cnt = 0;
        for(int i=0;i<V.size();i++)
        {
            if(V[i] > b) break;
            if(V[i] >= a && V[i] <= b)
            cnt++;
        }
        printf("Case #%d: %d\n",cas,cnt);
	}
return 0;
}
