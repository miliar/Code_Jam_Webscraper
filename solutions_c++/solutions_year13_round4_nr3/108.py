#include <stdio.h>
#include <string.h>
int n,print[2001],A[2001],B[2001],right[2001],save[2001],left[2001];
void pro(){
	int i,j,max,k;
	for(i=1;i<=n;i++){
		max=0;
		save[n]=0;
		for(j=n-1;j>=0;j--){
			save[j]=save[j+1];
			if(print[j]!=0 && save[j]<B[j])
				save[j]=B[j];
		}
		for(j=0;j<n;j++){
			if(print[j]!=0 && A[j]>max)
				max=A[j];
			if(print[j]!=0) continue;
			if(max+1==A[j] && save[j]+1==B[j] && right[A[j]]==j && left[B[j]]==j){
				print[j]=i;
				right[A[j]]=0;
				left[B[j]]=0x7fffffff;
				for(k=0;k<n;k++){
					if(print[k]!=0) continue;
					if(right[A[k]]<k)
						right[A[k]]=k;
					if(left[B[k]]>k)
						left[B[k]]=k;
				}
				break;
			}
		}
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test,testt,i;
	scanf("%d",&testt);
	for(test=1;test<=testt;test++){
		scanf("%d",&n);
		memset(print,0,sizeof(print));
		memset(right,0,sizeof(right));
		for(i=1;i<=n;i++)
			left[i]=0x7fffffff;
		for(i=0;i<n;i++){
			scanf("%d",&A[i]);
			if(right[A[i]]<i)
				right[A[i]]=i;
		}
		for(i=0;i<n;i++){
			scanf("%d",&B[i]);
			if(left[B[i]]>i)
				left[B[i]]=i;
		}
		pro();
		printf("Case #%d: ",test);
		for(i=0;i<n;i++)
			printf("%d ",print[i]);
		printf("\n");
	}
	return 0;
}
