// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <map>
#include <queue>
#include<set>
#include<stack>
#include<cstdio>
#include <unordered_map>
#include <functional>
#define PI 3.14159265
using namespace std;


int main() {

	std::ios_base::sync_with_stdio(false);
	


	ifstream fin;
	fin.open("A-small-attempt0 (1).in");
	ofstream fout;
	fout.open("A-small-attempt0 (1).out");
	int t;
	fin >> t;
	for (int T = 1; T <= t; T++){
		fout << "Case #" << T << ": ";

		int N,R,P,S;
		fin >> N >> R >> P >> S;
		//R=0,P=1,S=2
		string letter = "RPS";
		string ans = "";
		for (int last = 0; last <= 2; last++){
			int temp[3];
			for (int i = 0; i < 3; i++){
				if (i == last) temp[i] = 1;
				else temp[i] = 0;
			}
			for (int i = 0; i < N; i++){
				int t[3];
				for (int j = 0; j < 3; j++){
					t[j] = temp[j] + temp[(j + 1) % 3];
				}
				for (int j = 0; j < 3; j++){
					temp[j] = t[j];
				}
			}
			bool ok = true;
			if (temp[0] != R || temp[1] != P || temp[2] != S) ok = false;
			if (ok){
				vector<int> vlast;
				vlast.clear();
				vector<int> vnow;
				vnow.clear();
				vlast.push_back(last);
				for (int i = 0; i < N; i++)
				{
					for (int j = 0; j < vlast.size(); j++)
					{
						if (vlast[j] == 1){
							vnow.push_back(1);
							vnow.push_back(0);
						}
						else if (vlast[j] == 2){
							if (i>N - 3)
							{
								vnow.push_back(1);
								vnow.push_back(2);
							}
							else
							{
								vnow.push_back(2);
								vnow.push_back(1);	
							}
						}
						else
						{
							if (i>N - 2)
							{
								vnow.push_back(0);
								vnow.push_back(2);
							}
							else
							{
								vnow.push_back(2);
								vnow.push_back(0);
							}
						}
					}
					vlast = vnow;
					vnow.clear();
				}
				string s = "";
				for (int i = 0; i < vlast.size(); i++)
				{
					char a = letter[vlast[i]];
					s=s+a;
				}
				if (ans == "") ans = s;
				else if (ans>s) ans = s;
			}
		}
		if (ans!="")
		fout << ans<< endl;
		else fout << "IMPOSSIBLE" << endl;

	}
	
	system("PAUSE");
	return 0;
}