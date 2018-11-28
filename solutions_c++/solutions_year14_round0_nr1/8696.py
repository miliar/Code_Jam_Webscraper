#include <iostream>
#include <fstream>

using namespace std;
int  main(){
	int num,***arrangement,answers[2],check[2][4],index,count;
	ifstream fin("A-small-attempt1.in");
	ofstream fout("output.txt");
	arrangement=new int **[2];
	for(int i=0;i<2;i++){
		arrangement[i]=new int *[4];
		for(int j=0;j<4;j++){
			arrangement[i][j]=new int [4];
		}
	}
	fin>>num;
	if(num<=100 && num>0){
	for(int l=0;l<num;l++){	
		count=0;
		for(int i=0;i<2;i++){
			fin>>answers[i];
			for(int j=0;j<4;j++){
				for(int k=0;k<4;k++){
					fin>>arrangement[i][j][k];
					if(j==answers[i]-1)
						check[i][k]=arrangement[i][j][k];
				}
			}
		}
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				if(check[0][i]==check[1][j])
				{
					count++;
					index=check[0][i];
				}
			}
			if(count>1)
				fout<<"Case #"<<l+1<<": "<<" Bad magician! \n";
			else if(count==0)
				fout<<"Case #"<<l+1<<": "<<" Volunteer cheated! \n";
			else if(count==1)
				fout<<"Case #"<<l+1<<": "<<index<<endl;
	}
	}
	system("pause");
	return 0;
}