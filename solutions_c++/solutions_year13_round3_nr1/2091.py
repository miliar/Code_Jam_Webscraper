#include<stdio.h>
#include<string.h>
#include<assert.h>
#include<vector>
using namespace std;

int tcnt;
char chrs[1000001];
int conseqconson[1000001];
vector<int> links;
int chrlen;
int N;

bool isVowel(char c){
	assert('a' <= c && c <= 'z');
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main(){
	scanf("%d", &tcnt);
	for(int tidx = 1; tidx <= tcnt; tidx++){
		scanf(" %s %d", chrs, &N);
		links.clear();
		chrlen = strlen(chrs);

		int i;
		for(i = 0; i <= chrlen; i++)
			conseqconson[i] = 0;
		if(!isVowel(chrs[0])){
			conseqconson[0] = 1;
		}else
			conseqconson[0] = 0;
		for(i = 1; i < chrlen ;i++){
			if(isVowel(chrs[i])){
				conseqconson[i] = 0;
			}else{
				conseqconson[i] = conseqconson[i - 1] + 1;
			}
		}
		if(conseqconson[chrlen - 1] < N)
			conseqconson[chrlen - 1] = 0;
		for(i = chrlen - 2; i >= 0; i--){
			if(conseqconson[i +1] != 0 && conseqconson[i] != 0)
				conseqconson[i] = conseqconson[i +1];
			else if(conseqconson[i + 1] == 0 && conseqconson[i] != 0)
				if(conseqconson[i] < N)
					conseqconson[i] = 0;
		}
		if(conseqconson[0])
			links.push_back(0);
		for(i = 1; i < chrlen; i++){
			if(conseqconson[i] != 0 && conseqconson[i - 1] == 0)
				links.push_back(i);
		}
		if(links.size() == 0){
			printf("Case #%d: 0\n", tidx);
			continue;
		}

		__int64 answer = 0;

		int lsize = links.size();

		
		int leastpos = links[0] + conseqconson[links[0]] - N;

		__int64 tmp = conseqconson[leastpos] - N;
		answer += (tmp + 1) * (links[0] + 1) + (tmp +1) * tmp / 2;

		int befend = links[0] + conseqconson[links[0]] - 1;
		for(i = 1; i < lsize; i++){
			// more than N!
			int nextleastpos = links[i] + conseqconson[links[i]] - N;
			tmp = conseqconson[nextleastpos] - N;
			answer += (links[i] - befend - 1) * (leastpos + 1);
			answer += (N - 1) * (leastpos + 1);
			answer += (tmp + 1) * (links[i] + 1) + (tmp +1) * tmp / 2;
			leastpos = nextleastpos;

			befend = links[i] + conseqconson[links[i]] - 1;
		}
		// 뒤에 공백이 남아있따.
		answer += (leastpos + 1) * (chrlen - befend - 1);
		
		printf("Case #%d: %I64d\n", tidx, answer);
	}
	return 0;
}
/*
aaaabbbaaaa 3 35
abbbbbba 2
bbb 3
baaabaaab 3
bbbbbbbbbba 11
*/