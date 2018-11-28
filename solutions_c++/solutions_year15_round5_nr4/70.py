#include<bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef long long int LL;
typedef vector<int> VI;

#define sd(x) scanf("%d", &x)
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define MOD 1000000007
#define D double
#define LD long double
double EPS = 1e-12;

#define N 2223456

int a[N], b[N], f[N], p[N];
bool done[N];

int main(){
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	sd(t);
	for(int cas = 1; cas <= t; cas++){
		int k, i, j, s, n, s2;
		cin>>k;
		for(i = 0; i < k; i++){
			cin>>p[i];
		}
		for(i = 0; i < k; i++){
			cin>>f[i];
		}
		s = 0;
		for(i = 0; i < k; i++){
			while(f[i]--){
				a[s] = p[i];
				s++;
			}
		}
		sort(a, a + s);
		printf("Case #%d: ", cas);
		while(true){
			//cout<<s<<" ";
			cout<<a[1];
			//system("pause");
			if(s == 2){
				cout<<"\n";
				break;
			}
			else{
				cout<<" ";
			}
			for(i = 0; i < s; i++){
				done[i] = false;
			}
			done[1] = true;
			done[0] = true;
			j = a[1];
			b[0] = 0;
			s2 = 1;
			k = 0;
			for(i = 2; i < s; i++){
				while(k < i){
					if(done[k] == false){
						break;
					}
					k++;
				}
				if(k < i){
					if(a[i] - a[k] == a[1]){
						b[s2] = a[k];
						s2++;
						done[i] = true;
						done[k] = true;
					}
				}
			}
			for(i = 0; i < s2; i++){
				a[i] = b[i];
			}
			sort(a, a + s2);
			s = s2;
		}
		//cerr << "Case #" << cas << ": Done!" << endl;
	}
	return 0;
}

