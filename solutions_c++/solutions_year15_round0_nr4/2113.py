#include <stdio.h>

bool possible(int x, int r, int c){
	switch (x)
	{
	case 1:
	case 2:
	case 3:
	case 4:
	case 5:
	case 6:
		return (r >= x && c >= x - 1 || c >= x && r >= x - 1) && r * c % x == 0;
	}
	return false;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, m;
	scanf("%d", &t);
	for (m = 0; m < t; m++){
		int x, r, c;
		scanf("%d %d %d", &x, &r, &c);
		printf("%s\n", possible(x, r, c) ? "GABRIEL" : "RICHARD");
	}
	return 0;
}