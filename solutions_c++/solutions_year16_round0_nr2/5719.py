/* My First Template  
   :P
*/
#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define ll long long int
#define pb push_back
#define mk make_pair
ll power(ll a, ll b) {
ll x = 1, y = a;
    while(b > 0) {
        if(b%2 == 1) {
            x=(x*y);
            if(x>mod) x%=mod;
        }
        y = (y*y);
        if(y>mod) y%=mod;
        b /= 2;
    }
    return x;
}
string str;
bool rev(int idx)
{
	int i;
	bool flag = false;
	for(i = 0; i < idx; i++) {
		flag = true;
		str[i] = (str[i]=='+')?'-':'+';
	}
	reverse(str.begin(),str.begin()+idx);
	return flag;
}
int main()
{
	freopen("input2.in","r",stdin);
	freopen("output2.txt","w",stdout);
	int t;
	int tc = 1;
	cin>>t;
	while(t--) {
        cin>>str;
        int i,res;
        res = 0;
        while(1) {
        	bool flag = true;
        	for(i = 0; str[i]; i++) {
        		if(str[i] == '-') {
        			flag = false;
        			break;
        		}
        	}
        	if(flag) break;
        	for(i = 0; str[i]; i++) {
        		if(str[i] == '-') {
        			break;
        		}
        	}
        	res += rev(i);
        	for(i = str.size()-1; i >= 0; i--) {
        		if(str[i] == '-') {
        			break;
        		}
        	}
        	res += rev(i+1);
        }
        cout<<"Case #"<<tc<<": "<<res<<endl;
        tc++;
    }
	return 0;
}
