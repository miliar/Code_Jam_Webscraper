#include<iostream>

using namespace std;

int n,k,m,q,x,ans;
string s;
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);	
	cin>>n;
	for (int i = 0;i < n;i++) {
		cin>>m>>s;
		k = s[0] - 48;
		ans = 0;
		q = 0;
		while (k < m) {
			x = 0;
			for (int j = q + 1;j <= k;j++)
				x = x + (s[j] - 48);
			if (x == 0) {
				for (int j = k;j <= m;j++)
					if (s[j] != '0') {
						ans = ans + j - k;
						q = k;
						k = j;
						break;
					}
			} else {
				q = k;
				k = k + x;
			}
//			cout<<q<<" "<<k<<" "<<x<<endl;
		}
		cout<<"Case #"<<i + 1<<": "<<ans<<endl;
	}		
	return 0;
}


//1 3 2
//3 4 1
//4 5 1
