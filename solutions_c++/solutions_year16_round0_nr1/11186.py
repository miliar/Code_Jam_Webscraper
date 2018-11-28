// GoogleCodeJam20160410.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool CheckAllUsed(const std::vector<bool>& check)
{
	for (bool b : check) {
		if (!b) {
			return false;
		}
	}
	return true;
}

void Check(int NN, std::vector<bool>& check)
{
	while (NN > 0) {
		int a = NN % 10;
		check[a] = true;
		NN = NN / 10;
	}
}

int Calc(int N)
{
	std::vector<bool> check;
	check.resize(10);
	for (int i = 0; i < 10; ++i) {
		check[i] = false;
	}

	const int MAX = 100;
	for (int i = 1; i <= MAX; ++i) {
		int NN = N * i;
		Check(NN, check);
		if (CheckAllUsed(check)) {
			return NN;
		}
	}

	return -1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	if (argc != 2) {
		return 1;
	}

	std::vector<int> vectorN;
	{
		ifstream ifs(argv[1]);
		if (!ifs.is_open()) {
			return 2;
		}

		string s;
		getline(ifs, s);
		int T = atoi(s.c_str());
		vectorN.resize(T);
		for (int i = 0; i < T; ++i) {
			getline(ifs, s);
			vectorN[i] = atoi(s.c_str());
		}
	}

	std::vector<int> vectorResult;
	vectorResult.reserve(vectorN.size());

	for (int N : vectorN) {
		vectorResult.push_back(Calc(N));
	}

	//出力
	{
		ofstream ofs("result.txt");
		for (size_t i = 0; i < vectorResult.size(); ++i) {
			int result = vectorResult[i];
			ofs << "CASE #" << i + 1 << ": ";
			if (vectorResult[i] < 0) {
				ofs << "INSOMNIA";
			}
			else {
				ofs << vectorResult[i];
			}
			ofs << std::endl;
		}
	}

	return 0;
}

