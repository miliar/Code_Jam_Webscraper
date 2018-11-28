#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<string>
#include<math.h>
#include <algorithm>

using namespace std;

#define LL long long
#define LD long double
#define FM(i,a,b) for(int i=a;i<b;i++) //(b-a) times a ~ b-1
#define P_T "A"
#define I_T "large"
#define FILE_OPEN() char name1[50],name2[50];\
sprintf(name1, "%s-%s.in", P_T,I_T );\
sprintf(name2,"%s-%s.out" , P_T,I_T );\
freopen(name1,"r", stdin);freopen(name2, "w" ,stdout) // open file

#define D_INPUT_A(x) int x;scanf( "%d",&x)
#define D_INPUT_B(x,y) int x;int y;scanf( "%d%d",&x,&y)
#define D_INPUT_C(x,y,z) int x;int y;int z;scanf( "%d%d%d",&x,&y,&z)
#define INPUT_A(x) scanf("%d",&x)
#define INPUT_B(x,y) scanf("%d%d",&x,&y)
#define INPUT_C(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define INPUT_STR(x) scanf("%s",x)
#define OUTPUT(x) printf("Case #%d: %d\n",n+1,x)
#define OUTPUT_B(x,y) printf("Case #%d: %d %d\n",n+1,x,y)
#define OUTPUT_STR(x) printf("Case #%d: %s\n",n+1,x)
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

const LD EPS = 1e-10;
const LD PI = acos(-1.0);

int alphabet[26];
char buf[2010];
int phonenumber[10];

void count_num(char *buf, int num) {
	int i = 1;
	int temp = alphabet[buf[0] - 'A'];
	alphabet[buf[0] - 'A'] = 0;
	if (temp == 0) return;
	while (buf[i] != '\0') {
		alphabet[buf[i] - 'A'] -= temp;
		i++;
	}
	phonenumber[num] = temp;
}

void get_number() {

	count_num("ZERO", 0);
	count_num("UFOR", 4);
	count_num("XSI", 6);
	count_num("SEVEN", 7);
	count_num("FIVE", 5);
	count_num("WTO", 2);
	count_num("GEIHT", 8);
	count_num("HTREE", 3);
	count_num("ONE", 1);
	count_num("INNE", 9);
}
void print_number(){

	FM(i, 0, 10) {
		if (phonenumber[i] != -1) {
			FM(j, 0, phonenumber[i]) {
				printf("%d", i);
			}
		}
	}
	
}
int main() {
	FILE_OPEN();

	D_INPUT_A(T);
	FM(n, 0, T) {
		memset(phonenumber, -1, sizeof(phonenumber));
		memset(alphabet, 0, sizeof(alphabet));
		INPUT_STR(buf);
		int i = 0;
		while (buf[i] != '\0') {
			alphabet[buf[i] - 'A']++;
			i++;
		}
		//
		get_number();
		
		printf("Case #%d: ", n + 1);
		print_number();
		printf("\n");
	}
	
	return 0;
}
