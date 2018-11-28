#include<iostream>
#include<stdio.h>
FILE *fr,*fw;
using namespace std;

main(){
	
	
	int in1=0, in2=0;
	int grid1[4][4],grid2[4][4];
	int i=0,j=0,count=0,ans=0;
	int T=0,t=0;
	
	fr=fopen("in.txt","r");
	fw=fopen("out.txt","w");
	
	
	fscanf(fr,"%d",&T);
	
	while(t<T){
		
		//cout<<t<<"\n";
		count=0;
		ans=0;
		fscanf(fr,"%d",&in1);
		
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			fscanf(fr,"%d",&grid1[i][j]);
		}
				
		fscanf(fr,"%d",&in2);
		
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			fscanf(fr,"%d",&grid2[i][j]);
		}
		
		
		cout<<"Case #"<<++t<<": ";
		fprintf(fw,"Case #%d: ",t);
		
		for(i=0;i<4;i++){
			
			for(j=0;j<4;j++){
			
			if(grid1[in1-1][i]==grid2[in2-1][j]){
				count++;
				
				ans=grid1[in1-1][i];
				
			}
		}
		}
			
			if(count==1){
				cout<<ans<<"\n";
				fprintf(fw,"%d\n",ans);
			}
			
			else if(count>1){
				cout<<"Bad magician!\n";
				fprintf(fw,"Bad magician!\n");
			}
			else if(count==0){
				cout<<"Volunteer cheated!\n";
			
				fprintf(fw,"Volunteer cheated!\n");
			}
		
		
	
	}
	
	return 0;
}