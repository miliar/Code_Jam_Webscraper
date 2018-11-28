#include<string>
#include<sstream>
#include<iostream>

using namespace std;

bool vis[256];

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int n;
	unsigned long long res;

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n;
		if (n==0){
			cout << "Case #" << tc << ": " << "INSOMNIA" << endl;
			continue;
			
		}
		res = n;
		memset(vis,0,sizeof(vis));
		int count = 10;
		while(1){
			string s;
			stringstream ss;
			ss << res;
			ss >> s;
			for (int i=0;i<s.length();i++)
				if (!vis[s[i]]) vis[s[i]] = true,count--;
			if (!count)
				break;
			res += n;
		}
		cout << "Case #" << tc << ": " << res << endl;

	}

	return 0;
}