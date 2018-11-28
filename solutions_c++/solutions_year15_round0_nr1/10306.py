#define _CRT_SECURE_NO_WARNINGS

#include <Windows.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main(int argc, char** argv){
	int tCases, shynessLevel, clappingAudience, additionalAudience;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &tCases);
	
	for (int i = 0; i < tCases; i++){
		clappingAudience = 0;
		additionalAudience = 0;
		
		scanf("%d", &shynessLevel);
		
		int audience[shynessLevel+1];
		char c[shynessLevel+1];
		
		scanf("%s\n", c);		
		
		// audience no. = audience[l]
		// audience shyness level = l
		
		for(int l = 0; l <= shynessLevel; l++){
			audience[l] = c[l]-'0';
		}
		
		//printf("Case #%d\n", i+1);
		
		for(int l = 0; l <= shynessLevel; l++){
			if(audience[l] != 0){
				if(clappingAudience >= l){
					clappingAudience += audience[l];
				}
				else if(clappingAudience < l){
					additionalAudience += l-clappingAudience;
					clappingAudience += additionalAudience;
					clappingAudience += audience[l];
				}
			}
			//printf("clapping audience: %d, l = %d, audience no: %d, additionalAudience: %d\n", clappingAudience, l, audience[l], additionalAudience);
		}
		
		printf("Case #%d: %d\n", i+1, additionalAudience);
	}
	
	
	return 0;
}