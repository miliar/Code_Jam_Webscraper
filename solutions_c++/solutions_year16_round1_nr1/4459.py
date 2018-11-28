#include<iostream>
#include<list>
using namespace std;


list<char> lst;
void process() {
	char str[1002];
	scanf("%s", &str);


	lst.push_back(str[0]);
	int len = 1;
	while (str[len]) {
		

		if (str[len] >= lst.front())
			lst.push_front(str[len]);
		else
			lst.push_back(str[len]);
		len++;
	}

	while (lst.size()) {
		printf("%c", lst.front());
		lst.pop_front();
	}printf("\n");
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T;i++){
		printf("Case #%d: ", i);
		process();
	}


	return 0;
}