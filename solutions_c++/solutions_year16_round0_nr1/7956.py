#include<iostream>
#include<cstring>
#include<iomanip> 
#include<sstream>
#include<fstream>
using namespace std;

int main(){
    ofstream fout("output.txt");
    ifstream fin("A-large.in");
	int T,TT;
	fin>>T;
	TT = T;
	int* nums = new int[T];
	int map[10];


	string result;
	while(T--){
        fin>>nums[TT-T-1];
		int cur = nums[TT-T-1];
		cur = abs(cur);
		memset(map,0,sizeof(map));
		if(cur == 0){
			fout<<"Case #"<<TT-T<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		while(true){	
            ostringstream convert;   // stream used for the conversion	
			convert<<cur;//insert the textual representation of 'Number' in the characters in the stream
			result = convert.str();
			//cout<<result<<endl;
			for(int i = 0; i<result.size();i++){
				map[result[i]-48] ++;
				//cout<<map[result[i]-48]<<endl;
			}
			if(map[0]>0&&
			map[1]>0&&
			map[2]>0&&
			map[3]>0&&
			map[4]>0&&
			map[5]>0&&
			map[6]>0&&
			map[7]>0&&
			map[8]>0&&
			map[9]>0
			)
			{
				fout<<"Case #"<<TT-T<<": "<<result<<endl;
				break;
			}
			cur+=nums[TT-T-1];
		}
		
	}

	return 0;
}