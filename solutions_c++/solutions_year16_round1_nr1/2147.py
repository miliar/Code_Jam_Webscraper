
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout << x << " " << y << endl
#define N 100005

using namespace std;

char s[N];

int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
	
	while(tc--){
		
		scanf("%s", s);
		int len = strlen(s);
		
		deque<char>q;
		q.push_front(s[0]);
	
		for(int i = 1; i < len; i++){
			
			if(q.front() <= s[i])q.push_front(s[i]);
			else q.pb(s[i]);
		}
		
		string ans = "";
		for(int i = 0; i < len; i++)ans.pb(q.front()), q.pop_front();
		
		printf("Case #%d: %s\n", caso++, ans.c_str());
	}


}

