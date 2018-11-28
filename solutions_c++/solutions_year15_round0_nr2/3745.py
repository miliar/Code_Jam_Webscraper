#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main(){
	ifstream infile;
	ofstream outfile;
	infile.open("B-large.in");
	//infile.open("test.in");
	outfile.open("prob2.out");
	int rowNum;
	int size;
	infile>>rowNum;
	for(int i = 0; i< rowNum; i++){
		infile>>size;
		int minute = 0;
		vector<int> vec;
		for(int j = 0; j< size; j++){
			int pancakeNum;
			infile>>pancakeNum;
			vec.push_back(pancakeNum);
		}
		sort(vec.begin(), vec.end());//sort from min to max
		int max = vec.back();
		minute = max;//set the init value ;
		int tmpMin;
		for(int j = 1; j< max; j++){
			int sum = 0;
			for(vector<int>::iterator it = vec.begin(); it!= vec.end(); it++){
				if((*it)%j == 0){
					tmpMin = (int)(*it)/j -1;
				}else{
					tmpMin = (int)(*it)/j;
				}
				sum += tmpMin;
			}
			sum+=j;
			minute = min(minute, sum);
		}
		outfile<<"Case #"<<i+1<<": "<<minute<<endl;
	}
	return 0;
}