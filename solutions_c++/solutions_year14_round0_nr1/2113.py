#include <iostream>
#include <string.h>

using namespace std;

bool mark[17];
int arr1[5][5], arr2[5][5];

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t, r1, r2, no;
	int ans;
	bool multi;
	no = 1;
	scanf("%d",&t);
	while(t--){
		memset(mark,false,sizeof(mark));
		scanf("%d",&r1);
		for(int i = 0; i < 4; i++)
		    for(int j = 0; j < 4; j++)
		        scanf("%d", &arr1[i][j]);
		        
		for(int j = 0; j < 4; j++)
		    mark[arr1[r1-1][j]] = true;
		    
		scanf("%d",&r2);
		for(int i = 0; i < 4; i++)
		    for(int j = 0; j < 4; j++)
		        scanf("%d", &arr2[i][j]);
		
		ans = -1;
		multi = false;
		for(int j = 0; j < 4; j++){
			if(mark[arr2[r2-1][j]]){
				if(ans == -1)
				    ans = arr2[r2-1][j];
				else
				    multi = true;
			}
		}
		if(ans != -1 && !multi)
		    printf("Case #%d: %d\n", no, ans);
		else if(ans != -1 && multi)
		    printf("Case #%d: Bad magician!\n", no);
		else
		    printf("Case #%d: Volunteer cheated!\n", no);
		no++;
	}
	return 0;
}
