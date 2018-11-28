#include<cstdio>
#include <fstream>
using namespace std;
int main(){
	int TC,row1,row2,count,tcNo=1,ans;
	bool done;
	int mat1[4][4], mat2[4][4];
	scanf("%d",&TC);
	ofstream myfile ("example.txt");
	while(TC--){
		count=0;
		done=false; 
		scanf("%d",&row1);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&mat1[i][j]);
		scanf("%d",&row2);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&mat2[i][j]);
		row1--;
		row2--;	
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(mat1[row1][i]==mat2[row2][j]){
					count++;
					ans=mat1[row1][i];
				}	
				if(count==2){
					myfile<<"Case #"<<tcNo<<": Bad magician!\n";
					done=true;
					break;
				}
			}
			if(done)
				break;
		}
		if(!done){
			if(count==0)
				myfile<<"Case #"<<tcNo<<": Volunteer cheated!\n";
			if(count==1)
				myfile<<"Case #"<<tcNo<<": "<<ans<<endl;
		}
		tcNo++;
	}
return 0;
}	
