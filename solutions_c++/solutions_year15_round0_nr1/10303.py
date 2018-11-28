#include <cstdio>
#include <string>

int main(int argc, char** argv) {
	int T = 0;
	
	scanf("%d", &T);
	
	for (int i = 0; i < T; ++i) {
		int max_shy_level = 0;
		char people_str[1001];
		
		scanf("%d%s", &max_shy_level, people_str);
		
		int answer = 0, standing_ovation = 0;
		for (int shy_level = 0; shy_level <= max_shy_level; ++shy_level) {
			int people_count = people_str[shy_level] - '0';
			
			if (standing_ovation >= shy_level) {
				standing_ovation += people_count;
			} else {
				++answer;
				standing_ovation += people_count + 1;
			}
		}
		
		printf("Case #%d: %d\n", i+1, answer);
	}
	
	return 0;
}