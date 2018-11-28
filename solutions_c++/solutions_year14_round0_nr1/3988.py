#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
	int a[5][5];
	int b[5][5];
	
	int t,i,a1,a2,j,k,c,num;
	ifstream fin("A-small-attempt0.in");
	ofstream fout("magicout.txt");
	
	fin.seekg(0);
	
	fin >> t;
	//cout<<"1111";
	
	for(i = 1; i <= t; i++) {
		
		c=0;
		
		fin >> a1;
		//cout<<"2222";
		
		for(j = 1; j <= 4; j++) {
			for(k = 1; k <= 4; k++) {
				
				fin >> a[j][k];	
				//cout<<"3333";
			}
		
		}
		
		fin >> a2;
		//cout<<"4444";
		
		for(j = 1; j <= 4; j++) {
			for(k = 1; k <= 4; k++) {
				
				fin >> b[j][k];
				//cout<<"5555";	
			}
		
		}
		
		
		for(j = 1; j <= 4; j++) {
			for(k = 1; k <= 4; k++){
					
				if(a[a1][j] == b[a2][k]){
					
					c++;
					num = a[a1][j];
					//cout<<"6666";
					
				}
			}
			
			
		
		}
		
		
		//cout<<"7777";
		
		if(c == 0) {
			fout <<"Case #"<<i<<": Volunteer cheated!\n";
		}else if(c == 1){
			fout << "Case #"<<i<<": "<<num<<"\n";
		}else{
			fout << "Case #"<<i<<": Bad magician!\n";
		}
	
	}
	
	fin.close();
	fout.close();
	
	return 0;
}
