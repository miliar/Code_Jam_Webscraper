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
	freopen("C-small-attempt3.in","r",stdin);
	freopen("myfile.txt","w",stdout);
	int t,l,x,ans;
	string str;
	string arr[] = {"NO","YES"};
	string table[][3] = {
			{"-1","k","-j"},
			{"-k","-1","i"},
			{"j","-i","-1"},
			{"-i","-j","-k"},
			{"i","j","k"},
			{"","-k","j"},
			{"k","","-i"},
			{"-j","i",""},
	};
	map<string,int> maps;
	maps["i"] = 0;
	maps["j"] = 1;
	maps["k"] = 2;
	maps["-1"] = 3;
	maps[""] = 4;
	maps["-i"] = 5;
	maps["-j"] = 6;
	maps["-k"] = 7;
	cin>>t;
	For(i,0,t){
		cin>>l>>x>>str;
		string cur = "";
		string ss = "";
		ans = 0;
		bool fi = false,fj = false;
		For(j,0,x){
			For(k,0,str.size()){
				ss = "";
				ss += str[k];
				cur = table[maps[cur]][maps[ss]];
				if(cur == "i")
					fi = true;
				if(fi && cur == "k")
					fj = true;
			}
		}
		if(fi && fj && cur == "-1")
			ans = 1;
		cout<<"Case #"<<i+1<<": "<<arr[ans]<<endl;
	}
	return 0;
}
/**/
