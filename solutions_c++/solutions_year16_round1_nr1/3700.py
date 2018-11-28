#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int p=1;p<=t;p++){
		string str;
		cin>>str;
		vector<char> ans;
		ans.push_back(str[0]);
		for(int i=1;i<str.length();i++){
			if(str[i]>=ans[0])
				ans.insert(ans.begin(), str[i]);
			else
				ans.push_back(str[i]);
		}
		printf("Case #%d: ", p);
		for(int i=0;i<ans.size();i++)
			printf("%c", ans[i]);
		cout<<endl;
	}
	return 0;
}