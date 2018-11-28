#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <algorithm>


using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
typedef stack<long long> ss;
#define get(a) #a
//#define DEBUG
#ifdef DEBUG

     #define debug(args...)            {dbg,args; cerr<<endl;}

#else

    #define debug(args...)              // Just strip off all debug tokens

#endif


struct debugger

{

    template<typename T> debugger& operator , (const T& v)

    {

        cerr<<v<<" ";

        return *this;

    }

} dbg;

int main(){
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;

	int count = 1;
	while(t--){
		int s;
		cin>>s;

		string str;
		cin>>str;

		int sum = str[0] - '0';
		//cout<<"sum = "<<sum<<endl;
		int ans = 0;
		for(int i = 1;i < str.length();i++){
			if(sum < i){
				if(str[i] != '0'){
					ans += i - sum;
					//cout<<"ans = "<<ans<<endl;
					sum += ans;
				}
			}
			sum = sum + (int)(str[i] - '0');
			//cout<<"sum = "<<sum<<endl;
		}

		cout<<"Case #"<<count<<": "<<ans<<endl;
		count++;
	}
}
