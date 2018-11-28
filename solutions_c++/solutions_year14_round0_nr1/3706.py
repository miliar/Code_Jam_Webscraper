#include <iostream>
#include <fstream>

using namespace std;

int getCardNo(int arr1[], int arr2[]){
	int res,n=0;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(arr1[i]==arr2[j]){
				res=arr1[i];
				n++;
				if(n>=2)
					return -1;
			}
		}
	}

	if(n==0)
		return -2;
	else
		return res;
}

int main(){
	ifstream inp("mtinput.txt");
	ofstream out("mtoutput.txt");

	int t,cno=0,a1,a2,res;
	int arr1[4][4],arr2[4][4];
	inp>>t;

	for(int i=0;i<t;i++){
		cno++;

		inp>>a1;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				inp>>arr1[j][k];

		inp>>a2;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				inp>>arr2[j][k];

		res=getCardNo(arr1[a1-1], arr2[a2-1]);

		if(res==-1){
			out<<"Case #"<<cno<<": Bad magician!\n";
		}

		else if(res==-2){
			out<<"Case #"<<cno<<": Volunteer cheated!\n";
		}

		else{
			out<<"Case #"<<cno<<": "<<res<<"\n";
		}

	}
}