#include<cstdio>
#include<set>

using namespace std;

int main(){
    int T, t;
    scanf("%d", &T);
    for(int t=1; t<=T; t++){
        int a1,a2,i,j;
        int c1[4][4], c2[4][4];
        scanf("%d",&a1);
        for(i=0; i<4; i++){
            for(j=0;j<4;j++){
                scanf("%d",&c1[i][j]);
            }
        }
        scanf("%d",&a2);
        for(i=0; i<4; i++){
            for(j=0;j<4;j++){
                scanf("%d",&c2[i][j]);
            }
        }
        set<int> ans;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(c1[a1-1][i] == c2[a2-1][j]){
                    ans.insert(c1[a1-1][i]);
                }
            }
        }
        if(ans.size() == 0){
            printf("Case #%d: Volunteer cheated!\n",t);
        }
        else if(ans.size() == 1){
            printf("Case #%d: %d\n",t,*(ans.begin()));
        }
        else{
            printf("Case #%d: Bad magician!\n",t);
        }
    }
	return 0;
}
