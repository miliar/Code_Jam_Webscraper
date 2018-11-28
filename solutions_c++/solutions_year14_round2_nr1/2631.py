#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <map>
#include <unistd.h>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
    if (!fscanf(stdin, "%d", &T))
        cerr << "File not valid" << endl;

    for (int case_no = 0; case_no < T; ++case_no) {
        int N;
        fscanf(stdin, "%d\n", &N);

		vector<vector<int> > strings;
		std::string singlified;

		strings.resize(N);
		bool valid = true;

		for (int i = 0; i < N; ++i) {
			char buf[4096];
			fgets(buf, 4096, stdin);
			std::string str(buf);
			while ((str[str.size()-1] == '\n') || (str[str.size()-1] == '\r') || (str[str.size()-1] == ' '))
				str.resize(str.size() - 1);
			string singles;
			int cur_letter = 0;
			int cur_letter_start = 0;
			for (size_t j = 0; j < str.size(); ++j) {
				if ((j == 0) || (str[j] != str[j-1])) {
					singles.push_back(str[j]);
					if (j != 0) {
						strings[i].push_back(j - cur_letter_start);
						++cur_letter;
						cur_letter_start = j;
					}
				}
			}
			strings[i].push_back(str.size() - cur_letter_start);
			
			if (i == 0)
				singlified = singles;
			else if (singles != singlified) {
				valid = false;
			}
		}
		if (!valid) {
	        printf("Case #%d: Fegla Won\n", case_no + 1);
		} else {
			int result = 0;
			for (int letter = 0; letter < strings[0].size(); ++letter) {
				int sum = 0;
				int min = 200, max = 0;
				for (int i = 0; i < N; ++i) {
					sum += strings[i][letter];
					if (strings[i][letter] > max)
						max = strings[i][letter];
					if (strings[i][letter] < min)
						min = strings[i][letter];
				}
				int local_result = 500000000;
				for (int candidate = min; candidate <= max; ++candidate) {
					int cand_result = 0;
					for (int i = 0; i < N; ++i) {
						cand_result += abs(candidate - strings[i][letter]);
					}
					if (cand_result < local_result)
						local_result = cand_result;
				}
				result += local_result;
			}
			printf("Case #%d: %d\n", case_no + 1, result);
		}
    }

    return 0;
}
