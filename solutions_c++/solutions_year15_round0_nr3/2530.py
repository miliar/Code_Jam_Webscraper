#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>

#define rep(k,a) for(int k = 0; k < (a); k++)

using namespace std;
int multiptable[5][5] = { {3333,3333,3333,3333,3333},
	{3333, 1,  2,  3,  4},
	{3333, 2, -1,  4, -3},
	{3333, 3, -4, -1,  2},
	{3333, 4,  3, -2, -1}
};
int prefixes[10000000];
int ctoi(char* c){
		if(c[0] == '-'){
			if(c[1] == 'i')
				return -2;
			if(c[1] == 'j')
				return -3;
			if(c[1] == 'k')
				return -4;
		}
		else{
			if(c[0] == 'i')
				return 2;
			if(c[0] == 'j')
				return 3;
			if(c[0] == 'k')
				return 4;
		}
}
char* itoc(int i){
	if(i < 0){
		if(i == -1)
			return "-1";
		if(i == -2)
			return "-i";
		if(i == -3)
			return "-j";
		if(i == -4)
			return "-k";
	}
	else{
		if(i == 1)
			return "1";
		if(i == 2)
			return "i";
		if(i == 3)
			return "j";
		if(i == 4)
			return "k";
	}

}
int multiply(int i1, int i2){
//	int i1 = ctoi(c1);
//	int i2 = ctoi(c2);
	if(i1 < 0 && i2 > 0 || i1 > 0 && i2 < 0)
		return -multiptable[abs(i1)][abs(i2)];
	else
		return multiptable[abs(i1)][abs(i2)];

}
int product(int i, int j){
//		int beg = prefixes[i-1];
	//	int whole = prefixes[j];
		for(int interv = -4; interv <= 4; interv++){
			if(interv == 0)
				continue;
			if(multiply(i,interv)==j)
				return interv;
		}
		return -666;
}

int main()
{
	int T;
	prefixes[0]=1;
	scanf("%d", &T);
	rep(testcase, T){
		int l, x;
		scanf("%d %d", &l, &x);
		getchar();
		rep(i, l){
			char c = getchar();
			char ptr[2];
			ptr[0]=c;
			ptr[1]='\0';
			prefixes[i+1] = multiply(prefixes[i], ctoi(ptr));
			//printf("pref %d", prefixes[i+1]);
		}
//		for(int i = 1; i <= l; i++){
	//		printf("%s\n", itoc(prefixes[i]));
		//}
	//	printf("\n\n");
	//	printf("from 2 to 4 %s\n\n", itoc(product(2,4)));
		bool found = false;
		for(int i = 1; i <= l*x-2 && !found; i++){
			int celku = i / l;
			int pozice = i % l;
			//if(pozice == 0) pozice = l;
		//	printf("Pozice %d celku %d\n", pozice, celku);
			int p1 = 1;
			int p2 = 1;
			int p3 = 1;
			int cel = 0;
			if(celku % 4 == 0)
				cel = 1;
			else if(celku % 4 == 1)
				cel = prefixes[l];
			else if(celku % 4 == 2)
				cel = -1;
			else
				cel = -prefixes[l];
			p1 = multiply(cel, prefixes[pozice]);
			//printf("p1 %d\n", p1);
			if(p1 != 2)
				continue;
//			printf("found i, from 1 to %d\n", i);
			for(int j = i+1; j<= l*x-1; j++){
				int p2tmp = 1;
				celku = j/l;
				pozice = j%l;
				//if(pozice == 0) pozice = l;
				//printf("celku %d pozice %d\n", celku, pozice);
				if(celku % 4 == 0)
					cel = 1;
				else if(celku % 4 == 1)
					cel = prefixes[l];
				else if(celku % 4 == 2)
					cel = -1;
				else
					cel = -prefixes[l];
				p2tmp = multiply(cel, prefixes[pozice]);
				p2 = product(p1,p2tmp);
				if(p2!=3)
					continue;
	//			printf("FOUND j from %d to %d\n", i+1, j);
				int p3tmp = 1;
				celku = (l*x-(j+1))/l;
				pozice = (j+1)%l;
				if(pozice == 0) pozice = l;
		//		printf("celku %d pozice %d\n", celku, pozice);
				p3tmp = product(prefixes[pozice-1], prefixes[l]);
				if(celku % 4 == 0)
					cel = 1;
				else if(celku % 4 == 1)
					cel = prefixes[l];
				else if(celku % 4 == 2)
					cel = -1;
				else
					cel = -prefixes[l];
				p3 = multiply(p3tmp, cel);
				if(p3!=4)
					continue;
				found = true;
				printf("Case #%d: YES\n", testcase+1);
				break;
			}
			if(found)
				break;
		}
		if(!found)
			printf("Case #%d: NO\n", testcase+1);
	}
	return 0;
}

