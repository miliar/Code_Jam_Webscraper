#include <iostream>
#include <cstdio>


int main(int argc, char **argv) {

	unsigned T;
	std::cin >> T;

	for (unsigned i=0; i<T; ++i) {
		std::string S;
		std::cin >> S;

		std::string unusedPrefix(S);
		std::string lastWord;
		std::size_t lastWordInsertIx = 0;

		int c = 'Z';
		while (c>='A') {
			std::size_t pos = unusedPrefix.rfind(c);
			while (pos != std::string::npos) {
				lastWord.insert(lastWordInsertIx,unusedPrefix.substr(pos));
				unusedPrefix = unusedPrefix.substr(0,pos);
				++lastWordInsertIx;
				pos = unusedPrefix.rfind(c);
			}
			--c;
		}

		printf("Case #%d: %s\n",i+1,lastWord.c_str());
	}

	return 0;
}




