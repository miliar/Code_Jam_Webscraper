#include <bits/stdc++.h>

using namespace std;

bool sync_with_stdio (bool sync = false);

typedef long long ll;

char str[110];
stack<char> pilha;
queue<char> fila;

int main(){
	int t, cont  = 1, i, j, tam, ans, flag;
	scanf("%d", &t);
	while(t--){
		scanf(" %s", str);
		tam = (int)strlen(str);
		
		for(i = tam-1; i >= 0; i--)
			pilha.push(str[i]);
		
		flag = 0;
		char ant;
		while(!pilha.empty()){
			if(!flag){
				flag = 1;
				fila.push(pilha.top());
				ant = pilha.top();
				pilha.pop();
			}
			else if(ant != pilha.top()){
				fila.push(pilha.top());
				ant = pilha.top();
				pilha.pop();
			}
			else pilha.pop();
		}
		ans = 0;
		
		if(fila.size() == 1){
			if(fila.front() == '-') ans++;
			fila.pop();
		}
		
		else{
			flag = 0;
			while(!fila.empty()){
				if(!flag){
					ant = fila.front();
					fila.pop();
					flag = 1;
				}
				else{
					if(ant == '-' && fila.front() == '+'){
						//printf("a\n");
						ans++;
						fila.pop();
						ant = '+';
					}
				
					else if(ant == '+' && fila.front() == '-') {
						//printf("b\n");
						ans += 2;
						fila.pop();
						ant = '+';
					}
					else {//printf("c\n"); 
					fila.pop();}
				}
			}
		}
		
		while(!pilha.empty()) pilha.pop();
		while(!fila.empty()) fila.pop();
		
		
		printf("Case #%d: %d\n", cont++, ans);
	}
	

	return 0;
}
