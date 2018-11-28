#include <stdio.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <string.h>
#include <queue>
#include <limits>
#include <map>

using namespace std;

void solve();

int main(){
	int cases;
	scanf("%d", &cases);

	for(int i=1; i<=cases; i++){
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}

void solve(){
	int strings, index = 0, len;
	char buf[100][110], curr, ref[110], stats[100][100];
	memset(stats, 0, sizeof(stats));

	scanf("%d", &strings);

	for(int i=0; i<strings; i++){
		scanf("%s", buf[i]);
	}

	curr = '-'; //FEGLA
	for(int i=0; i<strlen(buf[0]); i++){
		if(curr!=buf[0][i]){
			ref[index] = buf[0][i];
			curr = buf[0][i];
			index++;
		}
	}
	ref[index] = '\0';
	len = index;

	for(int i=0; i<strings; i++){
		index = 0;
		for(int j=0; j<strlen(buf[i]); j++){
			if(ref[index]!=buf[i][j]){
				printf("Fegla Won\n");
				return;
			}else{
				while(ref[index]==buf[i][j]){
					j++;
				}
				j--;
			}
			index++;
		}
		if(len!=index){
			printf("Fegla Won\n");
			return;
		}
	} //FEGLA SLUT
	
	int count;
	for(int i=0; i<strings; i++){ //f�r varje str�ng
		curr = buf[i][0];
		index = 0;
		for(int j=0; j<strlen(buf[i]); j++){ //f�r varje tecken i str�ngen
			count = 0;
			while(curr == buf[i][j]){
				j++;
				count++;
			}
			curr = buf[i][j];
			j--;
			stats[i][index] = count;
			index++;
		}

		/*printf("\n");
		for(int j=0; j<index; j++){
			printf("%d ", stats[i][j]);
		}
		printf("\n");*/
	}
	
	int res = 0, min, tmp, tmp2;
	for(int i=0; i<index; i++){ //f�r varje index
		min = 1000000;
		for(int j=1; j<=100; j++){ //f�r varje m�jlig kombination
			tmp = 0;
			for(int k=0; k<strings; k++){ //f�r varje str�ng
				tmp2 = (j-stats[k][i]); //f�rskjutning som beh�vs
				if(tmp2<0){
					tmp2 = -tmp2;
				}
				tmp += tmp2;
			}
			if(tmp<min){
				min = tmp;
			}
		}
		//printf("min: %d\n", min);
		res += min;
	}
	printf("%d\n", res);
}