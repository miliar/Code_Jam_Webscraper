#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
void remove_leading(char s[]){
	int curr_len = strlen(s);
	int i = curr_len - 1;
	while(i >= 0 && s[i] == '+'){
		s[i] = '\0';
		i--;
	}
}
void reverse(int len, char s[]){
	for(int i = 0; i < len/2; i++){
		char t = (s[i] == '+')?'-':'+';
		s[i] = (s[len - i - 1] == '+')?'-':'+';
		s[len - i - 1] = t;
	}
	if(len%2 == 1){
		s[len/2] = (s[len/2] == '+')?'-':'+';
	}	
}
void flip(int len, char s[]){
	int i = 0;
	while(i < len && s[i] == '+'){
		s[i] = '-';
		i++;
	}
}
int main(int argc, char const *argv[])
{
	int T = 0;
	scanf("%d", &T);
	for(int t = 0; t < T; t++){
		char s[101] = {'\0'};
		scanf("%s", s);
		int len = 0, count = 0;
		remove_leading(s);
		while((len = strlen(s)) > 0){
			// printf("%d %s\n", len, s);
			int i = 0;
			if(s[i] == '-')
				reverse(len, s);
			else
				flip(len, s);
			count++;
			remove_leading(s);
		}
		printf("Case #%d: %d\n", (t + 1), count);
	}
	return 0;
}