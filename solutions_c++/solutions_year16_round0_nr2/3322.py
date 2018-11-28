#include <iostream>
using namespace std;

int main() {
	int t;
	scanf("%d ", &t);
	for(int tcase = 1; tcase <= t; tcase++) {
		string str;
		cin >> str;
		int len = str.size();
		//for (int i = 0; i < len; i++)
			//cout << str[i]; ////////
		//cout << endl; //// 
		int ultimo_mais = len;
		int op= 0;  //qtd de operações
		while(1) {
			while (ultimo_mais >= 1 && str[ultimo_mais - 1] == '+') {
				ultimo_mais--;
			}
			if (ultimo_mais == 0) 
				break;
			
				
			int primeiros_mais = -1;
			while(str[primeiros_mais + 1] == '+')
				primeiros_mais++;
			for (int i = 0; i <= primeiros_mais; i++) {
				str[i] = '-';
			}
			if (primeiros_mais >= 0) {
				op++;
				//for (int i = 0; i < len; i++)
					//cout << str[i]; ////////
				//cout << endl; ////
			}
				
			string copy (str, 0, ultimo_mais);
			for (int i = 0; i < ultimo_mais; i++) 
				str[i] = copy[ultimo_mais - 1 - i] == '+' ? '-' : '+';
			op++;
			//for (int i = 0; i < len; i++)
				//cout << str[i]; ////////
			//cout << endl; ////
		}
		printf("Case #%d: %d\n", tcase, op);
		
	}
}
