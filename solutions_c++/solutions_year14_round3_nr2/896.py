#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
//#include<queue>
//#include<stack>
//#include<vector>
//#include<map>


using namespace std;

int t;
int n;
int ans ;
bool used[300];
string instr[200];
char str[1000];
bool vis[300] = {false};

int len;

inline bool ok()
{
//	cout << "check : " << str << endl;
	int x;
	char pre;
	char certain;
	for(int i = 'a' ; i <= 'z' ; i++)
		vis[i] = 0;
	pre = str[0];
	x = 1;
	while(x < len)
	{
	//	cout << "x : " << x << ", y = " << y << endl;
		certain = str[x];
		if(certain != pre)
		{
			vis[pre] = true;
		}
		if(vis[certain])
			return 0;
		else
			pre = certain;
		
		x++;
	}
	return 1;
}

void dfs(int node, int step)
{
	//
//	cout << "node : " << node << ", step = " << step << endl;
	
	used[node] = true;
	
	strcat(str,instr[node].c_str());
	len = strlen(str);
	
	if(step == n-1)
	{
		ans += ok();
	}
	else if(ok())
		for(int i = 0 ; i < n ; i++)
			if(!used[i])
				dfs(i,step+1);
	
	len -= instr[node].size();
	str[len] = '\0';
	used[node] = false;
	
	return;
}


int main()
{
	
	cin >> t;
	for(int k = 1 ; k <= t ; k++)
	{
		//init
		memset(used, 0, sizeof(used));
		ans = 0;
		
		cin >> n;
//		cout << "n = " << n << endl;
				
		for(int i = 0 ; i < n ; i++)
			cin >> instr[i];
		
	//	puts("in ok");
	//	puts("start dfs()");
		for(int i = 0 ; i < n ; i++)
		{
	//		cout << "dfs : " << i << endl;
			dfs(i,0);
		}
		printf("Case #%d: %d\n",k,ans);
	}
	
	return 0;
}

