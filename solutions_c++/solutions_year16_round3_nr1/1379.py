#include<bits/stdc++.h>
using namespace std;
#define w(t) while(t--)
#define ll long long
#define S(x) scanf("%d",&x)
#define SLL(x) scanf("%lld",&x)
#define P(x) printf("%d\n",x)
#define fl(i , a, b) for(i = (int)a; i<(int)b; i++)
#define mem(a , value) memset(a , value , sizeof(a))
#define tr(c, itr) for(itr = (c).begin(); itr != (c).end(); itr++)
string convertstring(ll n) { stringstream ss; ss << n ; return ss.str(); }
#define MOD 1000000007
#define MAX 1000000010
#define all(v) v.begin(),v.end()
#define mp make_pair
#define pb push_back
#define f first
#define s second
typedef pair<int,int> pp;
int a[1234567];
std::vector<pair < int , char > > v;
int main()
{
//	   freopen("C:\\Users\\screw_1011\\Desktop\\input.txt","r",stdin);
//	    freopen("C:\\Users\\screw_1011\\Desktop\\output.txt","w",stdout);
	int t , i , n ,tt;
	cin >> t;
	fl(tt , 1, t+1)
	{
		v.clear(); 
		printf("Case #%d: ", tt);
		cin >> n ;
		fl(i , 0 , n ){
			cin >> a[i]; 
			v.pb( mp( a[i] , char(i + 65) ) ) ; 
		}
		sort(all(v)); 
		while(v.size() > 0 )
		{
			if(v.size() == 2)
			{
				if(v[0].f == v[1].f )
				{
					cout << v[0].s << v[1].s <<" "; 
					v[0].f--;
					v[1].f--;
				}
				while(v.back().f == 0 ) v.pop_back(); 
			}
			else
			{
				cout << v.back().s << " "; 
				v.back().f--;
				while(v.back().f == 0 ) v.pop_back(); 
			}
			sort(all(v));
		}
		cout << endl;
	}
	return 0 ;
}