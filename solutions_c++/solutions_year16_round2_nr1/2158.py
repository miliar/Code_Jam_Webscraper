#include<bits/stdc++.h>
using namespace std;

inline void print(char pt) {
	printf("%c\n", pt);
}
inline void print(int pt) {
	printf("%d\n", pt);
}
inline void print(long long pt) {
	printf("%I64d\n", pt);
}
inline void print(double pt) {
	printf("%f\n", pt);
}
inline void print(char pt[]) {
	printf("%s\n", pt);
}

inline void scan(int &pt) {
	scanf("%d", &pt);
}
inline void scan(long long &pt) {
	scanf("%I64d", &pt);
}
inline void scan(double &pt) {
	scanf("%lf", &pt);
}
inline void scan(char pt[]) {
	scanf("%s", pt);
}
struct pii {
	int a;
	int b;
	friend int operator<(pii a, pii b) {
		if (a.a != b.a)
			return a.a < b.a;
		return a.b < b.b;
	}
};

class str {
	char val[5];
	friend int operator<(str a, str b) {
		return strcmp(a.val, b.val) < 0;
	}
};

int n;
char stra[10050];
int nums[1000];
int whoa[20];

int main() {
	FILE* ina;
	FILE* outa;
	ina = fopen("in.txt","r+");

	outa = fopen("out.txt","w+");

	fscanf(ina,"%d",&n);
	for (int t = 1; t <= n; t++) {
		fscanf(ina,"%s",stra);
		memset(nums,0,sizeof(nums));
		int lena = strlen(stra);
		for (int i = 0; i < lena; i++) {
			nums[stra[i]]++;
		}
		whoa[0] = nums['Z'];
		whoa[2] = nums['W'];
		whoa[4] = nums['U'];
		whoa[6] = nums['X'];
		whoa[8] = nums['G'];
		whoa[3] = nums['R']-whoa[4]-whoa[0];
		whoa[5] = nums['F']-whoa[4];
		whoa[7] = nums['S']-whoa[6];
		whoa[9] = nums['I']-whoa[5]-whoa[6]-whoa[8];
		whoa[1] = nums['N']-whoa[9]*2-whoa[7];
		fprintf(outa,"Case #%d: ",t);
		for(int i=0;i<=9;i++){
			for(int j=0;j<whoa[i];j++){
				fprintf(outa,"%d",i);
			}
		}
		fprintf(outa,"\n");
	}
	fclose(ina);
	fclose(outa);
	return 0;
}
