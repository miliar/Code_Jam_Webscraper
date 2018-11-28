# include <stdio.h>
# include <stdlib.h>
# include <math.h>

int compareRows(int a[], int b[]){
	int i,j;
	int count = 0;
	int ans = -1;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(a[i]==b[j]){
				count++;
				ans = a[i];
			}
		}
	}
	if(count > 1) return -2;
	return ans;
}

int main(){
	FILE*in = fopen("A-small-attempt0.in","r");
	FILE*out = fopen("output.txt","w");
	int T,i,c,a[2];
	int arr[4][4];
	int arr2[4][4];
    int j,k,ans;

	fscanf(in,"%d",&T);
	
	for(i=1;i<=T;i++){
		for(c=0;c<2;c++){
			fscanf(in,"%d",&a[c]);
			for(j=0;j<4;j++){
				for(k=0;k<4;k++){
					if(c==0)fscanf(in,"%d",&arr[j][k]);
					else fscanf(in,"%d",&arr2[j][k]);
				}
			}
		}
		ans = compareRows(arr[a[0]-1],arr2[a[1]-1]);
		if(ans == -1)fprintf(out,"Case #%d: Volunteer Cheated!\n",i);
		else if(ans == -2)fprintf(out,"Case #%d: Bad Magician!\n",i);
		else fprintf(out,"Case #%d: %d\n",i,ans);
	
	}
	
	system("pause");
}
