#include <algorithm>
#include <iostream>
#include <string>
#include <math.h>
#include <vector>
#include <fstream>

using namespace std;

struct fractiles {
	std::vector<string> initial;
	std::vector<string> final; 
	int index;
};

struct pairs
{
	std::vector<long> values;
};

std::vector<string> generateAllStrings(long len){
	string temp = "";
	std::vector<string> result;
	for (int i = 0; i < len; ++i)
		temp = temp + '0';
	

	for (int i = 0; i < len; ++i)
	{
		string another = temp;
		for (int j = 1; j <= i; ++j)
		{
			another[another.length()-j] = '1';
		}
		do
    	{	
       		result.push_back(another);
    	}
    	while (std::next_permutation(another.begin(), another.end()));
	}
	temp = "";
	for (int i = 0; i < len; ++i)
		temp = temp + '1';
	result.push_back(temp);	
	return result;
}

struct fractiles generateInitialStrings(long len){
	std::vector<string> temp =  generateAllStrings(len);
	struct fractiles result;
	for (int i = 0; i < temp.size(); ++i)
		{
			string check = temp[i];
			for (int j = 0; j < check.length(); ++j)
			{
				if(check[j] == '0') check[j] = 'L';
				else check[j] = 'G';
			}
			result.initial.push_back(check);
		}	
		return result;
}

string populateOne(string inputStr, long number){
	string result = "";
	string gold = "";
	for (int i = 0; i < inputStr.length(); ++i)
			gold = gold + 'G';
	for (int j = 0; j  < number; j++){	
		for (int i = 0; i < inputStr.length(); ++i)
		{
			if(inputStr[i] == 'G') result = result + gold;
			else result = result + inputStr;
		}
	}	
	return result;
}

struct fractiles populateFinal(struct fractiles input, long number){
	for (int i = 0; i < input.initial.size(); ++i)
	{
		input.final.push_back(populateOne(input.initial[i],number));
	}
	return input;

}

struct fractiles setIndex(struct fractiles info){
	info.index = -1;
	for (int i = 0; i < info.final.size(); ++i)
	{	string check = info.final[i];
		bool condition = false;
		for (int j = 0; j < check.length(); ++j)
		{
			if(check[j] == 'G') {
				condition = true;
				break;
			}
		}
		if(condition == false) {
			info.index = i;
			break;
		}
	}
	return info;
}

std::vector<struct pairs>  generateAllCombination(std::vector<struct pairs> v,long K,long total){
	cout << "In generateAllCombination: " << K << endl;
	if(K == 0) return v;

	if(v.size() == 0){
		for (int i = 0; i < total; ++i)
		{
			struct pairs a;
			a.values.push_back(i);
			v.push_back(a);
		}
		return generateAllCombination(v,K-1,total);
	}else {
		std::vector<struct pairs> another;

		for (int i = 0; i < v.size(); ++i)
		{
			
			for (int j = v[i].values[v[i].values.size()-1]+1; j < total; ++j)
			{
				struct pairs abc = v[i];
				abc.values.push_back(j);
				another.push_back(abc);
			}
		}
		return generateAllCombination(another,K-1,total);

	}

}

string vectorToStringA(std::vector<long> myVector, struct fractiles input){
	string myString = "";
	string in = input.final[input.index];
	for (int i = 0; i < myVector.size(); ++i)
		myString = myString + ((char)in[myVector[i]]);
	return myString;
}


std::vector<string> vectorToStringB(std::vector<long> myVector,struct fractiles info){
	string myString = "";
	string in = info.final[info.index];

	std::vector<string> v;
	for (int j = 0; j < info.final.size(); ++j)
	{
	string str = info.final[j];
	if(str != in){
		for (int i = 0; i < myVector.size(); ++i)
			myString = myString + ((char)str[myVector[i]]);
		
		v.push_back(myString);
		}
	}
	return v;
}

bool makeADecision(std::vector<string> v, string str){
	bool decision = true;
	for (int i = 0; i < v.size(); ++i)
	{
		if(str == v[i]){
			decision = false;
			break;
		}
	}
	return decision;
}

std::vector<long> findTheTiles(struct fractiles info,long C, long S){

	std::vector<struct pairs> vec;
	vec = generateAllCombination(vec, S, info.final[0].length());
	for (int i = 0; i < vec.size(); ++i)
	{
		std::vector<long> myVector = vec[i].values;
		string stringFromVec = vectorToStringA(myVector,info);
		std::vector<string> v = vectorToStringB(myVector,info);
		if(makeADecision(v,stringFromVec)) return myVector;
	}
	std::vector<long> k;
	return k;
}

int main(){
	long K,C,S;
	
	ifstream input("input.txt");
	ofstream output("output.txt");
	long numberOfInputs;
	input >> numberOfInputs;
	long inputNumber;
	long counter = 0;
	while (numberOfInputs > 0){
		counter++;
		input >> K >> C >> S;
		// struct fractiles info = generateInitialStrings(K);
		// info = populateFinal(info,C);
		// info = setIndex(info);
		// std::vector<long> result = findTheTiles(info,C-1,S);
		 output << "Case #" << counter << ": ";
		if(K==S){
			for (int i = 1; i <= K; ++i)
			{
				output << i << " ";
			}
			output << endl;
		}else output << "IMPOSSIBLE" << endl;
		numberOfInputs--;
	}
	return 0;
}