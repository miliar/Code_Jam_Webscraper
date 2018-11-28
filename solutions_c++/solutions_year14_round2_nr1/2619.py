#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#define INF 2000000000
#define x first
#define y second
using namespace std;

int T,N;
char str[105][105];
char strmain[105];
int lastpoint[105];
int mlenth;

int ab(int x){
	if(x<0)
		return -x;
	return x;
}

int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++) {
		memset(strmain,0,sizeof strmain);
		memset(lastpoint,0,sizeof lastpoint);
		mlenth = 0;
		scanf("%d",&N);
		int Move = 0;
		bool Lose = false;
		for(int i=0;i<N;i++){
			scanf("%s",str[i]);
			int k = 0;
			if(i==0) {
				for(int j=0;j<str[i][j]!='\0';j++){
					if(str[i][j]!=str[i][j+1]) {
						strmain[mlenth] = str[i][j];
						mlenth++;
						//printf("%c",strmain[mlenth-1]);
					}
				}
				//printf("\n");
			}
			else {
				for(int j=0;str[i][j]!='\0';j++) {
					if(str[i][j]!=str[i][j-1]){
						if(str[i][j]==strmain[k]){
							k++;
						}
						else{
							Lose = true;
							break;
						}
					}
				}
				if(k!=mlenth){
					Lose = true;
				}
			}
		}

		if(Lose==1) {
			printf("Case #%d: Fegla Won\n",Case);
		}
		else {
			int End = 0;
			while(End<N) {
				vector<int> Med;
				for(int i=0;i<N;i++) {
					int k = 1;
					while(str[i][lastpoint[i]]!='\0') {
						//printf("%d %c\n",i,str[i][lastpoint[i]]);
						if(str[i][lastpoint[i]]!=str[i][lastpoint[i]+1]){
							lastpoint[i]++;
							if(str[i][lastpoint[i]]=='\0')
								End++;
							break;
						}
						k++;
						lastpoint[i]++;
						if(str[i][lastpoint[i]]=='\0')
							End++;
					}
					//system("pause");
					Med.push_back(k);
				}
				sort(Med.begin(),Med.end());
				for(int i=0;i<Med.size();i++) {
					//printf("Med %d\n",Med[i]);
					Move += ab(Med[i]-Med[Med.size()/2]);
				}
			}
			printf("Case #%d: %d\n",Case,Move);
		}
	}
}
