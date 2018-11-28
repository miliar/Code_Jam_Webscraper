#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime> 



int solve(int cnum){
	
	int n;
	scanf("%d",&n);
	int a[4][4];
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++)scanf("%d",&a[i][j]);
	}
    int m;
	scanf("%d",&m);
	n--;
	m--;
	int b[4][4];
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++)scanf("%d",&b[i][j]);
	}
    int c[17]={0};
    int ans=0;
    int ac[3]={0};
    for(int i=0;i<4;i++)c[a[n][i]]++;
    for(int i=0;i<4;i++)c[b[m][i]]++;
    for(int i=0;i<17;i++){ 
    	if(c[i]==2)ans=i;
    	ac[c[i]]++;
    }
    printf("Case #%d: ",cnum);
    if(ac[2]==1)printf("%d\n",ans);
    else if(ac[2]>1)printf("Bad magician!\n");
    else if(ac[2]==0)printf("Volunteer cheated!\n");
     
	return 0;
}

int main(){
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		solve(i+1);
	}
	
	
	
	
	return 0;
}