#include <bits/stdc++.h>
#define rep(i,n) for(int i = 0; i < n; i++)
const int    INF = 100000000;
const double EPS = 1e-10;
const int    MOD = 1000000007;
using namespace std;
typedef pair<int,int> P;

int k, n;
vector<double> p;

template < class BidirectionalIterator >
bool next_combination ( BidirectionalIterator first1 ,
  BidirectionalIterator last1 ,
  BidirectionalIterator first2 ,
  BidirectionalIterator last2 )
{
  if (( first1 == last1 ) || ( first2 == last2 )) {
    return false ;
  }
  BidirectionalIterator m1 = last1 ;
  BidirectionalIterator m2 = last2 ; --m2;
  while (--m1 != first1 && !(* m1 < *m2 )){
  }
  bool result = (m1 == first1 ) && !(* first1 < *m2 );
  if (! result ) {
    while ( first2 != m2 && !(* m1 < * first2 )) {
      ++ first2 ;
    }
    first1 = m1;
    std :: iter_swap (first1 , first2 );
    ++ first1 ;
    ++ first2 ;
  }
  if (( first1 != last1 ) && ( first2 != last2 )) {
    m1 = last1 ; m2 = first2 ;
    while (( m1 != first1 ) && (m2 != last2 )) {
      std :: iter_swap (--m1 , m2 );
      ++ m2;
    }
    std :: reverse (first1 , m1 );
    std :: reverse (first1 , last1 );
    std :: reverse (m2 , last2 );
    std :: reverse (first2 , last2 );
  }
  return ! result ;
}
 
template < class BidirectionalIterator >
bool next_combination ( BidirectionalIterator first ,
  BidirectionalIterator middle ,
  BidirectionalIterator last )
{
  return next_combination (first , middle , middle , last );
}

double calc(vector<double> z){
	vector<double> q;
	double ret = 0.0;
	for(int i = 1; i < k; i++) q.push_back(z[i]);
	if(k/2-1 == 0) ret += z[0]*(1-z[1]);
	else{
		do{
			double a = z[0];
			rep(i,k/2-1) a *= q[i];
			for(int i = k/2-1; i < q.size(); i++) a *= (1.0-q[i]);
			ret += a;
		} while(next_combination(q.begin(),q.begin()+k/2-1,q.end()));
	}
	q.clear();
	for(int i = 1; i < k; i++) q.push_back(z[i]);
	do{
		double a = 1.0-z[0];
		rep(i,k/2) a *= q[i];
		for(int i = k/2; i < q.size(); i++) a *= (1.0-q[i]);
		ret += a;
	} while(next_combination(q.begin(),q.begin()+k/2,q.end()));
	return ret;
}

void solve(){
	cin >> n >> k;
	p.clear();
	rep(i,n){
		double tmp;
		cin >> tmp;
		p.push_back(tmp+EPS*i);
	}
	sort(p.begin(),p.end());
	double ans = 0.0;
	do{
		ans = max(ans,calc(p));
    }while(next_combination(p.begin(), p.begin()+k, p.end()));
	printf("%.9f\n", ans);
}

int main(){
	int T;
	cin >> T;
	rep(i,T){
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}