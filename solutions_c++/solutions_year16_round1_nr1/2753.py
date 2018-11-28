#include<bits/stdc++.h>

#define _ ios::sync_with_stdio(false);
#define INF (1 << 30)
#define ll_INF (1ll << 60)
#define ll long long
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define mt make_tuple
#define pii pair<int,int>
#define mem(x,a) memset(x, a, sizeof(x))
#define SWAP(a,b) tie(a,b) = mt(b,a)
#define rep(i, begin, endd) for (__typeof(endd) i = (begin) - ((begin) > (endd)); i != (endd) - ((begin) > (endd)); i += 1 - 2 * ((begin) > (endd)))
inline ll Power(int b, int p) { ll ret = 1; for ( int i = 1; i <= p; i++ ) ret *= b; return ret; }

#define MAX 100005
/*sort(begin(t), end(t), [](pii a, pii b){
	if(a.first < b.first) return true;
	if(a.first == b.first) return(a.second < b.second);
	return false; 
});*/

using namespace std;
struct comp {
    bool operator() (const pii &a, const pii &b) {
        return a.second > b.second;
    }
};
int gcd(int a, int b)
{
	if(b == 0) return a;
	return gcd(b,a%b);
}

int main()
{_
	int T;
	cin>>T;
	for(int t=1; t<=T; t++)
	{
		string s,tmp;
		cin>>s;
		tmp = s[0];
		for(int i=1; i<s.length(); i++)
		{
			if(tmp+s[i]>s[i]+tmp)
				tmp = tmp+s[i];
			else
				tmp = s[i] + tmp;
		}
		cout<<"Case #"<<t<<": "<<tmp<<"\n";
	}	

}