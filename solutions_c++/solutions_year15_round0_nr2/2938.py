#include<bits/stdc++.h>
using namespace std;
int main(){
    FILE *fp,*fp1;
    fp=fopen("B-large.in","r");
    fp1=fopen("output_2_large.txt","w");
	int t,j;
	fscanf(fp,"%d",&t);
	for(j=1;j<=t;j++){
		int high1=0,n,a[10000];
		fscanf(fp,"%d",&n);
		for(int i=1;i<=n;i++){
			fscanf(fp,"%d",&a[i]);
			if(high1<a[i])
                high1=a[i];
		}
		int res=high1;
		for(int i=1;i<=high1;i++){
			int temp=0,high2=0;
			for(int k=1;k<=n;k++){
				if(a[k]>i){
					temp +=(a[k]/i);
					if(a[k]%i==0)
                        temp--;
                    if(high2<i)
                        high2=i;
				}
				else{
                    if(high2<a[k])
                        high2=a[k];
                }
			}
			temp=temp+high2;
			if(temp<res)
                res=temp;
		}
		fprintf(fp1,"Case #%d: %d\n",j,res);
	}
	return 0;
}
