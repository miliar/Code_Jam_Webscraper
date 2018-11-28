#include <bits/stdc++.h>
using namespace std;

unordered_set<string> vis;

string flip(string& str, int size){
	string res;
	for (int i = size-1; i >= 0; --i)
	{
		res += str[i]=='+'?"-":"+";
	}
	for(int i = size; i < (int)str.size(); i++)
		res += str[i];
	return res;
}
int calc(string str){
	queue<string> q;
	q.push(str);
	vis.insert(str);
	int res = 0;
	while(q.size()){
		int siz = q.size();
		while(siz--){
			str = q.front();
			q.pop();
			if(str.find("-") == str.npos) return res;
			for (int s = 1; s <= str.size(); ++s)
			{
				string next = flip(str,s);

				if(vis.count(next)) continue;
				vis.insert(next);
				q.push(next);
			}
		}
		res++;
	}
	return -1;
}
int main(){
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int tst;
	cin >> tst;

	for (int t = 1; t <= tst; ++t)
	{
		string str;
		cin >> str;
		printf("Case #%d: ", t);
		vis.clear();
		printf("%d\n",calc(str));
	}

}
