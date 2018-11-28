#include<iostream>
#include<fstream>
#include<sstream>
using namespace std;
bool checker(bool check[10]);

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	
	fin >> T;
	
	if(T >= 1 && T <= 100)
	{
		
		for(int l = 0; l < T; l++){
			
			int N;
			fin >> N;
			
			
			
			if(N == 0){
				fout << "Case #" << l+1 << ": INSOMNIA\n"; 
			}
			else{
			
				if(N >= 0 && N <= 1000000){
					
					int nTemp;
					int i = 1;
					bool check[10] = {false,false,false,false,false,false,false,false,false,false};
					
					while(!checker(check)){
						
						nTemp = i * N;
						while(nTemp != 0){
							int temp = nTemp % 10;
							check[temp] = true;
							nTemp = nTemp/10;
						}
						i++;
					} 
					fout << "Case #" << l+1 << ": " << (i-1) * N << "\n";
				}
			
			}
		}
	
	}
}

bool checker(bool check[10]){
	
	for(int i =0; i < 10 ; i++){
		if(check[i] == false){
			return false;
		}
	}
	return true;
	
}
