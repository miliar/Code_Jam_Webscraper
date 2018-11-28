#include <bits/stdc++.h>
using namespace std;
typedef pair<string, int> si;

string str;

int bfs(){
	string strans, curstr, straux;
	int w, prev;
	queue<si> q;
	set<string> vis;
	for (int i = 0; i < str.size(); i++)
		strans.push_back('+');
	q.push(si(str, 0));
	vis.insert(str);
	
	while (!q.empty()){
		curstr = q.front().first;
		w = q.front().second;
		q.pop();
		if (strans == curstr)
			return w;
		
		for (int i = 0; i < curstr.size(); i++){
			straux = curstr;
			for (int j = 0, k = i; k >= 0; k--, j++)
				straux[j] = curstr[k] == '+'? '-':'+';
			if (!vis.count(straux)){
				vis.insert(straux);
				q.push(si(straux, w + 1));				
			}
		}
	}
	return -1;
}

int main (void){
	int t, cs = 1;
	
	freopen("bsmall.in", "r", stdin);
	freopen("out.txt","w",stdout);
	scanf ("%d", &t);
	getchar();
	while(t--){
		cin >> str;
		printf("Case #%d: %d\n", cs++, bfs());
	}
	
	return 0;
}
