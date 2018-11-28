#include<iostream>

char cake[110];
bool allP(){
	int i = 0;
	while (cake[i] != '\0'){
		if (cake[i] == '-'){
			return false;
		}
		i++;
	}
	return true;
}
bool allN(){
	int i = 0;
	while (cake[i] != '\0'){
		if (cake[i] == '+'){
			return false;
		}
	}
	return true;
}
void flip(){
	int answer = 0;
	char fisrt = cake[0];
	while (cake[answer] == fisrt){
		if (fisrt == '+'){
			cake[answer] = '-';
		}
		else{
			cake[answer] = '+';
		}
		answer++;
	}

}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("d.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int x = 1; x <= T; x++){
		int answer = 0;
		scanf("%s", cake);
		while (allP() != true){
			answer++;
			flip();
		}
		printf("Case #%d: %d\n", x, answer);
	}
}