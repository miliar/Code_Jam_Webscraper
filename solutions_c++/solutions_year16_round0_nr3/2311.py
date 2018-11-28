#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define D(x) cout << #x << " = " << (x) << endl;
#define all(x) (x).begin(),(x).end()
int n,k;
string act = "";

long long check(int base){
	long long r = 0;
	for(int i=0;i<n;i++){
		r = r * base + act[i] - '0';
	}
	for(long long i = 2; i*i <= r ; i++){
		if(r%i==0)
			return i;
	}
	return -1;
}

bool check(){
	vector<long long> p;
	for(int b = 2 ; b <= 10 ; b++){
		long long c = check(b);
		if(c==-1)
			return false;
		p.push_back(c);
	}
	cout << act;
	for(int i=0;i<(int)p.size();i++)
		cout << " " << p[i];
	cout << endl;
	return true;
}

void fun(int i){
	if(k<=0) return;
	if(i==n){
		if(check()) k--;
		return;
	}
	if(i!=0 && i!=n-1){
		act += '0';
		fun(i+1);
		act.pop_back();
	}
	act += '1';
	fun(i+1);
	act.pop_back();
}

int main()
{
    freopen("/home/khaled/file.in","r",stdin);
    freopen("/home/khaled/file.out","w",stdout);
    int T,tc(1);
    cin >> T;
    while(T--){
		printf("Case #%d:\n",tc++);
		cin >> n >> k;
		act = "";
		fun(0);
    }
    return 0;
}



