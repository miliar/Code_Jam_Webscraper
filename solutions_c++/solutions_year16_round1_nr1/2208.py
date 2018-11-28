#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <vector>
#include <deque>

#define INF 2000000000

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int TC;


int main(){
	scanf("%d", &TC);
	for(int Tn = 1; Tn <= TC; Tn++){
		printf("Case #%d: ", Tn);
		deque<char> S;
		char A;
		int first = -1;
		int length = 0;
		scanf("\n%c", &A);
		while(A != '\n'){
			if((int) A >= first){
				first = (int) A;
				S.push_front(A);
			}else{
				S.push_back(A);
			}
			length++;
			scanf("%c", &A);
		}
		for(int i = 0; i < length; i++) printf("%c", S[i]);
		printf("\n");
	}
}