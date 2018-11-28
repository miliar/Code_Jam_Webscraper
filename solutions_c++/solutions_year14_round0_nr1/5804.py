#include <stdio.h>
#include <algorithm>
#include <vector>
void recv(FILE *fp,int *result){
	int i, j;
	int r;
	fscanf(fp,"%d", &r);
	for (i = 1; i <= 4; i++)
	for (j = 0; j < 4; j++)
	if (i == r)
		fscanf(fp,"%d", &result[j]);
	else
		fscanf(fp,"%*d");

}
int main(){
	FILE* fp = fopen("practice.in", "r");
	FILE* fp2 = fopen("practice.out", "w");

	int t;
	fscanf(fp,"%d", &t);
	int i, j, k;
	for (i = 1; i <= t; i++){
		int a[4];
		int b[4];
		recv(fp,a);
		recv(fp,b);
		std::vector<int> c(4);
		std::sort(a, a + 4);
		std::sort(b, b + 4);
		auto it=std::set_intersection(a, a + 4, b, b + 4, c.begin());
		c.resize(it - c.begin());

		for (auto it = c.begin(); it != c.end(); it++)
			printf("%d ", *it);

		if (c.size() == 1)
			fprintf(fp2, "Case #%d: %d\n", i, c[0]);
		else if(c.size()>1)
			fprintf(fp2, "Case #%d: Bad magician!\n", i);
		else
			fprintf(fp2, "Case #%d: Volunteer cheated!\n", i);
	}

}