/**
 * @file Problem_A.cpp
 * @brief A. Magic Trick 
 * @details 
 * Problem
 * 
 * Recently you went to a magic show. You were very impressed by one of the tricks, so you decided to try to figure out the secret behind it!
 * 
 * The magician starts by arranging 16 cards in a square grid: 4 rows of cards, with 4 cards in each row. Each card has a different number from 1 to 16 written on the side that is showing. Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in.
 * 
 * Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order. Once again, he asks the volunteer which row her card is in. With only the answers to these two questions, the magician then correctly determines which card the volunteer chose. Amazing, right?
 * 
 * You decide to write a program to help you understand the magician's technique. The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions: the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement. The rows are numbered 1 to 4 from top to bottom.
 * 
 * Your program should determine which card the volunteer chose; or if there is more than one card the volunteer might have chosen (the magician did a bad job); or if there's no card consistent with the volunteer's answers (the volunteer cheated).
 * Solving this problem
 * 
 * Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has only 1 Small input. Once you have solved the Small input, you have finished solving this problem.
 * Input
 * 
 * The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing an integer: the answer to the first question. The next 4 lines represent the first arrangement of the cards: each contains 4 integers, separated by a single space. The next line contains the answer to the second question, and the following four lines contain the second arrangement in the same format.
 * Output
 * 
 * For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1).
 * 
 * If there is a single card the volunteer could have chosen, y should be the number on the card. If there are multiple cards the volunteer could have chosen, y should be "Bad magician!", without the quotes. If there are no cards consistent with the volunteer's answers, y should be "Volunteer cheated!", without the quotes. The text needs to be exactly right, so consider copying/pasting it from here.
 * Limits
 * 
 * 1 ≤ T ≤ 100.
 * 1 ≤ both answers ≤ 4.
 * Each number from 1 to 16 will appear exactly once in each arrangement. 
 * 
 * @author Alonso J. Gragera Aguaza <alonso@is.s.u-tokyo.ac.jp> 
 * @version 1.0
 * @date 2014
 * 
 * @copyright Copyright (c) 2014 - LGPL v.3 
 * @copyright This file is subject to the terms and conditions defined in
 * file 'LICENSE', which is part of this source code package.
 */

#include <iostream> 
#include <fstream>

const int MAX_SIZE = 16;
const int SQ_SIZE = 4;

using namespace std;

int main(int argc, char const *argv[])
{
	bool MagicMatrix[MAX_SIZE];

	int numCases;
	int firstRow, secondRow;
	int firstMatrix[SQ_SIZE][SQ_SIZE], secondMatrix[SQ_SIZE][SQ_SIZE];

	ifstream inFile;
	ofstream outFile;

	inFile.open("A-small-attempt0.in");
	outFile.open("A-small-attempt0.out");

	inFile >> numCases;
//	cout << numCases << endl;

	for (int k = 0; k < numCases; ++k)
	{
		for (int i = 0; i < MAX_SIZE; ++i)
			MagicMatrix[i] = true;

		inFile >> firstRow;
//		cout << firstRow << endl;
		for (int i = 0; i < SQ_SIZE; ++i)
		{
			for (int j = 0; j < SQ_SIZE; ++j)
			{
				inFile >> firstMatrix[i][j];
//				cout << firstMatrix[i][j] << " ";
			}
//			cout << endl;
		}

		inFile >> secondRow;
//		cout << secondRow << endl;
		for (int i = 0; i < SQ_SIZE; ++i)
		{
			for (int j = 0; j < SQ_SIZE; ++j)
			{
				inFile >> secondMatrix[i][j];
//				cout << secondMatrix[i][j] << " ";
			}
//			cout << endl;
		}

		for (int i = 0; i < SQ_SIZE; ++i)
		{
			for (int j = 0; j < SQ_SIZE; ++j)
			{
				if (i != firstRow-1)
					MagicMatrix[firstMatrix[i][j]-1] = false;

				if (i != secondRow-1)
					MagicMatrix[secondMatrix[i][j]-1] = false;
			}
		}


		int possibleNumCount = 0;
		int possibleNum = 0;
		
		for (int i = 0; i < MAX_SIZE; ++i)
		{
//			cout << i << ": " << MagicMatrix[i] << " ";
			if (MagicMatrix[i] == true)
			{
				possibleNumCount++;
				possibleNum = i+1;
			}
		}
//		cout << endl;

		outFile << "Case #" << k+1 <<": ";
//		cout << "Case #" << k+1 <<": ";
		switch (possibleNumCount)
		{
			case 0:
				outFile << "Volunteer cheated!" << endl;
//				cout << "Volunteer cheated!" << endl;
				break;
			case 1:
				outFile << possibleNum << endl;
//				cout << possibleNum << endl;
				break;
			default:
				outFile << "Bad magician!" << endl;
//				cout << "Bad magician!" << endl;
				break;
		}
	}

	inFile.close();
	outFile.close();
	
	return 0;
}