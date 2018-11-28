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
	freopen("D-small-attempt4.in","r",stdin);
	freopen("myfile.txt","w",stdout);
	int t,ans;
	string arr[] = {"RICHARD","GABRIEL"};
	cin>>t;
	For(i,0,t){
		int x,r,c;
		cin>>x>>r>>c;
		if(x == 1)
			ans = 1;
		else if(x == 2){
			if(r%2 && c%2)
				ans = 0;
			else
				ans = 1;
		}else if(x == 4){
			if(c+r >= 7)
				ans = 1;
			else
				ans = 0;
		}else{
			if((r == 3 || c == 3) && min(r,c) > 1)
				ans = 1;
			else
				ans = 0;
		}
		cout<<"Case #"<<i+1<<": "<<arr[ans]<<endl;
	}
	return 0;
}
/**/
