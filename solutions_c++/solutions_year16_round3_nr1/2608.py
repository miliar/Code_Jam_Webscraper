using namespace std;
#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define rite(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define clr clear()
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9
typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
#define mx 0
int main() {
    ios_base::sync_with_stdio(0);

    int t; scanf("%d", &t);

    for (int x = 0; x < t; ++x)
  	{
  		string y = "";
  		int sens; 
  		scanf("%d", &sens);
  		int sen[sens];
  		int sum = 0;
  		rep(i, sens){ 
  			int toins;
  			scanf("%d", &sen[i]);
  			sum +=sen[i];
  		}
  		int et = 0;
  		int suma = sum;
  		for (int i = 0; i < sum; ++i)
  		{
  			int maxi = distance(sen, max_element(sen, sen + sens));
  			y += 'A'+maxi;
  			
  			// printf("%f\n", sen[maxi]*1.0/suma);
  			// printf("%d\n", suma);
  			// printf("%d\n", sen[maxi]);

  			sen[maxi]--;
  			suma--;
  			// maxi = distance(sen, max_element(sen, sen + sens));
  			// if(sen[maxi]!=0 && suma!=0) {
  			// 	 if(sen[maxi]/suma>0.5){
  			// 	 	y += 'A'+maxi;
  			// 		sen[maxi]--;
  			// 		suma--;
  			// 	}
  			// }
  			et++;
  			int nexmaxi = distance(sen, max_element(sen, sen + sens));

  			if (i!=sum-1){
  				//printf("%f\n", (double)sen[nexmaxi]/suma);
  				if((double)sen[nexmaxi]/suma<=0.5){
 
  					y += ' ';
  					et=0;
  				}
  			}
  			
  		}

  		cout << "Case #"<< x+1 << ": ";
  		cout << y << endl;
    }


    return 0;
}