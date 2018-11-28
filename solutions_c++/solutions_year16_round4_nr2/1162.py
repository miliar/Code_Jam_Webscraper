#include <bits/stdc++.h>
using namespace std;

#define f(i,a)  for(int i=0;(i)<(a);++i)
#define fab(i,a,b) for (int i = (a); (i) < (b); ++i)
#define fba(i,a,b) for (int i = (b) - 1; (i) >= (a); --i)
#define fit(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(),(c).end()
#define pb push_back
#define MOD 1000000007

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
typedef char u8;
typedef vector <int> vi;
typedef pair <int, int> pii;

template <typename Iterator>
inline bool next_combination(const Iterator first, Iterator k, const Iterator last)
{
   /* Credits: Thomas Draper */
   if ((first == last) || (first == k) || (last == k))
      return false;
   Iterator itr1 = first;
   Iterator itr2 = last;
   ++itr1;
   if (last == itr1)
      return false;
   itr1 = last;
   --itr1;
   itr1 = k;
   --itr2;
   while (first != itr1)
   {
      if (*--itr1 < *itr2)
      {
         Iterator j = k;
         while (!(*itr1 < *j)) ++j;
         std::iter_swap(itr1,j);
         ++itr1;
         ++j;
         itr2 = k;
         std::rotate(itr1,j,last);
         while (last != j)
         {
            ++j;
            ++itr2;
         }
         std::rotate(k,itr2,last);
         return true;
      }
   }
   std::rotate(first,k,last);
   return false;
}

ll pw(ll b,int p, int m){
    ll a=1;
    while(p){
        if(p&1)
            a=(a*b)%m;
        b=(b*b)%m;
        p>>=1;
    }
    return a;
}

ll gcd(ll a, ll b){
    if(a<b)
        swap(a,b);
    if(!b)
        return a;
    return gcd(b,a%b);
}
bool grater_comp (pair<int,char> i,pair<int,char> j) { return (i.first>j.first); }
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int T,n,k,zs,x;
	vi A,B;
	double a,max,total,p,to;
	std::vector<double> P,X;
    cin>>T;
    f(t,T){
        cout<<"Case #"<<t+1<<": ";
		cin>>n>>k;
		max=to=0;
		total=1;
		P.clear();
		f(i,n){
			cin>>a;
			total*=a;
			P.pb(a);
		}
	//	cout<<total<<"\n";
		A.clear();
		f(i,n)
			A.pb(i);
		do {
			X.clear();
			B.clear();
			f(i,k){
				X.pb(P[A[i]]);
	//			cout<<P[A[i]]<<" ";
				B.pb(i);
			}
			x=k/2;
	//		cout<<endl;
			to=0;
			do {
				p=1;
				f(i,k/2)
					p=(p-p*X[B[i]]);
				fab(i,k/2,k)
					p=p*X[B[i]];
				to+=p;
	//			cout<<p<<" ";
			} while(next_combination(B.begin(),B.begin()+x,B.end()));
	//		cout<<to<<"\n";
			if(max<to)
				max=to;
		} while(next_combination(A.begin(),A.begin()+k,A.end()));
        cout<<setprecision(7)<<max<<"\n";
    }
    return 0;
}

