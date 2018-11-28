
#include<stdio.h>
#include <vector>

using namespace std;

int abs(int a) {
	return a<0? -a :a;
}

void testCase() {
	int number;
	scanf("%d", &number);

	vector<char> wzor;
	vector<int> *ilosci = new vector<int>[number];

	char text[101];
	for(int i=0; i<number; i++) {
		scanf("%s", text);
		int znak = 0;
		int ileZnakow = 0;
		for(int j=0; text[j]!=0; j++) {
			if(text[j] != znak) {
				if(znak!=0) {
					ilosci[i].push_back(ileZnakow);
				}
				znak=text[j];
				ileZnakow=1;
				if(i==0) {
					wzor.push_back(znak);
				}
				else {
					if(ilosci[i].size() >= wzor.size() || znak != wzor[ilosci[i].size()]) {
						printf("Fegla Won\n");
						return;
					}
				}
			}
			else {
				ileZnakow++;
			}
		}
		ilosci[i].push_back(ileZnakow);
		if(ilosci[i].size() != wzor.size()) {
			printf("Fegla Won\n");
			return;
		}
	}

	int suma = 0;
	for(int i=0; i<ilosci[0].size(); i++) {
		int min = 1000;
		int max = 0;
		for(int j=0; j<number; j++) {
			if(ilosci[j][i] > max) {
				max = ilosci[j][i];
			}
			if(ilosci[j][i] < min) {
				min = ilosci[j][i];
			}
		}
		int best = 1000000000;
		
		for(int k=min; k<=max; k++) {
			int sum = 0;
			for(int j=0; j<number; j++) {
				sum+=abs(k - ilosci[j][i]);
			}
			if(sum < best) best=sum;
		}

		suma += best;
	}
	printf("%d\n", suma);
}

int main()
{
	int testCases;
	scanf("%d", &testCases);

	for(int i=0; i<testCases; i++) {
		printf("Case #%d: ", i+1);
		//fprintf(stderr, "Case #%d: ", i+1);
		testCase();
	}
	return 0;
}