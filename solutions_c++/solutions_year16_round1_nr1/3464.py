#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<string>

using namespace std;

void solve(int tt)
{
	printf("Case #%d: ",tt);
	string in;
	string ans;
	cin >> in;
	ans.append(in,0,1);  
	int len = in.size();
	for(int i=1;i<len;i++)
	{ 
		if(ans[0] > in[i])
			ans.append(in,i,1);
			
		else
		{
			string tmp = ans;
			ans = "";
			ans.append(in,i,1);
			ans += tmp;
		}
		// cout << ans << endl;
	}
	cout << ans << endl;
	
}
int main()
{
	int tCase ;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&tCase);
	
	for(int i=1;i<=tCase;i++)
		solve(i);
	return 0;
}