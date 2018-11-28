#include<cstdio>
#include<algorithm>
#include<string>

using namespace std;

int main(){
	int casos, res;
	char aux[1024];
	string s;
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
		scanf(" %s", aux); s = aux; s += '+';
		res = 0;
		bool flip = true;
		while(flip){
			flip = false;
			for(int i=1;i<s.size();i++){
				if(s[i] != s[i-1]){
					flip = true;
					for(int j=0;j<i;j++) s[j] = s[i];
					res++;
					break;
				}
			}
		}
		printf("Case #%d: %d\n", inst, res);
	}
	return 0;
}