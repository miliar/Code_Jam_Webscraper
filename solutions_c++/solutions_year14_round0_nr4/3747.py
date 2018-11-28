#include <cstdio>
#include <string>
using namespace std;

void input(double n1[1010], int t){
	for (int j = 0; j < t; ++j)
		scanf("%lf", &n1[j]);
}
void output(double n1[1010], int t){
	for (int j = 0; j < t; ++j)
		printf("%lf ", n1[j]);
	putchar('\n');
}
void myCopy(double n1[1010], double n2[1010], int t){
	for (int j = 0; j < t; ++j)
		n2[j] = n1[j];
}
int l_gr(double k[1010], double v, int t){
	for(int j = 0; j < t; ++j)
		if(k[j] > v)
			return j;
	return -1;
}

int myCmp(const void *x, const void *y)
{
  double xx = *(double*)x, yy = *(double*)y;
  if (xx < yy) return -1;
  if (xx > yy) return  1;
  return 0;
}

int main(){
	string sample_i {"sample"};
	string small_i {"D-small-attempt0"};
	string large_i {"D-large"};
	freopen((large_i+".in").c_str(), "r", stdin);
	freopen((large_i+".out").c_str(), "w", stdout);
	int N,t;
	scanf("%6d", &N);
	double n1[1010], n2[1010],
		  k1[1010], k2[1010];
	int index1, maxk, mink, naow, naod;
	for(int i = 1; i <= N; ++i){
		mink = naow = naod = 0;
		scanf("%d", &t);
		maxk = t-1;
		input(n1,t);
		input(k1,t);
		qsort(n1, t, sizeof(n1[0]), myCmp);
		qsort(k1, t, sizeof(k1[0]), myCmp);
		//output(n1, t);
		//output(k1, t);
		myCopy(n1, n2, t);
		myCopy(k1, k2, t);
		for(int j = 0; j < t; ++j){
			index1 = l_gr(k1, n1[j], t);
			//printf("%d\n", index1);
			if(index1 == -1){
				k1[mink] = 0; mink++;
				naow++;
			}
			else
				k1[index1] = 0;
			n1[j] = 0;
		}
		mink = 0;
		for(int j = 0; j < t; ++j){
			if(n2[j] < k2[mink]){
				k2[maxk] = 0; maxk--;
			}
			else{
				naod++;
				k2[mink] = 0; mink++;
			}
			n2[j] = 0;
		}
		printf("Case #%d: %d %d\n", i, naod, naow);
	}
	return 0;
}
