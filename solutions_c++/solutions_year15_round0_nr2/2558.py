/**/
#include<bits/stdc++.h>
using namespace std;

#define pb push_back
#define For(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define all(v) v.begin(),v.end()
#define V vector
typedef long long ll;
/***********************************************/
/* Dear GCC compiler:
 * I've wasted time reading the problem and trying to figure out the solution
 * If there's any syntax error and you've any suggestion, please fix it yourself.
 * I hope my code compile and get accepted. KEE O.o
 *      ____________
 *     /         __ \
 *    /   __    |  | \
 *   /   |__|   |  |  \
 *  (           |__|   )
 *   \                /
 *    \      ___     /
 *     \____________/
 */
const ll mod = 1000000007;
V<int> a;
int ans;
void bt(int sum){
	int cur = INT_MAX;
	For(i,a.size(),1){
		if(a[i] > 0){
			cur = i;
			break;
		}
	}
	ans = min(ans,sum+cur);
	if(cur <= 3)
		return;
	For(j,2,cur/2+1){
		int d = a[cur];
		a[cur] = 0;
		a[cur - j] += d;
		a[j] += d;
		bt(sum+d);
		a[cur] = d;
		a[cur - j] -= d;
		a[j] -= d;
	}
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	freopen("B-small-attempt11.in","r",stdin);
	freopen("myfile.txt","w",stdout);
	int t,d,cur;
	cin>>t;
	For(i,0,t){
		cin>>d;
		a = V<int>(10,0);
		ans = 0;
		For(i,0,d){
			cin>>cur;
			ans = max(ans,cur);
			a[cur]++;
		}
		bt(0);
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
/**/
