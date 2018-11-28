#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <queue>
#include <map>

using namespace std;

map<string, bool> vmap;


int bfs(string str, string gstr, int len){
	queue<pair<string, int> > q;

	vmap[str] = true;
	q.push(make_pair(str, 0));

	while(!q.empty()){
		string s = q.front().first;
		int t = q.front().second;
		q.pop();

		if(s == gstr){
			return t;
		}

		for(int i=1; i<=len; i++){
			string ts = s;
			reverse(ts.begin(), ts.begin()+i);
			for(int j=0; j<i; j++){
				if(ts[j] == '-'){
					ts[j] = '+';
				}
				else{
					ts[j] = '-';
				}
			}
			//cout << ts << endl;

			if(!vmap[ts]){
				q.push(make_pair(ts, t+1));
				vmap[ts] = true;
			}
		}
	}

	return -1;
}

int main(void){

	int testcase;
	scanf("%d", &testcase);

	for(int t_itr=1; t_itr<=testcase; t_itr++){
		vmap.clear();

		string str;
		cin >> str;

		int len = str.length();

		string gstr = "";
		for(int i=0; i<len; i++){
			gstr += "+";
		}

		printf("Case #%d: ", t_itr);
		printf("%d\n", bfs(str, gstr, len));
	}

	return 0;
}