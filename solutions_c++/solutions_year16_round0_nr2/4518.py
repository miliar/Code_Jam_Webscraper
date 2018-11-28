#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	char temp;
	getchar();
	for (int I = 0; I < T; I++){
		string bread;
		getline(cin,bread);
		char state;
		int c = 1;
		for (int i = 0; i < bread.length(); i++){
			if (i == 0){
				state = bread[i];
				continue;
			}
			if (state != bread[i]) {
				c++;
				state = bread[i];
			}
		}
		if (bread[bread.length() - 1] == '+') c--;

		printf("Case #%d: %d\n", I + 1,c);
	}
	return 0;
}