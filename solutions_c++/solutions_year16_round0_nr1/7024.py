#include <bits/stdc++.h>
using namespace std;
#define all(c) c.begin(), c.end()
#define tr(container, it) for(auto it = container.begin(); it != container.end(); it++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp make_pair
#define Foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define rof(i,a,b) for(int (i)=(a);(i) > (b); --(i))
#define rep(i, c) for(auto &(i) : (c))
#define x first
#define y second
#define pb push_back
#define PB pop_back()
#define fastscan ios_base::sync_with_stdio(0);cin.tie(NULL);
int digits[10];

int done() {
	int ret = 1;
	for(int x=0;x<10;x++){
		if(digits[x]==0){
			ret = 0;
			break;
		}
	}
	return ret;
}

void slic(int n){
	while(n>0){
		int d = n%10;
		n=n/10;
		digits[d] = 1;
	}
}

int main() {
	int l;
	cin>>l;
	int i = 1;
	while(l--) {
		for(int x=0;x<10;x++){
			digits[x]=0;
		}
		int n;
		cin>>n;
		int num = n;
		if(n==0){
			cout<<"Case #"<<i<<": INSOMNIA\n";
		}else{
			while(done()!=1){
				slic(n);
				n=n+num;
			}
			cout<<"Case #"<<i<<": "<<n-num<<"\n";
		}
		i++;
	}
}
