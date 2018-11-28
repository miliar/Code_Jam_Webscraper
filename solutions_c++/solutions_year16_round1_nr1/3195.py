#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;
int main(){
	int T;
	scanf("%d", &T);
	for(int tt =1; tt<=T; tt++){
		printf("Case #%d:",tt); // standard
		string s;
		cin >> s;
		int curSep = s.length();
		char out[2000];
		bool used[2000];
		for(int i=0; i<curSep; i++) used[i] = false;
		int cur = 0;
		while(curSep >0){
			int tmp = 0;
			for(int i=1; i<curSep; i++)
				if(s[i] >= s[tmp] ) tmp = i;
			out[cur++] = s[tmp];
			used[tmp] = true;
			curSep = tmp;
		}
		for(int i=0; i<s.length();i++)
			if(!used[i])
				out[cur++] = s[i];
		out[cur] = 0;
		printf(" %s", out);
		//cout<<s<<'.'<<s.length()<<'.';
		printf("\n"); // endline
	}
	return 0;
}
