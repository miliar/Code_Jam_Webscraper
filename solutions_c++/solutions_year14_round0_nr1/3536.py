#include<iostream>
#include<cmath>
#include<cstdio>
#include<fstream>
using namespace std;
int main(){
	 ifstream myfile;
	 myfile.open("data.txt");
	FILE *fp = freopen ("myfile.txt","w",stdout);
	int tc;
	myfile>>tc;
	for (int cc=0;cc<tc;cc++){
		int r1, r2, d1[5][5], d2[5][5], count=0, num=0;
		myfile>>r1;
		r1--;
		for(int row=0;row<4;row++){
			for(int col=0;col<4;col++){
				myfile>>d1[row][col];
			}
		}
		myfile>>r2;
		r2--;
		for(int row=0;row<4;row++){
			for(int col=0;col<4;col++){
				myfile>>d2[row][col];
			}
		}
		for(int f=0;f<4;f++){
			for(int s=0;s<4;s++){
			//	cout<<d1[r1][f]<<" "<<d2[r2][s]<<endl;
				if(d1[r1][f]==d2[r2][s]){
					count++;
					num=d2[r2][s];
				}
			}
		}
		if(count==0){
			printf("Case #%d: Volunteer cheated!\n", cc+1);
		}else if(count==1){
			printf("Case #%d: %d\n", cc+1, num);
		}else{
			printf("Case #%d: Bad magician!\n", cc+1);
		}
	
		
	}
	  fclose (stdout);
}
