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
#define LL long long
#define ULL unsigned long long
#define UI unsigned int
#define MOD 1000000007
#define H 100
using namespace std;

int board[110][110];
int testCases;
int N,M;


void printBoard()
{
	for(int k=0;k<N;k++){
		for(int l=0;l<M;l++)
			cout << board[k][l];
		cout << endl;
	}
	cout << endl;
}

//Return true if we didn't find bigger num in that row else false
bool checkRowForBigger(int a, int b)
{
	int num = board[a][b];
	for(int j=0;j<M;j++)
		if(board[a][j] > num)
			return false;
	return true;
}

//Return true if we didn't find bigger num in that column else false
bool checkColumnForBigger(int a, int b)
{
	int num = board[a][b];
	for(int i=0;i<N;i++)
		if(board[i][b] > num)
			return false;
	return true;
}

bool solve()
{
	for(int k=0;k<N;k++)
		for(int l=0;l<M;l++)
			if(board[k][l] != H)
				if(!checkColumnForBigger(k,l) && !checkRowForBigger(k,l))
					return false;
	return true;
}

int main ()
{

    ofstream fout;
    ifstream fin;
    fin.open("testFile.txt");
    fout.open("output.txt");
    
    fin >> testCases;
    
    for(int i=0;i<testCases;i++){
		
		fin >> N >> M;
		
		for(int k=0;k<N;k++)
			for(int l=0;l<M;l++)
				fin >> board[k][l];			
		
		if(solve() == true)
			fout << "Case #" << i+1 << ": YES" << endl;
		else
			fout << "Case #" << i+1 << ": NO" << endl;
		
		//printBoard();
		
	}
    
    fin.close(); 
    fout.close(); 
}
