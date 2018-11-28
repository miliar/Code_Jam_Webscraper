#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
struct MinusPos
{
	int pos_minus_flip_idx = -1;
	int pos_minus_start_idx = 0;
	int pos_minus_end_idx = 0;
};

MinusPos getMinusPos(vector<bool> stack)
{
	struct MinusPos minusPos;

	int size = stack.size();
	while (size-- > 0){
		if (stack[size] == false) {
			minusPos.pos_minus_start_idx = size;
			if (minusPos.pos_minus_flip_idx < 0) minusPos.pos_minus_flip_idx = size;
		}
	}

	return minusPos;
}

vector<bool> flip(vector<bool> stack, int pos)
{
	int size = stack.size();
	vector<bool> flipStack(size, false);
	if (pos >= 0 && pos < size){
		for (int i = 0; i < size; i++){
			if (pos >= 0){
				flipStack[i] = !stack[pos--];
			}
			else {
				flipStack[i] = stack[i];
			}
		}
	}
	return flipStack;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	int T;
	string tStr;
	getline(fin, tStr);
	T = atoi(tStr.c_str());

	string pancakes;
	for (int i = 1; i <= T; i++)
	{
		fin >> pancakes;
		int change_step = 0;
		int pancake_total = pancakes.length();

		vector<bool> PAN_STACK(pancake_total, false);

		int temp_idx = pancake_total;
		int plus_total = 0;
		while (temp_idx-- > 0)
		{
			if (pancakes.at(temp_idx) == '-'){
				PAN_STACK[temp_idx] = false;
			}
			else if (pancakes.at(temp_idx) == '+'){
				PAN_STACK[temp_idx] = true;
				plus_total++;
			}
		}

		struct MinusPos minusPos = getMinusPos(PAN_STACK);
		if (minusPos.pos_minus_flip_idx < 0)
		{
			fout << "Case #" << i << ": 0" << endl;
			continue;
		}

		while (minusPos.pos_minus_flip_idx >= 0)
		{
			if (minusPos.pos_minus_start_idx > 0) {
				PAN_STACK = flip(PAN_STACK, minusPos.pos_minus_start_idx-1);
			}
			else {
				PAN_STACK = flip(PAN_STACK, minusPos.pos_minus_flip_idx);
			}

			change_step++;
			minusPos = getMinusPos(PAN_STACK);
		}

		fout << "Case #" << i << ": " << change_step << endl;
	}

	fout.close();
	return 0;
}

