#include <vector>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

char _buffer[2048];

#define FILE_NAME "B"
#define ULL unsigned long long
#define CASET int _t=0, case_num;cin>>case_num;while(++_t<=case_num)

typedef vector<int> VI;
typedef vector<VI> VVI;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
char dir[4] = {'E', 'S', 'W', 'N'};

bool solve()
{
	return false;
}

bool allPlus(string s){
	for(int i=0;i<s.length();i++){
		if(s[i]=='-')
			return false;
	}
	return true;
}

int main()
{
	sprintf(_buffer, "%s.in", FILE_NAME);
	freopen(_buffer, "r", stdin);
	sprintf(_buffer, "%s.out", FILE_NAME);
	freopen(_buffer, "w", stdout);

	CASET
	{
		int ans = 0, plus=0;
		string s;
		cin>>s;
		for(int i=0;i<s.length();i++)
			if(s[i]=='+')
				plus++;

		while(plus!=s.length()){
			char ch;
			int cnt=1;
			for(int i=0;i<s.length();i++){
				if(i){
					if(s[i]==ch)
						cnt++;
					else
						break;
				}
				else
					ch=s[i];
			}
			for(int i=0;i<cnt;i++)
				if(s[i]=='+'){
					s[i] = '-';
					plus--;
				}
				else{
					s[i] = '+';
					plus++;
				}
			// cout<<s<<endl;
			ans++;
		}
		
		cout<<"Case #"<<_t<<": "<<ans<<endl;
	}
		
	return 0;
}