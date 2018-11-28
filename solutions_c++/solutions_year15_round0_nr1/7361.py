#include <bits/stdc++.h>
using namespace std;
#define repeat(x) for(int fl = 0;fl <x; fl ++)
#define repeat2(x) for(int fl2=0;fl2<x;fl2++)
#define repeat3(x) for (int fl3 = 0;fl3<x ;fl3 ++)
#define rep(a, b) for (int r = int(a); r <= int(b); r++)
#define pb push_back
#define mk make_pair
typedef long long ll;
typedef unsigned int ui;
typedef vector<int> vi;
typedef pair<int, int> ii;
#define inf 2147483647
#define minf -2147483648
#define mil 1000000



int main(){ios_base::sync_with_stdio(false);
int T;cin>>T;int ca=0;
while(T--){ca++;
	int n;cin>>n;
	string s;cin>>s;
	long long int t=0,sum=0;
	repeat(s.size()){
		// cout<<sum<<endl;
		if(sum >= fl){
			sum+=(s[fl]-'0');
		}
		else {
			t += (fl-sum);
			sum = fl + (s[fl]-'0');
		}
	}
	cout<< "Case #"<<ca<<": "<<t<<endl;
}
return 0;
}
