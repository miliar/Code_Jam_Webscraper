#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;

int main(){
	ifstream myin;
 	myin.open("A-small-attempt1.in");
	ofstream myout;
	myout.open("output.out");
	int t,a1,a2,count,z,z1;
	z1=0;
	int arr1[4][4],arr2[4][4];
	myin >> t;;
	while(t--){
		z1++;
		count=0;
		myin >> a1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				myin >> arr1[i][j];
		}
		myin >>a2;;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				myin>> arr2[i][j];
		}
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(arr1[a1-1][i]==arr2[a2-1][j]){
					count++;
					z=arr1[a1-1][i];
				}
			}
		}
		if(count==0)
			myout<<"Case #"<<z1<<": Volunteer cheated!\n";
		else if(count==1)
			myout<<"Case #"<<z1<<": "<<z<<"\n";
		else
			myout<<"Case #"<<z1<<": Bad magician!\n";
	}
	myin.close();
	myout.close();
	return 0;
}