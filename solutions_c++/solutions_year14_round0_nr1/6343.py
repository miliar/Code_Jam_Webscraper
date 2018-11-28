#include <cstdio>
#include <set>

using namespace std;

FILE * magic = fopen("magic.out", "w");

int main(){
	int nc;
	scanf("%d", &nc);
	for(int caso = 1; caso <= nc; caso++){
		fprintf(magic, "Case #%d: ", caso);
		int row;
		set<int> s1, intersec;
		int num;
		scanf("%d", &row);
		for(int i = 1; i <= 4; i++){
			for(int k = 1; k<= 4; k++){
				scanf("%d", &num);
				if(i == row){
					s1.insert(num);
				}
			}
		}
		scanf("%d", &row);
		for(int i = 1; i <= 4; i++){
			for(int k = 1; k<= 4; k++){
				scanf("%d", &num);
				if(i == row){
					if(s1.find(num) != s1.end())
						intersec.insert(num);
				}
			}
		}
		if(intersec.empty()){
			fprintf(magic, "Volunteer cheated!\n");
		}
		else if(intersec.size() > 1)
			fprintf(magic, "Bad magician!\n");
		else fprintf(magic, "%d\n", *(intersec.begin()));
	}
	fclose(magic);
	return 0;
}