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
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,sm;
	string str;
	cin>>t;
	For(i,0,t){
		cin>>sm>>str;
		int res = 0;
		int cur = 0;
		For(j,0,str.size()){
			if(j > cur){
				res += j - cur;
				cur = j;
			}
			cur += str[j] - '0';
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}
/**/
