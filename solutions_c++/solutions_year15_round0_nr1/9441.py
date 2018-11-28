// GoogleCodeJamQualificationRoundA.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"

#include <vector>

struct Q
{
	std::vector<int> arrayS;

	int Slove() const {
		int a = 0;
		int sum = 0;
		for (size_t i = 0; i < arrayS.size(); ++i) {
			if (arrayS[i] != 0 && (int)i > sum) {
				a += i - sum;
				sum += i - sum;
			}
			sum += arrayS[i];
		}
		return a;
	}
};

void LoadQ(const std::wstring& sPath, std::vector<Q>& arrayQ)
{
	FILE* fpIn = NULL;
	_wfopen_s(&fpIn, sPath.c_str(), L"r");

	wchar_t szLine[2048];
	int T = 0;
	{
		if (!fgetws(szLine, 2048, fpIn)) {
			_ASSERTE(false);
			return;
		}
		T = _wtoi(szLine);
	}

	for (int i = 0; i < T; ++i) {
		if (!fgetws(szLine, 2048, fpIn)) {
			_ASSERTE(false);
			return;
		}
		int n = _wtoi(szLine);
		wchar_t* pc = szLine;
		while (iswdigit(*pc)) {
			++pc;
		}
		while (!iswdigit(*pc)) {
			++pc;
		}

		arrayQ.push_back(Q());
		for (int j = 0; j < n+1; ++j) {
			arrayQ.back().arrayS.push_back((*pc) - L'0');
			++pc;
		}
	}


	fclose(fpIn);
}

int _tmain(int argc, _TCHAR* argv[])
{
	if (argc != 2) {
		return 1;
	}

	std::vector<Q> arrayQ;
	LoadQ(argv[1], arrayQ);

	FILE* fpOut = NULL;
	_wfopen_s(&fpOut, L"c:\\temp\\a.txt", L"w");

	for (size_t i = 0; i < arrayQ.size(); ++i) {
		fwprintf_s(fpOut, L"Case #%d: %d\n", i+1, arrayQ[i].Slove());
	}

	fclose(fpOut);

	return 0;
}

