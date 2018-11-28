#include <cstdio>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string.h>

char quat_product(char a, char b, int *sign) {
	if (a == '1') {
		*sign = 1;
		return b;
	} 

	if (b == '1') {
		*sign = 1;
		return a;
	}

	if (a == b) {
		*sign = -1;
		return '1';
	} 

	if (a == 'i') {
		if (b == 'j') {
			*sign = 1;
			return 'k';
		} 
		if (b == 'k') {
			*sign = -1;
			return 'j';
		}
	}

	if (a == 'j') {
		if (b == 'i') {
			*sign = -1;
			return 'k';
		} 
		if (b == 'k') {
			*sign = 1;
			return 'i';
		}
	}

	 // a = k
	if (b == 'i') {
		*sign = 1;
		return 'j';
	}

	if (b == 'j') {
		*sign = -1;
		return 'i';
	}
}

#define SUB2IND(i, j, dim) (i)*(dim)+(j)

bool has_ijk_reduction(const char *s) {
	// dynamic program
	// let q[i,j] be the quat reduction of s[i:j]

	size_t s_len = strlen(s);

	char *q = (char*)malloc(s_len * s_len * sizeof(char));
	int *signs = (int*) malloc(s_len * s_len * sizeof(int));

	bzero(q, s_len*s_len*sizeof(char));

	int temp_sign;

	for (int i = 0; i < s_len; i++) {
		// begin with diagonal and work outwards
		q[SUB2IND(i,i,s_len)] = s[i];
		signs[SUB2IND(i,i,s_len)] = 1;

		// work forwards, j > i
		for (int j = i + 1; j < s_len; j++) {
			q[SUB2IND(i,j,s_len)] = quat_product(q[SUB2IND(i,j-1,s_len)], s[j], &temp_sign);
			signs[SUB2IND(i,j,s_len)] = signs[SUB2IND(i,j-1,s_len)] * temp_sign;
		}
	}

	// try to find a split point i such that s[0:i] reduces to 'i'
	for (int i = 0; i < s_len; i++) {
		if (q[SUB2IND(0, i, s_len)] == 'i' && signs[SUB2IND(0,i,s_len)] > 0) {
			// found i substring, look for j and k
			// try to find a split point j such that s[i:j] ~ 'j' and s[j:] ~ 'k'
			for (int j = i + 1; j < s_len - 1; j++) {
				char j_reduction = q[SUB2IND(i+1, j, s_len)];
				char j_sign = signs[SUB2IND(i+1, j, s_len)];

				char k_reduction = q[SUB2IND(j+1, s_len-1, s_len)];
				char k_sign = signs[SUB2IND(j+1, s_len-1, s_len)];

				if (j_reduction == 'j' && j_sign > 0 && k_reduction == 'k' && k_sign > 0) {
					// printf("ding ding ding!!\n");
					// printf("%s => (%.*s)(%.*s)(%s)\n", s, i+1, s, j-i, s+i+1, s+j+1);

					free(q);
					free(signs);
					return true;
				}
			}
		}
	}
					free(q);
					free(signs);

	return false;
}


int main(int argc, char *argv[]) {

	std::ifstream file_in(argv[1], std::ifstream::in);

	int n_cases;
	file_in >> n_cases;

	for (int i = 0; i < n_cases; i++) {
		int nchars, nrepeats;
		file_in >> nchars >> nrepeats;

		std::string in_str;
		file_in >> in_str;

		// build repeated string
		std::ostringstream os;
		for (int j = 0; j < nrepeats; j++) {
			os << in_str;
		}
		const std::string& s = os.str();

		std::cout << "Case #" << i+1 << ": " << (has_ijk_reduction(s.c_str()) ? "YES" : "NO") << std::endl;
	}

	return 0;
}


