#include<iostream>
#include<fstream>
#include<sstream>
#include<cstring>
#include<vector>
#include<unordered_map>

bool dfs(const std::vector<std::vector<int> > &matrix, const std::string &str, 
		 std::vector<int> &record, int startIndex, int target,
		 std::unordered_map<char, int> &map){
	for(int index=startIndex;index<str.size();++index){
		if(index==startIndex) record[index]=map[str[startIndex]];	//int, 1-4
		else{
			int m_ind1=record[index-1]>=0?record[index-1]:record[index-1]*-1;
			int m_ind2=map[str[index]];
			record[index]=record[index-1]>=0?matrix[m_ind1][m_ind2]:
						  matrix[m_ind1][m_ind2]*-1;					//translated
		}
		if(record[index]==target&&target==4&&index==str.size()-1)  return true;
		if(record[index]==target&&target==4&&index<str.size())	continue;
		if(record[index]==target)
			return dfs(matrix, str, record, index+1,target+1, map);
	}
	return false;
}
int main(){
	//---------------------
	//	initialize matrix
	//---------------------
	std::vector<std::vector<int> > results;
	int arr0[]={0,0,0,0,0};
	int arr1[]={0,1,2,3,4};
	int arr2[]={0,2,-1,4,-3};
	int arr3[]={0,3,-4,-1,2};
	int arr4[]={0,4,3,-2,-1};
	results.push_back(std::vector<int>(arr0,arr0+sizeof(arr0)/sizeof(int)));
	results.push_back(std::vector<int>(arr1,arr1+sizeof(arr1)/sizeof(int)));
	results.push_back(std::vector<int>(arr2,arr2+sizeof(arr2)/sizeof(int)));
	results.push_back(std::vector<int>(arr3,arr3+sizeof(arr3)/sizeof(int)));
	results.push_back(std::vector<int>(arr4,arr4+sizeof(arr4)/sizeof(int)));
	//---------------------
	//	start
	//---------------------
	std::ifstream input;
	input.open("3_input.txt");
	if(!input.is_open()){std::cout<<"error\n"; return 0;}
	int testCases=-1;
	input>>testCases;
	int ll, xx,size;
	std::string str;
	std::unordered_map<char, int> inds({{'1',1},{'i',2},{'j',3},{'k',4}});
	for(int ii=1;ii<=testCases;++ii){
		input>>ll>>xx>>str;
		std::stringstream ss;
		for(int cp=0;cp<xx;++cp) ss<<str;
		str=ss.str();
		size=ll*xx;
		if(size<3){	std::cout<<"Case #"<<ii<<": NO"<<std::endl;
		}else{
			std::vector<int> record(size,0);
			bool found=dfs(results,str, record, 0, 2, inds);
			if(!found)  std::cout<<"Case #"<<ii<<": NO"<<std::endl;
			else std::cout<<"Case #"<<ii<<": YES"<<std::endl;
		}
		
	}
	return 0;
}
		
		
		
		
		
		
		
		
		
		
		
		
		
		