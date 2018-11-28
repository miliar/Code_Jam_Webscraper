#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define ALL(x) x.begin(),x.end()

int main(int argc, char const *argv[])
{
	freopen("outs.txt","w",stdout);
	freopen("ins.txt","r",stdin);
	int t;
	scanf("%d",&t);
	for(int ct = 1 ;ct<=t;ct++){
		int ans=0,curpar=0;
		printf("Case #%d: ",ct);
		string s;
		cin >> s;
		int n = s.length();
		if(s[n-1] == '-')
			ans = 1;
		else
			ans = 0;
		if(s[0] == '+')
			curpar = 0;
		else curpar = 1;
		for(int i = 1 ; i < n ; i++){
			if(s[i] == '+' && curpar || s[i] == '-' && !curpar){
				ans++;
				curpar = 1 - curpar;
			}
		}
		printf("%d\n",ans);
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}
