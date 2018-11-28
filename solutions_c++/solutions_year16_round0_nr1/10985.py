/* In the name of ALLAH, most gracious.
 * You got a dream, you gotta protect it.
 */
#include <bits/stdc++.h>
using namespace std;
#define PI atan(1) * 4
typedef long long ll;
typedef long double ld;

int t;
ll num , x ,i, MAX , q;
set<int> se;

int main() {
	  freopen ("myfile.txt","r",stdin);
	  freopen ("myfile2.txt","w",stdout);
	scanf("%d", &t);
	while (t--) {
		q++;
		scanf("%d", &x);
		if (x==0)
		{
			cout<<"Case #"<<q<<": INSOMNIA"<<endl;
			continue;
		}
		i = x;
		num=x;
		while (i > 0)
			se.insert(i % 10), i /= 10;
		while (se.size() != 10) {
			num += x;
			i=num;
			while (i > 0)
				se.insert(i % 10), i /= 10;
		}
		cout<<"Case #"<<q<<": "<<num<<endl;
		se.clear();
	}

	return 0;
}
