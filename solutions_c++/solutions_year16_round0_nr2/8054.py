#include<iostream>
#include<fstream>

using namespace std;

int main(){
	int T;
	ifstream fin("B-large.in");
	ofstream fout("out.txt");
	fin>>T;
	int count;
	string cakes;
	for(int i = 0; i<T; i++){
		fin>>cakes;
		count=0;
		while(true){
			int prefix=0, end = cakes.size()-1;
			while(cakes[end]=='+'){
				end--;
				if(end == -1){
					fout<<"Case #"<<i+1<<": "<<count<<endl;
					break;
				}
			}
			if(end == -1)break;
			char firstchar = cakes[0];
			while(cakes[prefix]==cakes[0]){
				prefix++;
				if(prefix == cakes.size()){
					fout<<"Case #"<<i+1<<": "<<count+1<<endl;
					break;
				}
			}
			if(prefix == cakes.size())break;
			if(cakes[0] == '+'){
				count+=1;
				for(int j = 0;j<prefix;j++){
					cakes[j] = '-';
				}
			}
			else{
				count++;
				
					string tmp = cakes;
				for(int j = 0; j<=end;j++){
					cakes[j] = tmp[end-j]=='+'?'-':'+';	
					//fout<<cakes<<endl;
					//fout<<tmp<<endl;
                    				
				}
				
			}
			
		}
	}
	//system("pause");
	return 0;
	
}