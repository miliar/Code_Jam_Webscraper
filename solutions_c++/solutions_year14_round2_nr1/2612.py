#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define N 105

#define abs(a) ((a)>0?(a):(-(a)))
#define min(a,b) ((a)<(b)?(a):(b))
char s[N][N];

int num[N][N];
int l1;

char str[N];
void init(){
	memset(num, 0, sizeof(num));
}

void ana(char *s){
	int len = strlen(s);
	int j = 0;
	str[0] = s[0];
	for(int i = 1; i < len; i++){
		if(s[i] != s[i - 1]){
			str[++j] = s[i];
		}
	}
	str[++j] = '\0';
	l1 = j;
}

bool could(char *s, int id){
	int len = strlen(s);
	if(s[0] != str[0])
		return false;
	num[id][0]++;
	int j = 0;
	for(int i = 1; i < len ; i++){
		if(s[i] != s[i - 1]){
			if(s[i] != str[j + 1])
				return false;
			else{
				j++;
				num[id][j]++;
			}
		}
		else{
			num[id][j]++;
		}
	}
	if(j < l1 - 1)
		return false;
	return true;
}
int main(){
	int t, n;
	scanf("%d", &t);
	int icase = 1;
	while(t--){
		init();
		scanf("%d", &n);
		for(int i = 0; i < n; i++){
			scanf("%s", s[i]);
		}
		printf("Case #%d: ", icase++);
		ana(s[0]);
	//	printf("str=%s\n", str);
		bool flag = true;
		for(int i = 0; i < n; i++){
			if(!could(s[i], i)){
			//	printf("%d %s\n", i, s[i]);
				flag = false;
				break;
			}
		}
		if(!flag){
			printf("Fegla Won\n");
			continue;
		}
		int ans = 0;
		for(int i = 0; i < l1; i++){
			double sum = 0;
			for(int j = 0; j < n; j++){
				sum += num[j][i];
			}
			sum /= n;
			int t1 = (int)(sum += 0.5);
			int te[2] = {0, 0};
			for(int k = (int)(sum); k <= (int)(sum + 1); k++){
				for(int j = 0; j < n; j++){
					te[k - (int)(sum)] += abs(k - num[j][i]);
				}
			}
			ans += min(te[0], te[1]);
		}
		printf("%d\n", ans);
	}
	return 0;
}
