#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int T,r1,r2,j,k,mat1[4][4],mat2[4][4];
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		cin>>r1;
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				cin>>mat1[j][k];
			}
		}
		cin>>r2;
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				cin>>mat2[j][k];
			}
		}

		int count = 0;
		int card;
		
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				if(mat1[r1-1][j] == mat2[r2-1][k]){
					count++;
					card = mat1[r1-1][j];
				}
			}
		}
		switch(count){
			case 0:	cout<<"\nCase #"<<i<<": Volunteer cheated!";	break;
			case 1: cout<<"\nCase #"<<i<<": "<<card;				break;
			default:	cout<<"\nCase #"<<i<<": Bad magician!";		break;
		}
	}
}