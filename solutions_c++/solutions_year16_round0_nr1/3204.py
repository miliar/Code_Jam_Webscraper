#include<iostream>
#include<stdafx.h>
#include <iostream>
#include <fstream>
#include<string>
#include <vector>
#include<algorithm>
#define  LL long long
using namespace std;

vector<int>V;
long long Orgnum =0;
bool flag = false;
int cnt = 1;
bool Onlyonce = false;
LL number =0; 

void storeNum(LL num)
{
	Orgnum = num;
	cnt++;
	
	
	while(num!=0)
	{
		int rem = num%10;
		/*if(!Onlyonce)
		{
			V.push_back(rem);
			Onlyonce = true;
		}*/
		if ( std::find(V.begin(), V.end(), rem) != V.end())
		{
		}
		else{
		V.push_back(rem);
		}
		if(V.size() ==10)
		{
			flag = true;
			break;
		}
		num/= 10;
	}
	if(flag == true)
		return;
	storeNum(number*cnt);
}

int main(){
	
	ifstream fin("input.in");
    ofstream fout("output.out");

	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;

	LL t;
	fin >> t;
	
	
	//while(t--)
	for(LL i = 0; i<t; i++)
	{
		
		fin >> number;
		if(number ==0)
		fout << "Case #" << (i+1) << ": " << "INSOMNIA" << endl;
		else{
		storeNum(number);
		fout << "Case #" << (i+1) << ": " << Orgnum << endl;
		}
		V.clear();
		Orgnum =0;
		cnt =0;
		flag = false;

		

	}
		//fout << "Case #" << (i+1) << ": " << need << endl;		
	//}
	return 0;
}