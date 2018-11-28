/*************************************************************************
	> File Name: problemA.cpp
	> Author: csy
	> Mail: chshaoyi7@gmail.com 
	> Created Time: 2015年04月11日 星期六 20时28分54秒
 ************************************************************************/

#include<iostream>
using namespace std;

#include<string>
#include<fstream>

int main(){
	
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int t;
	int smax, count, result;
	string shyness;
	fin >> t;
	for(int i = 1; i <= t; i ++){
		fin >> smax >> shyness;
		result = count = 0;
		count = shyness[0] - '0';
		for(int j = 1; j < shyness.size(); j ++){
			if(shyness[j]!='0'){
				if(count <= j){
					result += j - count;
					count  += j - count  + shyness[j] - '0';
				}else{
					count += shyness[j] - '0';
				}
			}
		}
		fout << "Case #" << i << ": " << result << endl;
	}

	return 0;
}
