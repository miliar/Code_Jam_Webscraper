#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < (n); i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define sqrt(x) sqrt(abs(x))
#define y0 y3487465
#define y1 y8687969
#define fill(x,y) memset(x,y,sizeof(x))
                         
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) { re x > 0 ? x : -x; }

int idxCase;
long long int n;
long long int m[1000001];
int s[50];
//vector<pair<string, int> > w;

int main () {

    freopen ("q1.in", "r", stdin); 
    freopen ("q1.out", "w", stdout);


	for(long long int i=0 ;i<=1000000; i++){
		m[i] = -1;
	}
	m[0]=0;
	for(long long int i=0 ;i<=999999; i++){
		long long int next = i+1;
		if(m[next] == -1){
			m[next] = m[i] + 1;		
		}
		else if( (m[i]+1) < m[next]){
			m[next] = m[i] + 1;
		}

		// reverse
		long long int index = i;
		if((index % 10) != 0){
			next=0; 
			while(index!=0){
				//cout << "aaa original: "<< i <<" reverse: "<< next << "index: "<<index<<endl;
				next *=10;
				next += (index%10);
				index = index / 10;
				//cout << "bbb original: "<< i <<" reverse: "<< next << "index: "<<index<<endl;
			}
			//cout << "ccc original: "<< i <<" reverse: "<< next<<endl;
			if(m[next] == -1){
				m[next] = m[i] + 1;		
			}
			else if( (m[i]+1) < m[next]){
				m[next] = m[i] + 1;
			}
		}
	//	cout <<i<<endl;
	}

	int idxCase;
	cin >> idxCase;
	for (int it = 1; it <= idxCase; it++) {
		cin >> n ;


		//fill in answer
		cout<<"Case #"<<it <<": "<<m[n] <<endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", it, idxCase, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / it * idxCase) / CLOCKS_PER_SEC);
	}
	return 0;
}
