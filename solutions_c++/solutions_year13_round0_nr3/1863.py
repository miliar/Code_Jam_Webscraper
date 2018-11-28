#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <ctime>
#include <map>
#include <cmath>
#include <fstream>
#include <iterator>
#include <cstring>
#include <algorithm>
#include <set>
#include <cassert>
#include <list>
#include <sstream>
#define LL long long
#define ULL unsigned long long
#define UI unsigned int
#define MOD 1000000007
#define MAX_NUM 10000000
using namespace std;

ULL squares[MAX_NUM];
vector<ULL> vect;
ULL A,B;
int cnt;

bool isPalindrome(string);

void findFirstNums()
{
	for(ULL i=0;i<MAX_NUM;i++)
		squares[i] = i*i;

	for(int i=0;i<MAX_NUM;i++){
		stringstream ss,ss1;
		ss << squares[i];
		ss1 << i;
		string str = ss.str();
		string str1 = ss1.str();
		if(isPalindrome(str) && isPalindrome(str1))
			vect.push_back(squares[i]);
	}
	
	//for(size_t i=0;i<vect.size();i++)
		//cout << i << " - " << vect[i] << endl;
}

bool isPalindrome(string str)
{
	int i = 0;
	int j = str.size() -1;
	
	while(i<j){
		if(str[i] != str[j])
			return false;
		i++;
		j--;
	}
	
	return true;
}

int main ()
{
	findFirstNums();
	
	int testCases;
    ofstream fout;
    ifstream fin;
    fin.open("testFile.txt");
    fout.open("output.txt");
    
    fin >> testCases;
    
    
    
    for(int i=0;i<testCases;i++){
		
		fin >> A >> B;
		
		cnt = 0;

		for(size_t j=0;j<vect.size();j++)
			if(vect[j] >= A && vect[j] <= B)
				cnt++;
		
		fout << "Case #" << i+1 << ": " << cnt << endl;

		
		//printBoard();
		
	}
    
    fin.close(); 
    fout.close(); 
    
}
