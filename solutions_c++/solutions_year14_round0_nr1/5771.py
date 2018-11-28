#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int s[5][5],p[5][5];
int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
		int n1,n2;
        scanf("%d",&n1);
		for(int i=0;i<4;i++)
			for(size_t j = 0; j < 4; ++j)
				scanf("%d",&s[i][j]);
        scanf("%d",&n2);
		for(int i=0;i<4;i++)
			for(size_t j = 0; j < 4; ++j)
				scanf("%d",&p[i][j]);
		int k=0,ans;
		for(int i=0;i<4;i++)
			for(size_t j = 0; j < 4; ++j)
				if(s[n1-1][i]==p[n2-1][j])
				{
					k++;
					ans=s[n1-1][i];
				}
		
		if(k==1)
        	printf("Case #%d: %d\n", tt, ans);
		else
        	printf("Case #%d: %s\n", tt, k>1?"Bad magician!":"Volunteer cheated!");
    }
    return 0;
}

