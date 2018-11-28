// Create your own template by modifying this file!
#include <iostream>
using namespace std;

#define INF 100000000
#define pb push_back
#define PII pair<int,int>
#define mp make_pair
#define MAXN 100005

bool happy[105], aux[105];
string s;

bool isHappy(){
	for(int i = 0; i < s.length(); i++)
		if(!happy[i])
			return false;
	return true;
}

void reverse(int n){
	for(int i = 0; i <= n; i++)
		aux[i] = happy[i];
	for(int i = n; i >= 0; i--)
		happy[i] = !aux[n-i];
}

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cin >> s;
		for(int i = 0; i < s.length(); i++)
			happy[i] = s[i] == '+';
		int res = 0;
		while(!isHappy()){
			if(happy[0]){
				int i = 0;
				while(i < s.length() && happy[i]){
					happy[i] = false;
					i++;
				}
			}else{
				int lastM = 0;
				for(int i = 0; i < s.length(); i++)
					if(!happy[i])
						lastM = i;
				reverse(lastM);
			}
			res++;
		}
		cout << "Case #" << t << ": " << res << endl;
	}
}

