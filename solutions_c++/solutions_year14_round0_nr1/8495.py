#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iomanip>

using namespace std;

int T, ans1, card1[4][4],ans2, card2[4][4], ans=0;

template<class out_type, class in_value>
out_type convert(const in_value &t) {
	stringstream stream;
	stream << t;
	out_type result;
	stream >> result;
	return result;
}


int ff(){
	int num=0;
	int x1=ans1-1, x2=ans2-1;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(card1[x1][i]==card2[x2][j]){
				ans=card1[x1][i];
				num++;
				break;
			}
		}
	}
	return num;
}

int main() {
//	freopen("A.in","r",stdin);
//	freopen("out.txt","w",stdout);
	int y;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d",&ans1);
		for(int i=0;i<4;i++){
			scanf("%d%d%d%d",&card1[i][0],&card1[i][1],&card1[i][2],&card1[i][3]);
		}
		scanf("%d",&ans2);
		for(int i=0;i<4;i++){
			scanf("%d%d%d%d",&card2[i][0],&card2[i][1],&card2[i][2],&card2[i][3]);
		}

		y=ff();
		printf("Case #%d: ",t);
		if(y>1){
			printf("Bad magician!\n");
		}else if(y==0){
			printf("Volunteer cheated!\n");
		}else{
			printf("%d\n",ans);
		}
	}

	return 0;
}