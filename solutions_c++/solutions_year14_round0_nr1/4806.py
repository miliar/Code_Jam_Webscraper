#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

bool flag[25];

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
 int tes;
 
 scanf("%d",&tes);
 for(int tcase=1;tcase<=tes;tcase++){
	 for(int i=1;i<=16;i++) flag[i] = 0;
    int n,m;
	 
	 scanf("%d",&n);
	 for(int i=1;i<=4;i++){
	    for(int j=1;j<=4;j++){
			 int x;
			 scanf("%d",&x);
		    if(i == n) flag[x] = 1;		
		 }		
	 }
	 
	 int ans = 0;
	 scanf("%d",&m);
	 for(int i=1;i<=4;i++){
	    for(int j=1;j<=4;j++){
		    int x;
			 scanf("%d",&x);
			 if(i == m && flag[x]){
			    if(ans) ans = 123;
				 else ans = x;		
			 }		
		 }		
	 }
	 
	 if(ans == 123) printf("Case #%d: Bad magician!\n",tcase);
	 else if(ans == 0) printf("Case #%d: Volunteer cheated!\n",tcase);
	 else printf("Case #%d: %d\n",tcase,ans);		
 }
 fclose(stdin);
 fclose(stdout);
// system("pause");
 return 0;	
}
