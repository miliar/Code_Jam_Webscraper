#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

ifstream fin("a.txt");
ofstream fout("ans.txt");

void main(){
	int total,row,temp=0,k=1,count,var=0,arr[4]={0};
	fin>>total;
	while(k<=total){
		count=0;
		fin>>row;
		row=row-1;
		for(int i=0;i<16;i++){
			fin>>temp;
			if( i >= (4*row) && i<(4*(row+1))){
				arr[i-(4*row)]=temp;
			}
		}
		fin>>row;
		row=row-1;
		for(int i=0;i<16;i++){
			fin>>temp;
			if( i >=(4*row) && i < (4*(row+1)) ){
				if((temp == arr[0]) || (temp == arr[1]) || (temp == arr[2]) || (temp == arr[3]) ){
					count++;
					var=temp;
				}
			}
		}
		if(count==0){
			fout<<"Case #"<<k<<": Volunteer cheated!\n";	
		}
		else if(count==1){
			fout<<"Case #"<<k<<": "<<var<<"\n";	
		}
		else{
			fout<<"Case #"<<k<<": Bad magician!\n";	
		}
		k++;
	}
}

