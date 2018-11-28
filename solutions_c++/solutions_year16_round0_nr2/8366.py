#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fstream>
#define LL long long
using namespace std;

char S[101];
ofstream coutf; 
int main()	{
	coutf.open("output.txt");

	int t, T;
	cin >> T;
	for (t = 0; t < T; t++){
		scanf("%s", S);
		int len = 0;
		for (int i = 0; S[i]; i++)len++;
		int Cnt = 0; 
		char flag = '-';
		for (int i = len - 1; i >= 0; i--){
			if (S[i] == flag){
				Cnt++;
				if (flag == '-')flag = '+';
				else flag = '-';
			}
		}


		coutf << "Case #" << t + 1 << ": " << Cnt<<'\n';
	}


	return 0;
}