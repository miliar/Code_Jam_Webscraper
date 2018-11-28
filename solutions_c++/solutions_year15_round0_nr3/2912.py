#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
#define sd(x) scanf("%d", &x)
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define ft first
#define sc second
#define INF 1000000000
#define MOD 10000007
int arr[5][5];
int n;
string s;
int dp[10010][10][5][3];
int func(int ind, int num, int count, int neg)
{
	//cout<<ind<<" "<<num<<" "<<count<<" "<<neg<<endl;
	if(ind == n)
		return num == 4 && count == 2 && neg == 0;
		
	if(dp[ind][num][count][neg] != -1)
		return dp[ind][num][count][neg];
		
	int ans = 0;
	int cur;
	if (s[ind] == 'i') cur = 2;
	if (s[ind] == 'j') cur = 3;
	if (s[ind] == 'k') cur = 4;
	
	int nxt = arr[num][cur];
	
	if(nxt == 2 && count == 0 && neg == 0) {
			ans = max(ans, func(ind+1, 1, 1, 0));
			ans = max(ans, func(ind+1, 2, 0, 0));
			return dp[ind][num][count][neg] = ans;		
	}if(nxt == 6 && count == 0 && neg == 1) {
			ans = max(ans, func(ind+1, 1, 1, 0));
			ans = max(ans, func(ind+1, 2, 0, 0));
			return dp[ind][num][count][neg] = ans;
	}
	if(nxt == 3 && count == 1 && neg == 0) {
			ans = max(ans, func(ind+1, 1, 2, 0));
			ans = max(ans, func(ind+1, 3, 1, 0));
			return dp[ind][num][count][neg] = ans;	
	}
	if(nxt == 7 && count == 1 && neg == 1) {
			ans = max(ans, func(ind+1, 1, 2, 0));
			ans = max(ans, func(ind+1, 3, 1, 0));
			return dp[ind][num][count][neg] = ans;
	}
	else {
		int flag;
		if(neg == 1) {
			flag = (nxt <= 4);
		}
		else {
			flag = (nxt > 4);
		}
		ans = max(ans, func(ind+1, nxt > 4 ? nxt - 4 : nxt, count, flag));
		return dp[ind][num][count][neg] = ans;
	}
	
}
int main()
{
	arr[1][1] = 1; arr[1][2] = 2; arr[1][3] = 3; arr[1][4] = 4;
	arr[2][1] = 2; arr[2][2] = 5; arr[2][3] = 4; arr[2][4] = 7;
	arr[3][1] = 3; arr[3][2] = 8; arr[3][3] = 5; arr[3][4] = 2;
	arr[4][1] = 1; arr[4][2] = 3; arr[4][3] = 6; arr[4][4] = 5;
	
 	//freopen("inp.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	int t;
	cin>>t;

	for(int cse = 1; cse <= t; cse++) {
		cout<<"Case #"<<cse<<": ";
		memset(dp, -1, sizeof(dp));
		int l, x;
		cin>>l>>x;
		cin>>s;
		string res = "";
		for(int i = 1; i <= x; i++) {
			res += s;
		}
		s = res;
		n = s.length();
		if (func(0, 1, 0, 0)) {
			cout<<"YES"<<endl;
		}else {
			cout<<"NO"<<endl;
		}
	}
	return 0;
}
