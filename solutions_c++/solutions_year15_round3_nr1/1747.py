#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 
#include <fstream>
using namespace std;
const double eps=1e-8;
const int maxn=100005;
typedef long long ll;
typedef pair<int,int> pii;

int main() {
	int t;
	int r,c,w;
	int kase=1;
	ifstream cin("input.in");
	ofstream cout("output.out");
	cin>>t;
	while(t--) {
		cin>>r>>c>>w;
		int tot=r*c/w;
		if(r*c%w) tot++;
		if(tot) tot-=1;
		tot+=w;
		cout<<"Case #"<<kase++<<": ";
		cout<<tot<<endl;
	}


	return 0;
}
