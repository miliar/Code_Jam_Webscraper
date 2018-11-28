#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define inf 1000000000

int ar[1005];
int br[1005];
int cr[1005];

int main(){
 freopen("D-large.in","r",stdin);
 freopen("D-large.out","w",stdout);
 int tes;
 
 scanf("%d",&tes);
 for(int tcase=1;tcase<=tes;tcase++){
    int n;
	 
	 scanf("%d",&n);
	 for(int i=1;i<=n;i++){
	    double x;
		 scanf("%lf",&x);
		 ar[i] = (int)(x*1000000.0);		
	 }
	 for(int i=1;i<=n;i++){
	    double x;
		 scanf("%lf",&x);
		 br[i] = (int)(x*1000000.0);		
	 }	
	 
	 sort(ar+1,ar+n+1);
	 sort(br+1,br+n+1);
	 
	 // playing normal war
	 int ans2 = 0, idx = 0;
	 for(int i=n;i>=1;i--){
		 int mini = inf;
	    for(int j=1;j<=n;j++){
		    if(br[j] > ar[i]){
			    mini = min(mini,br[j]);		
			 }		
		 }
		 
		 if(mini == inf){
		    ans2++;
			 for(int j=1;j<=n;j++){
			    if(br[j] != -1){
					 cr[++idx] = br[j];
				    br[j] = -1;
					 break;		
				 }		
			 }		
		 }		
		 else{
		    for(int j=1;j<=n;j++){
			    if(br[j] == mini){
					 cr[++idx] = br[j];
				    br[j] = -1;
					 break;		
				 }		
			 }		
		 }
	 }
	 
	 // playing deceitful war
	 int ans1 = 0;
	 for(int i=1;i<=idx;i++){
		 int mini = inf;
	    for(int j=1;j<=n;j++){
		    if(ar[j] >	cr[i]){
			    mini = min(mini,ar[j]);		
			 }	
		 }
		 
		 if(mini == inf){
		    for(int j=1;j<=n;j++){
			    if(ar[j] != -1){
				    ar[j] = -1;
					 break;		
				 }		
			 }		
		 }
		 else{
			 ans1++;
		    for(int j=1;j<=n;j++){
			    if(ar[j] == mini){
				 	 ar[j] = -1;
					  break;	
				 }		
			 }		
		 }		
	 }
	 
	 printf("Case #%d: %d %d\n",tcase,ans1,ans2);
 }
 
 fclose(stdin);
 fclose(stdout);
// system("pause");
 return 0;	
}
