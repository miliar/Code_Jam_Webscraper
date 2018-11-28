#include<cstdio>
#include<set>
#include<algorithm>
using namespace std;

int x[4][4],y[4][4];

int main()
{
    int T,tc=1;
    scanf(" %d",&T);
    while(T--){
	int row;
	scanf(" %d",&row);
	int i,j;
	for(i=0;i<4;i++) for(j=0;j<4;j++) scanf(" %d",&x[i][j]);
	int row1;
	set<int> S;
	scanf(" %d",&row1);
	for(i=0;i<4;i++) for(j=0;j<4;j++){  
		scanf(" %d",&y[i][j]);
		if(i==row1-1) 
			S.insert(y[i][j]);
	}
	int match=0,ans=-1;
	for(j=0;j<4;j++) 
	{
		int ele=x[row-1][j];
		if(S.count(ele)){  match++;
		ans=ele;
		}
	}

	printf("Case #%d: ",tc++);
	if(match==1){
		printf("%d\n",ans);
	} else if(match==0) {
		printf("Volunteer cheated!\n");
	} else
		printf("Bad magician!\n");
    }
    return 0;
}
