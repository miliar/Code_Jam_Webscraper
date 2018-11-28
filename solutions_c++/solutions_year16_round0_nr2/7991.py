#include<cstdio>
#include<stack>
#include<vector>
#include<string.h>
using namespace std;
char* ptr_string[101];
char _string[101][101];
int index;
void Pancake();
int _case;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("outputB.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	char temp;
	for (int i = 0; i < T; i++) {
		scanf("%s", _string[i]);
		Pancake();
		index++;
	}	
}
void Pancake() {
	int check = 0;
	for (int i = 0; _string[index][i] != '\0'; i++) {
		if (_string[index][i] == '-') {
			check = i+1;
		}
	}
	if (check == 0) { 
		printf("Case #%d: %d\n", index + 1, _case);
		_case = 0;
		return;
	}
	_case++;
	for (int i = 0; i < check; i++) {
		if (_string[index][i] == '+') {
			_string[index][i] = '-';
		}
		else if (_string[index][i] == '-') {
			_string[index][i] = '+';
		}
	}
	Pancake();
}