#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main(int argc, char **argv){
	int cases, maxlevel;
	char people;
	int people_clapping, friends_invited;
	
	FILE *input = fopen(argv[1], "r+");
	
	FILE *output = fopen(argv[2], "w+");

	fscanf(input, "%d", &cases);
	
	for(int i = 0; i < cases; i++){
		fscanf(input, "%d", &maxlevel);
		
		vector<int> shy_levels;
		
		fscanf(input, "%c", &people);
		for(int j = 0; j <= maxlevel; j++){
			fscanf(input, "%c", &people);
			shy_levels.push_back((int)people - '0');
		}
		
		people_clapping = shy_levels[0];
		//printf("People initially clapping: %d\n", people_clapping);
		friends_invited = 0;
		
		for(int j = 1; j <= maxlevel; j++){
			//printf("#people of shy level %d: %d, clapping: %d\n", j, shy_levels[j], people_clapping);
			if(shy_levels[j] != 0){
				if(people_clapping >= j){
					people_clapping += shy_levels[j];
				}
				else{
					friends_invited += j - people_clapping;
					people_clapping += friends_invited + shy_levels[j];
				}
			}
		}
		
		fprintf(output, "Case #%d: %d\n", i+1, friends_invited);
	}
	return 0;
}