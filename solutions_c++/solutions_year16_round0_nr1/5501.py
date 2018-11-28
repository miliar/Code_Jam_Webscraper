#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define SZ(x) ((int)(x).size())
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define max(a,b) ( (a) > (b) ? (a) : (b))
#define min(a,b) ( (a) < (b) ? (a) : (b))
#define abs(x) (x<0?(-x):x)
#define ll long long
#define ull unsigned long long
#define ui unsigned int
#define us unsigned short
#define pi 3.1415926535897932384626
#define pb push_back
#define mp make_pair
#define ms(s, n) memset(s, n, sizeof(s))
#define all(a) a.begin(), a.end()
#define dist(xa,ya,xb,yb) sqrt(((xa) -(xb))*((xa) -(xb)) + ((ya)- (yb))*((ya)- (yb)))

using namespace std;
 
bool verifica[11];

int main()
{
	int n , asd;
	long long in;
	cin >> n;
	for(int a=1;a<=n;a++){
		cin >> in;
		if(in==0){
			cout << "Case #" << a << ": INSOMNIA" << endl;
		}else{
			memset(verifica,false, sizeof(verifica));
			int k=10;
			ll m=0;
			while(k != 0){
				m++;
				ll asd = m*in;
				while(asd!=0){
					if(verifica[asd%10] == false){
						k--;
						verifica[asd%10] = true;
					}
					asd /= 10;
				}
			}
			cout << "Case #"<< a << ": " << m*in << endl;
		}
	}
}