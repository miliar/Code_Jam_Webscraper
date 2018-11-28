/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * main.cc
 * Copyright (C) 2013 Kartik Somani <kartiksomani@ymail.com>
 * 
 * GoogleCodeJam-2013 is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * GoogleCodeJam-2013 is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;
typedef vector<int> int_vec;
typedef vector<string> str_vec;
vector<int_vec> EncodeTicToeMatrix(str_vec sMatrix,int iDim);
int_vec GetTicTacToeProducts(vector<int_vec> iMatrix);
string GetTicTacToeResult(str_vec sMatrix);
int main()
{
		str_vec sMatrix;
	
	string sInput;
	string sResult;
	string sLine;
	str_vec sResults;
	int iCases;	
	int iSize;
	
	int_vec iProducts;
	iSize=4;
	//Input Number of cases
	cin>>iCases;
	sResults.reserve(iCases);
	sMatrix.reserve(iSize);
	for(int iCase=0;iCase<iCases;iCase++){
		sMatrix.clear();
		for(int iRow=0;iRow<iSize;iRow++){
		cin>>sInput;
		sMatrix.push_back(sInput);
		}
		std::getline(std::cin,sLine);
		sResult=GetTicTacToeResult (sMatrix);
		sResults.push_back(sResult);		
	}

	//Output Results
	for(int iRes=0;iRes<sResults.size();iRes++){
		cout<<"Case #"<<iRes+1<<": "<<sResults[iRes]<<endl;
	}
	return 0;
}
string GetTicTacToeResult(str_vec sMatrix){
	vector<int_vec> iMatrix;
	int_vec iProducts;
	int iSize;
	bool bIncomplete;

	bIncomplete=false;
	iSize=sMatrix.size();
	//Encode Matrix
	iMatrix=EncodeTicToeMatrix (sMatrix,iSize);

	//Get Products
	iProducts=GetTicTacToeProducts (iMatrix);
	
	for(int iProd=0;iProd<iProducts.size();iProd++){
		
		switch(iProducts[iProd]){
			case 625:
				case 250:
				return "O won";
			case 81:
				case 54:
				return "X won";
				case 0:
				bIncomplete=true;
				break;				
		}
	}
	//If game has not yet completed
	if(bIncomplete==true){
		return "Game has not completed";
	}
	else{
		return "Draw";
	}
}

//Function to encode tic tac toe into prime numbers matrix
vector<int_vec> EncodeTicToeMatrix(str_vec sMatrix,int iDim){
	vector<int_vec> iMatrix;
	int_vec iTempRow;

	iMatrix.reserve(iDim*iDim);
	iTempRow.reserve(iDim);
	for(int i=0;i<iDim;i++){
		iTempRow.clear();
		for(int j=0;j<iDim;j++){
			switch(sMatrix[i].at(j)){
				case 'X':
					iTempRow.push_back(3);
						break;
					case 'O':
					iTempRow.push_back(5);
					break;
					case 'T':
					iTempRow.push_back(2);
					break;
					default:
					iTempRow.push_back(0);
			}
		}
		iMatrix.push_back(iTempRow);
	}
	return iMatrix;
}
int_vec GetTicTacToeProducts(vector<int_vec> iMatrix){
	int_vec iProducts;
	int iTempRowProd;
	int iTempColProd;
	int iDim;
int iRightDiagProduct;
	int iLeftDiagProduct;

	iRightDiagProduct=1;
		iLeftDiagProduct=1;
	iTempRowProd=1;
	iTempColProd=1;
	iDim=iMatrix.size();
	iProducts.reserve(2*iDim+2);
	for(int i=0;i<iDim;i++){
		iTempRowProd=1;
		iTempColProd=1;
		for(int j=0;j<iDim;j++){
			iTempRowProd=iTempRowProd*iMatrix[i][j];
			iTempColProd=iTempColProd*iMatrix[j][i];
			if(i==j){
				iRightDiagProduct=iRightDiagProduct*iMatrix[i][j];
			}
			if(i+j+1==iDim){
				iLeftDiagProduct=iLeftDiagProduct*iMatrix[i][j];
			}
		}
		iProducts.push_back(iTempRowProd);
		iProducts.push_back(iTempColProd);
	}
	iProducts.push_back(iRightDiagProduct);
	iProducts.push_back(iLeftDiagProduct);
	return iProducts;
}


