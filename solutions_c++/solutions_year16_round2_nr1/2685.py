#include <iostream>
#include <cstdio>
#include <map>
#include <string>



typedef std::map<char,unsigned> CharMap;
typedef std::map<char,unsigned> PhoneNum;



void add(CharMap& cm, char c) {
    CharMap::iterator it = cm.find(c);
    if (it == cm.end()) {
        cm[c] = 1;
    } else {
        ++cm[c];
    }
}

void remove(CharMap& cm, char c, unsigned n) {
    CharMap::iterator it = cm.find(c);
    if (it == cm.end()) {
        std::cerr << "No more " << c << '\n';
    } else if (it->second < n){
        std::cerr << "No more " << c << " - " << it->second << '\n';
    } else {
        it->second -= n;
    }
}

void remove(CharMap& cm, const std::string& word, unsigned n) {

    for (unsigned i=0;i<word.length();++i) {
        remove(cm,word[i],n);
    }
}

unsigned get(CharMap& cm, char c) {
    CharMap::iterator it = cm.find(c);
    if (it == cm.end()) {
        return 0;
    } else {
        return it->second;
    }
}


void read(CharMap& cm,const std::string& str) {

    for (unsigned i=0; i<str.length(); ++i) {
        add(cm,str[i]);
    }
}


void process(CharMap& cm, const std::string& word, char c, char digit, PhoneNum& phoneNumber) {

    unsigned n = get(cm,c);
    if (n > 0) {
        remove(cm,word,n);
        phoneNumber[digit] = n;
    }
}


std::string getPhoneNumStr(PhoneNum phoneNumber) {

    std::string r;

    for (PhoneNum::iterator it = phoneNumber.begin();
    it != phoneNumber.end();
    ++it) {
         r.append(it->second,it->first);
    }

    return r;
}


int main(int argc, char **argv) {

	unsigned T;
	std::cin >> T;

	for (unsigned i=0; i<T; ++i) {
		std::string S;
		std::cin >> S;

        CharMap cm;
        read(cm,S);

        PhoneNum phoneNumber;

        process(cm,"SIX",'X','6',phoneNumber);
        process(cm,"TWO",'W','2',phoneNumber);
        process(cm,"ZERO",'Z','0',phoneNumber);
        process(cm,"EIGHT",'G','8',phoneNumber);
        process(cm,"THREE",'H','3',phoneNumber);
        process(cm,"FOUR",'U','4',phoneNumber);
        process(cm,"FIVE",'F','5',phoneNumber);
        process(cm,"SEVEN",'V','7',phoneNumber);
        process(cm,"NINE",'I','9',phoneNumber);
        process(cm,"ONE",'O','1',phoneNumber);

		printf("Case #%d: %s\n",i+1,getPhoneNumStr(phoneNumber).c_str());
	}

	return 0;
}



