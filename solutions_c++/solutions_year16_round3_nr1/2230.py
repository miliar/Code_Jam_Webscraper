#include <bits/stdc++.h>
using namespace std;

#define fr(a, n) for(a = 0; a < n; a++)
#define fr1(a, n) for(a = 1; a <= n; a++)
#define frR(a, n) for (a = n; a >= 0; a--)
#define sc(a) scanf("%d", &a)
#define pr(a) printf("%d\n", a)
#define p(i, j) make_pair(i, j)
#define fi first
#define se second

typedef pair<int, int> ii;
typedef pair<double, double> dd;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long int ll;
typedef unsigned long long int ull;

struct cmpStruct {
  bool operator() (pair<int, char> const & lhs, pair<int,char> const & rhs) const
  {
    return lhs > rhs;
  }
};

int main(){
	int n, i, j, t, aux, total;
	vector< pair<int,char> > s;
	vector<pair<int,char> >::iterator it;
	pair<int, char> a, b;
	char auxChar;
	bool first;
	sc(t);
	
	fr1(i,t){
		sc(n);
		s.clear();
		auxChar= 'A';
		total = 0;
		fr(j,n){
			sc(aux);
			total += aux;
			s.push_back(make_pair(aux, auxChar));
			auxChar++;
		}
		sort(s.begin(), s.end(), greater<pair<int, char> >());
		printf("Case #%d:", i);
		while(total > 0){
			if(s.size() == 1){
				it = s.begin();
				printf(" %c", it->se);
				it->fi--;
				if(it->fi == 0) s.erase(it);
				total--;
			}
			else{
				it = s.begin();
				a = *it;
				it++;
				b = *it;
				if(b.fi > (total-1)/2){
					it = s.begin();
					printf(" %c%c", a.se, b.se);
					a.fi--;
					b.fi--;
					if(a.fi == 0){
						s.erase(s.begin());
						if(b.fi == 0){
							s.erase(s.begin());
						}
					}
					total -= 2;
				}
				else{
					it = s.begin();
					printf(" %c", it->se);
					it->fi--;
					total --;
					if(it->fi == 0)s.erase(it);
				}
			}
			sort(s.begin(), s.end(), greater<pair<int, char> >());
		}
		printf("\n");
		
		
	}

	return 0;
}
