/* Vipul Jain */

#include <bits/stdc++.h>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<double,double>
#define pb(x) push_back(x)
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FB(i,a,n) for(int i=(a);i>=(n);--i)
#define FI(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define Su(x) scanf("%llu",&x)
#define Sf(x) scanf("%f",&x)
#define Sd(x) scanf("%lf",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
#define fi first
#define se second

int main()
{
	int t;
    int j, k;
    S(t);
    F(i, 1, t + 1) {
        
        string s;
        cin >> s;
        int alpha[30];
        M(alpha, 0);
		F(j, 0, s.size()) {
			alpha[s[j] - 'A']++;
		} 

		int num[10];
		M(num, 0);
		if (alpha['Z' - 'A'] != 0) {
			num[0] = alpha['Z' - 'A'];
			
			alpha['E' - 'A'] -= alpha['Z' - 'A'];
			alpha['R' - 'A'] -= alpha['Z' - 'A'];
			alpha['O' - 'A'] -= alpha['Z' - 'A'];
			alpha['Z' - 'A'] = 0;
		} 

		if (alpha['G' - 'A'] != 0) {
			num[8] = alpha['G' - 'A'];
			
			alpha['E' - 'A'] -= alpha['G' - 'A'];
			alpha['I' - 'A'] -= alpha['G' - 'A'];
			alpha['H' - 'A'] -= alpha['G' - 'A'];
			alpha['T' - 'A'] -= alpha['G' - 'A'];
			alpha['G' - 'A'] = 0;
		}  

		if (alpha['X' - 'A'] != 0) {
			num[6] = alpha['X' - 'A'];
			alpha['S' - 'A'] -= alpha['X' - 'A'];
			alpha['I' - 'A'] -= alpha['X' - 'A'];	
			alpha['X' - 'A'] = 0;
	
		} 


		if (alpha['W' - 'A'] != 0) {
			num[2] = alpha['W' - 'A'];
			alpha['T' - 'A'] -= alpha['W' - 'A'];
			alpha['O' - 'A'] -= alpha['W' - 'A'];
			alpha['W' - 'A'] = 0;

		} 

		if (alpha['S' - 'A'] != 0) {
			num[7] = alpha['S' - 'A'];
			alpha['E' - 'A'] -= alpha['S' - 'A'];
			alpha['V' - 'A'] -= alpha['S' - 'A'];
			alpha['E' - 'A'] -= alpha['S' - 'A'];
			alpha['N' - 'A'] -= alpha['S' - 'A'];
						alpha['S' - 'A'] = 0;

		} 


		if (alpha['U' - 'A'] != 0) {
			num[4] = alpha['U' - 'A'];
			alpha['F' - 'A'] -= alpha['U' - 'A'];
			alpha['O' - 'A'] -= alpha['U' - 'A'];
			alpha['R' - 'A'] -= alpha['U' - 'A'];
			alpha['U' - 'A'] -= alpha['U' - 'A'];
		}


		if (alpha['F' - 'A'] != 0) {
			num[5] = alpha['F' - 'A'];
			alpha['I' - 'A'] -= alpha['F' - 'A'];
			alpha['V' - 'A'] -= alpha['F' - 'A'];
			alpha['E' - 'A'] -= alpha['F' - 'A'];
			alpha['F' - 'A'] -= alpha['F' - 'A'];
		}		

		if (alpha['O' - 'A'] != 0) {
			num[1] = alpha['O' - 'A'];
			alpha['N' - 'A'] -= alpha['O' - 'A'];
			alpha['E' - 'A'] -= alpha['O' - 'A'];
			alpha['O' - 'A'] -= alpha['O' - 'A'];
		}	

		if (alpha['I' - 'A'] != 0) {
			num[9] = alpha['I' - 'A'];
			alpha['N' - 'A'] -= alpha['I' - 'A'];
			alpha['E' - 'A'] -= alpha['I' - 'A'];
			alpha['N' - 'A'] -= alpha['I' - 'A'];
			alpha['I' - 'A'] -= alpha['I' - 'A'];
		}

		num[3] = alpha['T' - 'A'];

		string ans = "";
		F(j, 0, 10) {
			F(k, 0, num[j]) {
				ans += j + '0';
			}
		}

		cout << "Case #" << i << ": ";
		cout << ans << endl;
	}

	return 0;

}