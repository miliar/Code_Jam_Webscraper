#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef vector < long long > vll;
typedef pair < long long, long long > pll;
typedef pair < int, int > pii;
typedef vector < int > vii;
 
#define rep(i,n) for(int i = 0; i < n; i++)
#define reps(i,a,n) for(int i = a; i < n; i++)
#define s(n) cin >> n
#define csl ios_base::sync_with_stdio(false); cin.tie(NULL)

int t,n;
string str;

int Solve(){
	if(n==0)
		return 0;
	else{
		int total=str[0]-'0',result=0;
		reps(i,1,str.size()){
			//cout<<"total="<<total<<"i="<<i<<endl;
			if(total>=i)
				total+=(str[i]-'0');
			else{
				result+=abs(total-i);
				total=i+str[i]-'0';
			}

		}
		return result;
	}
}
int main(){
	csl;
	cin>>t;
	reps(i,1,t+1){
		cin>>n;
		cin>>str;
		cout<<"Case #"<<i<<": "<<Solve()<<endl;
	}
	return 0;
}