#include <stdio.h>

using namespace std;

short x[50], res[50][100];

short l = 0, ld = 1, temp, temp1;


void wypiszx(short* x1, int i){
	while (x1[i] == 0) i--;
	while (i >=0 ) printf("%d", x1[i--]);
	printf(" %d %d\n", l, ld);
}

void fairandsquare(short* x1){
	static int qqqq = 0;
	for (int i = 0; i < 100; i++) res[qqqq][i] = 0;
	//square
	int i = 0;
	for (int j = 0; j < ld; j++){
		temp = temp1 = 0;
		for (i = 0; i < ld; i++){
			temp1 = (res[qqqq][i+j] + temp + x1[i] * x1[j]) / 10;
			res[qqqq][i+j] = (res[qqqq][i+j] + temp + x1[i] * x1[j]) % 10;
			temp = temp1;
		}
		if (temp != 0) res[qqqq][i+j+1]=temp;
	}
	//check
	
	int j = 44;
	i = 0;
	while (res[qqqq][j] < 1){
		
		//printf("w %d w\n", res[qqqq][j]);
		res[qqqq][j] = -1;
		j--;
	}
	
	while (i < j && res[qqqq][i] == res[qqqq][j]){
		i++;
		j--;
	}
	if (res[qqqq][i] == res[qqqq][j]){//ok
		qqqq++;
	}
}

void gen(){
	for (int i = 0; i < 50; i++) {
		x[i] = 0;
		for (int q = 0; q < 100; q++) 
			res[i][q] = 0;
	}
	while ( ld < 8 ) {
		x[0]++;
		while ( true){
		fairandsquare(x);
			int i = l;
			if ( x[i] != 9 ) {
				x[i]++;
			}
			else {
				x[i] = 0;
				temp = i+1;
				while ( x[temp] == 9 ) {
					x[temp] = 0;
					x[ld-temp-1] = 0;
					temp++;
				}
				x[temp]++;
				x[ld-temp-1]++;
				if ( temp == ld) {
					if (ld % 2) {
						l++;
					}
					ld++;
					break;
				}
			}
		}
		x[0]++;
		while ( true){
		fairandsquare(x);
		int i = l;
			if ( x[i] != 9 ) {
				x[i]++;
				x[i-1]++;
			}
			else {
				x[i] = 0;
				x[i-1] = 0;
				temp = i+1;
				while ( x[temp] == 9 ) {
					x[temp] = 0;
					x[ld-temp-1] = 0;
					temp++;
				}
				x[temp]++;
				x[ld-temp-1]++;
				if ( temp == ld) {
					ld++;
					break;
				}
			}
		}
	}
}

int all = 48;

int len(short* number){
	int i = 0;
	//printf("len1\n");
	while (number[i] > -1 && i < 50) {
		//printf("%d", number[i]);
		i++;
	}
	//printf("len2\n");
	return i;
}

int compare(short* num1, short* num2){
	//printf("compare1\n");
	if( len(num1) > len(num2) ) return -1;
	else if (len(num1) < len(num2)) return 1;
	else {
		int i = 0;
		while (num1[i] != -1 && num1[i] == num2[i]){
			i++;
			//printf("%d\n", num1[i]);
		}
		//printf("compare2\n");
		if (num1[i] == -1) return 0;
		else if (num1[i] > num2[i]) return -1;
		else if (num1[i] < num2[i]) return 1;
	}
}

int findStart(short* start){
	int i = 0, k = all;
	int j = k/2;
	//printf("findStart1\n");
	while ( i < k ){
		//printf("findStart2\n");
		j = (k+i)/2;
		//printf("%d %d %d\n", i, j, k);
		if (compare(start, res[j]) == 1)k = j;
		else if (compare(start, res[j]) == -1) i = j + 1;
		else return j;
		//printf("findStart3\n");
		//printf("%d %d %d\n", i, j, k);
	}
	return i;
}

int findStop(short* stop){
	int i = 0, k = all;
	int j = k/2;
	//printf("findStop1\n");
	while ( i < k ){
		//printf("findStop2\n");
		j = (k+i)/2+1;
		//printf("%d %d %d\n", i, j, k);
		if (compare(stop, res[j]) == 1)k = j - 1;
		else if (compare(stop, res[j]) == -1) i = j;
		else return j;
		//printf("findStop3\n");
		//printf("%d %d %d\n", i, j, k);
	}
	return i;
}

int find(short* start, short* stop){
	//printf("%d %d\n", findStop(stop), findStart(start));
	
	return findStop(stop) - findStart(start) + 1;
}

int main(){
	
	gen();
	int all = 48;//max 14
	//teraz szukanie po tablicy...
	int instances;
	char start_t[50], stop_t[50];
	short start[50], stop[50];
	scanf("%d", &instances);
	for (int i = 0; i < instances; i++){
		scanf("%s", start_t);
		scanf("%s", stop_t);
		for (int k = 0; k < 50; k++){
			while ( start_t[k] > 40 ){
				start[k] = start_t[k]-48;
				k++;
			}
			start[k]=-1;
		}
		for (int k = 0; k < 50; k++){
			while ( stop_t[k] > 40 ){
				stop[k] = stop_t[k]-48;
				k++;
			}
			stop[k]=-1;
		}
		printf("Case #%d: %d\n", i+1, find(start, stop));
	}
	return 0;
}
