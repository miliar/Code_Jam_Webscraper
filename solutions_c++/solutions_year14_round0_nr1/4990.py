#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>

using namespace std;

int 		first[4][4],f;
int 		second[4][4],s;
int			t;
int			tu[4], cnt;
bool 		visit[4];

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tt=1;tt<=test;tt++){
		scanf("%d",&f);
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				scanf("%d",&first[i][j]);
			}
		}
		scanf("%d",&s);
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				scanf("%d",&second[i][j]);
			}
		}

		f--;
		s--;

		cnt=0;

		for(int i=0;i<4;i++){
			tu[cnt++] = first[f][i];
		}
		int rez = -1;
		int br = 0;
		for(int i=0;i<cnt;i++){
			for(int j=0;j<4;j++){
				if(tu[i] == second[s][j]){
					rez = tu[i];
					br++;
					break;
				}
			}
		}
		/*for (int i = 0; i < tu.size(); ++i)
		{
			/* code 
			cout << tu[i] << endl;
		}*/

		if(br==1){
			printf("Case #%d: %d\n",tt,rez);
		}else if(br > 1){
			printf("Case #%d: Bad magician!\n",tt);
		}else {
			printf("Case #%d: Volunteer cheated!\n", tt);
		}

	}
	return 0;
}