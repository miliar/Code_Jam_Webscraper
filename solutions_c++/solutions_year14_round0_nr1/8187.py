#include<iostream>
#include<fstream>
using namespace std;

int main(){

	ifstream fin;
  	fin.open ("input.txt");
	
	ofstream fout;
  	fout.open ("output.txt");
	
	int t;
	fin>>t;
	
	int result;
	
	for(int p=1; p<=t; p++){
		
		int temp;
		int result1,result2;
		
		fin>>result1;
		
		int arr1[4][4];
		
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				fin >> arr1[i][j];
			}		
		}

		fin>>result2;
		
		int arr2[4][4];
		
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				fin >> arr2[i][j];
			}
		}
		
		int show[27] = {0};
		
		bool first_hit = false;
		bool second_hit = false;
		bool third_hit = true;
		int hit;
		int data;
		
		for(int i=0;i<4;i++){
			show[arr1[result1-1][i]]++;
		}		
		
		for(int i=1;i<17;i++)
		{	
			cout<<show[i]<<" ";
		}
		cout<<endl;
		
		for(int i=0;i<4;i++){
			data = show[arr2[result2-1][i]];
			cout<<arr2[result2-1][i]<<" ";
			if(data == 0){
			}else{
				third_hit = false;
				if(first_hit == true && second_hit != true){
					second_hit = true;
				}else{	
					hit = arr2[result2-1][i];
					first_hit = true;
				}
			}
		}
		cout<<endl;
		
		if(third_hit){
			fout<<"Case #"<<p<<": Volunteer cheated!"<<endl;
		}else if(second_hit){
			fout<<"Case #"<<p<<": Bad magician!"<<endl;
		}else if(first_hit){
			fout<<"Case #"<<p<<": "<<hit<<endl;
		}		
	}
	
}
