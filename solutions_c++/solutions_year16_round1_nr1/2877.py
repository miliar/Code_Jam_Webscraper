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
int main()
{
	   // freopen("C:\\Users\\screw_1011\\Desktop\\input.txt","r",stdin);
	    // freopen("C:\\Users\\screw_1011\\Desktop\\output.txt","w",stdout);
	int t, i ,n ;
	cin >> t;

	for(int tt=1;tt<=t;tt++)
	{
		std::vector<char> fr,back;
		printf("Case #%d: ",tt );
		string s;
		cin >> s;
		n = s.size();
		char ch ; 
		fr.pb(s[0]); 
		fl(i , 0, n)
		{
			if(i == 0) ch = s[i]; 
			else
			{
				if(s[i] >= ch){
					fr.pb(s[i]); 
					ch = s[i]; 
				}
				else{
					back.pb(s[i]);
				}

			}
		}
		// cout << back.size()<<endl;
		while(fr.size() > 0){
			cout << fr.back();
			fr.pop_back(); }
			fl(i,0,back.size()) cout <<back[i];
		cout << endl;
	}
	return 0 ;
}