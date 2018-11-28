#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility> //Pair
#include <algorithm>
#include <sstream> // istringstream>> ostring stream<<
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>
using namespace std;
 
typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
typedef istringstream iss;
typedef ostringstream oss;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n) for(int i=0;i<n;i++)
#define fu(i,a,n) for(int i=a;i<=n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define all(a) a.begin(),a.end()
#define ESP (1e-9)

int main(){
	freopen("A-large.in","r",stdin);
	freopen("outputlarge.txt","w",stdout);
	int tt,smax,i,perstand,ans,j=0;
	string aud;
	cin >> tt;
	while(tt--){
		cin >> smax;
		//int nonzeroindex[smax+1];
		//memset(nonzeroindex,0,sizeof(nonzeroindex));
		cin >> aud;
		ans =0;
		perstand = 0;
		for(i=0;i<smax+1;i++){
			if(aud[i]-48 > 0){
				if(perstand >= i){
					perstand += (aud[i] - 48);
					//cout << perstand << endl;
				}
				else{
				    //cout << "ya" << endl;
					ans += (i - perstand);
					perstand += (i - perstand + aud[i] - 48 );
				}
			}
		}
		j++;
		cout << "Case #" << j<< ": "<< ans << endl;
	}
	return 0;
}