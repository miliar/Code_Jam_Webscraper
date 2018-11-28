#include <iostream>
#include <string>
#include <stdint.h>

using std::cin;
using std::cout;
using std::string;

bool is_vowels(char c)
{
	char vowels[] = {'a', 'e', 'i', 'o', 'u'};

	for(size_t i = 0; i < 5; ++i) {
		if(c == vowels[i])
			return true;
	}

	return false;
}

int main()
{
    int t;


    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    cin >> t;

    for(size_t i = 0; i < t; ++i) {
		string s;
		size_t n;
		uint32_t res = 0;

		cin >> s >> n;
		
		for(size_t j = 0; j < s.size(); ++j) {
			for(size_t h = j + n; h <= s.size(); ++h) {
				uint32_t k = 0;

				for(size_t g = j; g < h; ++g) {
					if(!is_vowels(s[g]))
						++k;
					else
						k = 0;
				
					if(k >= n) {
						++res;
						break;
					}
				}
			}
		}
		
				
		cout << "Case #" << i+1 << ": ";
		cout << res << std::endl;
	}

    return 0;
}
