#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue>
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 

using namespace std; 

typedef long long ll; 
typedef pair<int, int> pii;

#define MOD 1000000007
#define INF 1000000000
#define pb push_back 
#define sz size() 
#define mp make_pair

int main()
{
 
 int t, s, p, invites;
 string audience;
 
 cin >> t;
 
 for (int i = 0; i < t; i++) {
	cin >> s >> audience;
	p = invites = 0;
	for (int j = 0; j < audience.sz; j++) {
		if (p < j && audience[j] != '0') {
			invites += (j-p);
			p += invites;
		}
		p += audience[j]-'0';
	}
	cout << "Case #" << i+1 << ": " << invites << endl; 
 }
 
 return 0;
}
