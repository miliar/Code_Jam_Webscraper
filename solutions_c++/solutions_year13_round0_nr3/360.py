// TopCoder.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include "Task1.h"
#include "Task2.h"
#include "Task3.h"
#include <fstream>

bool _isValid(char * str) {
	int nlen = strlen(str);
	int mval = nlen / 2;
	for (int i = 0; i < mval; ++i)
		if (str[i] != str[nlen - i - 1])
			return false;
	return true;
}

void genTests() {
	std::ofstream tests("test.txt");
	tests << "1000" << std::endl;
	for (int i = 0; i < 1000; ++i)
		tests << "1 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" << std::endl;
	tests.close();
}

bool compareLessStr(const string & str1, const string & str2) {
	if (str1.length() < str2.length())
		return true;
	if (str1.length() > str2.length())
		return false;
	return str1 <= str2;
}

string squareStr(char * buff) {
	char dstBuff[200];
	memset(dstBuff, 0, sizeof(dstBuff));
	int idx = 0;
	while (buff[idx] != 0) {
		int idx2 = 0;
		while(buff[idx2] != 0) {
			if (dstBuff[idx + idx2] == 0)
				dstBuff[idx + idx2] = '0';
			dstBuff[idx + idx2] = ((dstBuff[idx + idx2] - '0') +  (buff[idx] - '0')*(buff[idx2] - '0')) + '0';
			if (dstBuff[idx + idx2 + 1] == 0 && (dstBuff[idx + idx2] - '0') / 10 > 0)
				dstBuff[idx + idx2 + 1] = '0';
			dstBuff[idx + idx2 + 1] = (dstBuff[idx + idx2 + 1]  - '0' + (dstBuff[idx + idx2] - '0') / 10) + '0';
			dstBuff[idx + idx2] = (dstBuff[idx + idx2] - '0') % 10 + '0';
			++idx2;
			int idx3 = 0;
			while(dstBuff[idx3] != 0) {
				if ((dstBuff[idx3] - '0') / 10 > 0) {
					if (dstBuff[idx3 + 1] == 0)
						dstBuff[idx3 + 1] = '0';
					dstBuff[idx3 + 1] = ((dstBuff[idx3 + 1] - '0') + (dstBuff[idx3] - '0') / 10) + '0';
					dstBuff[idx3] = ((dstBuff[idx3] - '0') % 10) + '0';
				}
				++idx3;
			}
		}
		++idx;
	}
	int trIdx = strlen(dstBuff) - 1;
	while(trIdx >= 0 && dstBuff[trIdx] == '0') {
		dstBuff[trIdx] = 0;
		--trIdx;
	}
	if (!_isValid(dstBuff))
		return "";
	return dstBuff;
}

vector<string> fairs;

void solve() {
	char buf[200];
	char buf2[200];
	char buf3[200];
	memset(buf, 0, sizeof(buf));
	int sum = 0;
	int idx = 0;
	while (idx >= 0) {
		if (idx >= 25) {
			--idx;
			continue;
		}
		if (buf[idx] == 0) {
			if (idx == 0 && sum == 0) {
				buf[idx] = '3';
				sum = 9;
			} else if (sum + 4 < 10)  {
				buf[idx] = '2';
				sum += 4;
			} else if (sum + 1 < 10) {
				buf[idx] = '1';
				sum += 1;
			} else {
				--idx;
				continue;
			}
		} else {
			sum -= (buf[idx]-'0')*(buf[idx]-'0');
			buf[idx] = ((buf[idx]-'0') - 1) + '0';
			if (buf[idx] > '0')
				sum += (buf[idx]-'0')*(buf[idx]-'0');
			if (buf[idx] < '0') {
				buf[idx] = 0;
				--idx;
				continue;
			}
		}

		memset(buf2, 0, sizeof(buf2));
		memset(buf3, 0, sizeof(buf3));
		for (int i = 0; i < idx + 1; ++i) {
			buf2[i] = buf[i];
			buf2[2*idx + 1 - i] = buf[i];
			buf3[i] = buf[i];
			buf3[2*idx - i] = buf[i];
		}
		string strRes;
		if (2*sum < 10) {
			strRes = squareStr(buf2);
			if (!strRes.empty()) {
				fairs.push_back(strRes);
				if ((fairs.size() % 1000) == 0) {
					std::cout << fairs.size()*100/41551 << "%" << std::endl;
				}
			}
		}
		if (2*sum - (buf[idx]-'0')*(buf[idx]-'0') < 10) {
			strRes = squareStr(buf3);
			if (!strRes.empty()) {
				fairs.push_back(strRes);
				if ((fairs.size() % 1000) == 0) {
					std::cout << fairs.size()*100/41551 << "%" << std::endl;
				}
			}
		}
		if (2*sum - (buf[idx]-'0')*(buf[idx]-'0') < 10)
			++idx;
	}
}

void dump () {
	std::ofstream dumpstr("dump.txt");
	for (int i = 0; i < fairs.size(); ++i)
		dumpstr << fairs[i] << std::endl;
	dumpstr.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	//genTests();
	solve();
	std::cout << "solved!" << std::endl;
	//dump();
	std::ifstream ifs("test.txt");
	std::ofstream ofs("ans.txt");

	int t = 0;
	ifs >> t;
	for (int idx = 0; idx < t; ++idx) {
		char a[200], b[200];
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		ifs >> a;
		ifs >> b;
		long long int counter = 0;
		for (int i = 0; i < fairs.size(); ++i)
			if (compareLessStr(a, fairs[i]) && compareLessStr(fairs[i], b)) {
				++counter;
				//ofs << fairs[i].c_str() << std::endl;
				//ofs.flush();
			}
		ofs << "Case #" << idx + 1 << ": " << counter << std::endl;
	}

	std::cout << "Done!!!" << std::endl;
	char buffer[120];
	std::cin >> buffer;
	return 0;
}

