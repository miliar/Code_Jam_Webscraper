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
#define INF 2000000000
#define MOD 1000000007
#define D double
#define LD long double

int mat[5][5] =  { {0, 0,  0,  0,  0},
				   {0, 1,  2,  3,  4},
				   {0, 2, -1,  4, -3},
				   {0, 3, -4, -1,  2},
				   {0, 4,  3, -2, -1} };

int mul(int a, int b){
	int ret = 1;
	if(a < 0){
		a = -a;
		ret = -1;
	}
	if(b < 0){
		b = -b;
		ret = -ret;
	}
	ret *= mat[a][b];
	return ret;
}

#define N 2222222

string s;
int a[N];

int main(){
	freopen("ip.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	sd(t);
	for(int c = 1; c <= t; c++){
		int l, y, i, leni, lenk, l2;
		long long int x;
		string res[] = {"YES", "NO"};
        printf("Case #%d: ", c);
		cin>>l>>x;
        cin>>s;
        if(x % 4 == 0){
            cout<<res[1]<<"\n";
            continue;
        }
        y = 1;
        for(i = 0; i < l; i++){
            a[i] = s[i] - 'g';
            y = mul(y, a[i]);
        }
        if(x % 2 == 0){
            if(y == 1 || y == -1){
                cout<<res[1]<<endl;
                continue;
            }
        }
        else{
            if(y != -1){
                cout<<res[1]<<endl;
                continue;
            }
        }
        leni = INF;
        lenk = INF;
        l2 = 4 * l;
        for(i = l; i < l2; i++){
            a[i] = a[i - l];
        }
        y = 1;
        for(i = 0; i < l2; i++){
            y = mul(y, a[i]);
            if(y == 2){
                leni = i + 1;
                break;
            }
        }
        y = 1;
        for(i = l2 - 1; i >= 0; i--){
            y = mul(a[i], y);
            if(y == 4){
                lenk = l2 - i;
                break;
            }
        }
        if(leni == INF || lenk == INF){
            cout<<res[1]<<endl;
        }
        else if(leni + lenk <= x * l){
            cout<<res[0]<<endl;
        }
        else{
            cout<<res[1]<<endl;
        }
	}
	return 0;
}
