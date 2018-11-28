#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
typedef long long LL;

//*******************
//*******************
int cas = 1;
int u = 1;
void read() {
	set<long long> s;
	long long a; 
	cin>>a;
	if(a==0)
			{cout<<"Case #"<<cas<<": INSOMNIA"<<endl; return;}

	// a = u++;
	long long b = 0;
	while(s.size()!=10)
	{
		b+=a;
		long c = b;
		while(c!=0)
		{
			s.insert(c%10);
			c/=10;
		}
	}
	cout<<"Case #"<<cas<<": "<<b<<endl;
}

void solve() {
}

void clean() {
}

int main() {
  ios::sync_with_stdio(false);
  int z;
  cin >> z;

  for(;cas<=z; cas++) {
     read();
     solve();
     clean();
  }
  return 0;
}