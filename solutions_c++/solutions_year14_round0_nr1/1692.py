#include <stdio.h>
#include <map>

using namespace std;
int mat1[5][5];
int mat2[5][5];
int row1,row2;
int T;
map<int, int> m;

int main(){
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++){
		scanf("%d",&row1);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				scanf("%d",&mat1[i][j]);
			}
		}
		scanf("%d",&row2);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				scanf("%d",&mat2[i][j]);
			}
		}
		m.clear();
		for(int j=1;j<=4;j++){
			m[mat1[row1][j]] = 0;
		}
		for(int j=1;j<=4;j++){
			if(m.find(mat2[row2][j])!=m.end()){
				m[mat2[row2][j]]++;
			}
		}
		int c = 0;
		int n;
		for(auto &s : m){
			if(s.second==1){
				c++;
				n = s.first;
			}
		}
		if(c==0){
			printf("Case #%d: Volunteer cheated!\n",Case);
		}
		else if(c==1){
			printf("Case #%d: %d\n",Case,n);
		}
		else {
			printf("Case #%d: Bad magician!\n",Case);
		}
	}
}

