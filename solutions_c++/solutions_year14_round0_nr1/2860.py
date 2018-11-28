#include<stdio.h>
#include<stdlib.h>

using namespace std;
#include<set>

set<int> candidate;

int main(int argc, char* argv[]){
    FILE *fin;
    fin = fopen(argv[1], "r");

    int T, row, card, hit, hitcnt;
    fscanf(fin, " %d ", &T);
    for(int tc=0; tc<T; ++tc){
	candidate.clear();

	fscanf(fin, " %d ", &row);
	for(int r=0; r<4; ++r){
	    for(int c=0; c<4; ++c){
		fscanf(fin, " %d ", &card);
		if(r+1 == row){
		    candidate.insert(card);
		}
	    }
	}

	hit = -1;
	hitcnt = 0;
	fscanf(fin, " %d ", &row);
	for(int r=0; r<4; ++r){
	    for(int c=0; c<4; ++c){
		fscanf(fin, " %d ", &card);
		if(r+1 == row){
		    if(candidate.count(card) > 0){
			++hitcnt;
			hit = card;
		    }
		}
	    }
	}

	if(hitcnt == 1){
	    printf("Case #%d: %d\n", tc+1, hit);
	}else if(hitcnt == 0){
	    printf("Case #%d: Volunteer cheated!\n", tc+1);
	}else if(hitcnt > 1){
	    printf("Case #%d: Bad magician!\n", tc+1);
	}else{
	    printf("error!\n");
	}
    }
    fclose(fin);

    return 0;
}
