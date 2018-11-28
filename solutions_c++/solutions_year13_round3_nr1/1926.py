#include <cstdio>
#include <cstring>
#include <string>
#include <unordered_set>

#define MAX_LEN 101

bool isCon(char a){
	return a != 'a' && a != 'e' && a != 'i' && a != 'o' && a != 'u';
}

int solve(char *name, int n){

	std::unordered_set<std::string> str_set;

	int l = strlen(name), x = 0, total = 0;
	char buf[8];
	int *ptr_a = (int*)&buf[0], *ptr_b = (int*)&buf[4];
	if( l < n ) return 0;

	for(int p = 0; p < l; p++){
		if(isCon(name[p])) {
			if( x < n ) x++;
			if( x < n ) continue;

			for(int i = 0; i <= p - n + 1; i++)
				for(int j = p; j < l; j++){
					/*
					char t = name[j + 1];
					name[j + 1] = 0;
					std::string a(&name[i]);
					name[j + 1] = t;
					*/
					*ptr_a = i; *ptr_b = j;
					std::string a(buf, 8);
					if(str_set.count(a) > 0) continue;
					str_set.insert(a);
					//printf("%d %d %d\n", p, i, j);
					total++;
				}
		}else{
			x = 0;
		}
	}

	return total;
}

int main() {

	char str[MAX_LEN] = {0};
	int t, n;

	scanf("%d", &t);

	for(int c = 1; c <= t; c++){

		scanf("%s%d", str, &n);

		printf("Case #%d: %d\n", c, solve(str, n));
	}

	return 0;
}