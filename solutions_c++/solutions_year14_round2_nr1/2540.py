#include<cstdio>
#include<cstring>
#include<Algorithm>
#include<cmath>

using namespace std;

class str{
public:
	char ch;
	int len;
};

int n;
char tmpstr[100];
str array[100][100];
int arraylen[100];

int process(){
	int i, j, flag;
	flag = arraylen[0];
	for(i=0;i<n;i++){
		if(flag != arraylen[i]){
			return -1;
		}
	}

	int ans = 0;
	for(j=0;j<arraylen[0];j++){
		int tot = 0;
		char cf = array[0][j].ch;
		for(i=0;i<n;i++){
			if(cf != array[i][j].ch) return -1;
			tot += array[i][j].len;
		}

		double avg = round( (double)tot / (double)n );

		for(i=0;i<n;i++){
			ans = ans + (int)abs( double( (int)avg - array[i][j].len ) );
		}
	}
	return ans;
}

int main(void){
	int t, T;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			int cnt = 0;
			scanf("%s",tmpstr);
			for(int j=0;j<strlen(tmpstr);j++){
				if(j == 0){
					array[i][cnt].ch = tmpstr[j];
					array[i][cnt].len = 1;
				}
				else if(array[i][cnt].ch != tmpstr[j]){
					cnt = cnt + 1;
					array[i][cnt].ch = tmpstr[j];
					array[i][cnt].len = 1;
				}
				else{
					array[i][cnt].len++;
				}
			}
			arraylen[i] = cnt + 1;
		}
		int ans = process();
		printf("Case #%d: ", t);
		if(ans == -1){
			printf("Fegla Won\n");
		}
		else{
			printf("%d\n",ans);
		}
	}
}
