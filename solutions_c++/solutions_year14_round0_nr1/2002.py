#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
//#include <fstream> //이거 없어도 freopen 이 되넹....으으....

using namespace std;


void main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int nCase;
	cin>>nCase;

	const int nRow = 4;
	const int nCol = 4;

	int nFirstRow;
	int nSecondRow;
	vector<vector<int>> firstMat;
	vector<vector<int>> secondMat;
	
	firstMat.resize(nRow);
	for(int i = 0 ; i < nRow ; i++)
		firstMat[i].resize(nCol);
	
	secondMat.resize(nRow);
	for(int i = 0 ; i < nRow ; i++)
		secondMat[i].resize(nCol);

	for(int caseIndex = 0 ; caseIndex < nCase ; caseIndex++)
	{
		cin>>nFirstRow;
		for(int i = 0 ; i < nRow ; i++)
			for(int j = 0 ; j < nCol ; j++)
				cin>>firstMat[i][j];		//matrix 세팅

		cin>>nSecondRow;
		for(int i = 0 ; i < nRow ; i++)
			for(int j = 0 ; j < nCol ; j++)
				cin>>secondMat[i][j];


		int nCnt = 0; //정답수
		int selectedCard = -1;
		for(int i = 0 ; i < nRow ; i++){
			for(int j = 0 ; j < nCol ; j++){
				if(firstMat[nFirstRow-1][i] == secondMat[nSecondRow-1][j])
				{
					nCnt++;
					selectedCard = firstMat[nFirstRow-1][i];
				}
			}
		}
		if (nCnt == 0)
			cout <<"Case #"<<caseIndex+1<<": Volunteer cheated!"<<endl;//
		else if (nCnt > 1)
			cout <<"Case #"<<caseIndex+1<<": Bad magician!"<<endl;//Case #1: YES
		else if(nCnt == 1)
			cout <<"Case #"<<caseIndex+1<<": "<<selectedCard<<endl;//Case #1: YES

	}
}