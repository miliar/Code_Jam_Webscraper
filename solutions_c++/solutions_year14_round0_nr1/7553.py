#include<iostream>
using namespace std;
int main(){
	int testcases;
	int r1;
	int r2;
	int mat1[4][4];
	int mat2[4][4];
	int common=0;
	int sum_common=0;

	cin>>testcases;
	
	for(int kcounter=1;kcounter<=testcases;kcounter++)
	{
		common=0;
		sum_common=0;

		cin>>r1;
		for(int icounter=0;icounter<4;icounter++)
		{
			for(int jcounter=0;jcounter<4;jcounter++)
				cin>>mat1[icounter][jcounter];
		}

		cin>>r2;
		
		for(int icounter=0;icounter<4;icounter++)
		{
			for(int jcounter=0;jcounter<4;jcounter++)
				cin>>mat2[icounter][jcounter];
		}

		//get the common contents between the two rows
		for(int icounter=0;icounter<4;icounter++)
		{
			for(int jcounter=0;jcounter<4;jcounter++)
				if(mat1[r1-1][icounter]-mat2[r2-1][jcounter]==0)
				{
					common=mat1[r1-1][icounter];
					sum_common+=1;
				}
		}

		if(sum_common==1){ //that means we have proper solution
			cout<<"Case #"<<kcounter<<": "<<common<<endl;
		}
		else if(sum_common>1){
			cout<<"Case #"<<kcounter<<": Bad magician!"<<endl;
		}
		else if(sum_common==0){
			cout<<"Case #"<<kcounter<<": Volunteer cheated!"<<endl;
		}
	}
	return 0;
}
