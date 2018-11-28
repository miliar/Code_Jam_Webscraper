#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>

#define small 
//#define large

const short i = 2, j = 3, k = 4;


short conv(char c){
	switch (c){
	case 'i':
		return i;
	case 'j':
		return j;
	case 'k':
		return k;
	}
}

short multiply(const short mult1, const char in2){
	short mult2;
	mult2 = conv(in2);
	switch (mult1)
	{
	case -1:
		switch (mult2)
		{
		case i:
			return -i;
		case j:
			return -j;
		case k:
			return -k;
		}
	case 1:
		switch (mult2)
		{
		case i:
			return i;
		case j:
			return j;
		case k:
			return k;
		}
	case i:
		switch (mult2)
		{
		case i:
			return -1;
		case j:
			return k;
		case k:
			return -j;
		}
	case j:
		switch (mult2)
		{
		case i:
			return -k;
		case j:
			return -1;
		case k:
			return i;
		}
	case k:
		switch (mult2)
		{
		case i:
			return j;
		case j:
			return -i;
		case k:
			return -1;
		}
	case -i:
		return(-1 * multiply(i, in2));
	case -j:
		return(-1 * multiply(j, in2));
	case -k:
		return(-1 * multiply(k, in2));
	}
}

int main()
{
#if defined(small)
	std::ifstream in("A-small-practice.in");
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
	std::ofstream out("out.out");
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#elif defined(large)
	std::ifstream in("A-large-practice.in");
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
	std::ofstream out("out.out");
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#endif

	int T;
	long long L, X;
	std::cin >> T;
	std::string s;
	for (int l = 1; l <= T; l++){
		std::vector<char> vc;
		short result1 = 1, result2 = 1, result3 = 1;
		short split1 = -1, split2 = -1; //index after which is split 
		bool cont1 = false, cont2 = false;
		std::cin >> L;
		std::cin >> X;
		std::cin >> s;
		for (long long m = 0; m < X; m++)
			for (long long n = 0; n < L; n++)
				vc.push_back(s[n]);

		while (((result1 != i) || (result2 != j) || (result3 != k)) & (split1 + 1 + 2 <= vc.size()) & (split2 + 1 + 1 <= vc.size())){
			while ((result1 != i || cont1 == true) & split1 + 1 + 2 <= vc.size()){
				cont1 = false;
				split1 = split1++;
				result1 = multiply(result1, vc[split1]);
			}
			if (cont2 != true)
				split2 = split1;
			while ((result2 != j || cont2 == true) & split2 + 1 + 1<= vc.size()){
				cont2 = false;
				split2 = split2++;
				result2 = multiply(result2, vc[split2]);
			}
			for (long long m = (split2 + 1); m + 1 <= vc.size(); m++)
				result3 = multiply(result3, vc[m]);
			if (split2 + 1 + 1 > vc.size()){
				cont1 = true;
				result2 = 1;
				result3 = 1;
			}
			if (result3 != k){
				cont2 = true;
				result3 = 1;
			}
		}
		if (result1 == i & result2 == j & result3 == k)
			std::cout << "Case #" << l << ": " << "YES" << std::endl;
		else
			std::cout << "Case #" << l << ": " << "NO" << std::endl;
	}
}