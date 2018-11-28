#include<iostream>
#include<fstream>

using namespace std;

int row1, row2, result, testcases, trash, count, answer;
int arr1[5];
int arr2[5];


void get1(ifstream &in, int row){
	for(int i=1; i<=4*(row-1); i++){in>>trash;}
	for(int i=1; i<=4; i++){in>>arr1[i];}
	for(int i=4*row+1; i<=16; i++){in>>trash;}
};

void get2(ifstream &in, int row){
	for(int i=1; i<=4*(row-1); i++){in>>trash;}
	for(int i=1; i<=4; i++){in>>arr2[i];}
	for(int i=4*row+1; i<=16; i++){in>>trash;}
};

int comp(int A1[], int A2[]){
	count=0;
	answer=0;
	for(int i=1; i<=4; i++){
	for(int j=1; j<=4; j++){
		if(A1[i]==A2[j]){
		count++; 
		answer=A1[i];
		}
	}
	}
	return count;
		
};

void printarr(int A[]){
	cout<<endl;
	for(int i=1; i<=4; i++){
		cout<<A[i]<<" ";
	}
	cout<<endl;
}

int main(){
	ifstream infile("A-small-attempt0.in");
	ofstream outfile;
	outfile.open("2.txt");
	
infile>>testcases;
for(int t=1; t<=testcases; t++){
	infile>>row1;
	get1(infile, row1);
	infile>>row2;
	get2(infile, row2);
	//printarr(arr1);
	//printarr(arr2);
	result=comp(arr1, arr2);
	if(result==0){outfile<<"Case #"<<t<<": "<<"Volunteer cheated!";}
	if(result==1){outfile<<"Case #"<<t<<": "<<answer;}
	if(result>1){outfile<<"Case #"<<t<<": "<<"Bad magician!";}
	outfile<<endl;
	
}
outfile.close();
return 0;
}

