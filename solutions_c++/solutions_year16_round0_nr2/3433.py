#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define mem(a, v) memset(a, v, sizeof(a))
#define PI 3.14159265358979323846
typedef long long ll;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<VI> matrix;
const ll MOD = 1000000007LL;

string flip(string str, int idx)
{
	reverse(str.begin(), str.begin() + idx);
	for(int i=0; i<idx; i++){
		if(str[i] == '+')
			str[i] = '-';
		else
			str[i] = '+';
	}
	return str;
}

bool isOk(string str)
{
	for(int i=0; str[i]; i++){
		if(str[i] == '-')
			return false;
	}
	return true;
}

int bfs(string str, int n)
{
	int ret = 0;
	while(true){
		if(isOk(str))
			break;
		for(int i=0; str[i]; i++){
			if(str[i] == '-'){
				str = flip(str, i);
				if(i)
					ret++;
				break;
			}
		}
		if(isOk(str))
			break;
		for(int i=n-1; i>=0; i--){
			if(str[i] == '-'){
				str = flip(str, i+1);
				ret++;
				break;
			}
		}
	}
	return ret;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; tc++){
		string str;
		cin>>str;
		int n = str.length();
		int ans = bfs(str, n);	
		printf("Case #%d: %d\n", tc, ans);	
	}
	return 0;
}