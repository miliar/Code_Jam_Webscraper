/*************************************************************************
    > File Name: A.cpp
    > Author: csy
    > Mail: chshaoyi7@gmail.com 
    > Created Time: Sun 04 May 2014 12:05:20 AM CST
 ************************************************************************/

#include<iostream>
#include<fstream>
using namespace std;

#include<string>

string Minimize(string str){
	
	string s = "";

	s += str[0];
	for(int i = 1; i < str.size(); i ++){
		if(str[i] != str[i-1]) s += str[i];
	}

	return s;

}

string str[101];

int Fabs(int x){
	if(x < 0) return -x;

	return x;
}

int main(){
	
	ifstream fin("A-small.in");
	ofstream fout("A-small.out");
	int t, n;
	string minStr;
	bool flag = true;
	fin >> t;
	for(int i = 1; i <= t; i ++){
		fin >> n;
		fin >> str[0];

		flag = true;

		minStr = Minimize(str[0]);
		for(int j = 1; j < n; j ++){
			fin >> str[j];
			if(minStr != Minimize(str[j])){
				flag = false;
			}
		}
		
		fout << "Case #" << i << ": ";
		if(!flag) fout << "Fegla Won" << endl;
		else{
			int j = 1, k = 1;
			int total = 0,count1,count2;
			for(int p = 0; p < minStr.size(); p ++){
				count1 = 0; count2 = 0;
				while(j < str[0].size() && str[0][j] == minStr[p]){
					count1 ++;
					j ++;

				}

				while(k < str[1].size() && str[1][k] == minStr[p]){
					count2 ++;
					k ++;
				}

				total += Fabs(count1 - count2);
			}
			fout << total << endl;
		}
	}

}

