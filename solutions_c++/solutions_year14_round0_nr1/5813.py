#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <climits>
#include <cstdio>
#include <set>
using namespace std;
#define db(a) (cout << (#a) << " = " << (a) << endl)
typedef long long ll;

int main()
{
  int T;
  cin>>T;
  for(int t=0;t<T;t++)
  {
	cout << "Case #" << t+1 << ": ";
	int a,b;
	int A[16];
	int B[16];
	cin>>a; a--;
	for(int i=0;i<16;i++) cin>>A[i];
	cin>>b; b--;
	for(int i=0;i<16;i++) cin>>B[i];
	int erg = 0;
	int erg_v = 0;
	for(int j=0;j<4;j++) for(int i=0;i<4;i++) if(A[i + a*4] == B[j + b*4]) {erg_v = A[i+a*4]; erg++;}
	if(erg <= 0) cout << "Volunteer cheated!\n";
	else if(erg == 1) cout << erg_v << "\n";
	else if(erg > 1) cout << "Bad magician!\n";
  }
  return 0;
}