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

char guarda[120];

int main(){
	int t;
	cin >> t;
	int p = 1;
	while(t--){
		int contador=0;
		cin >> guarda;
		int n = strlen(guarda);
		for(int i=n-1;i>=0;i--){
			if(guarda[i]!='+'){
				guarda[i] = '+';
				contador++;
				int j;
				for( j=i-1;j>=1;j--){
					if(guarda[j]=='-'){
						guarda[j]='+';
					} else {
						break;
					}
			    }
				i = j;
				for(int k=i;k>=0;k--){
					guarda[k] == '+'? guarda[k] = '-' : guarda[k] = '+';
				}
				i++;
			}
		}
		cout<<"Case #"<<p<<": "<<contador<<"\n";
		p++;
	}
}