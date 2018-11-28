#include "InputParser.h"

InputParser::InputParser(const string& path) {
	fin.open(path, ios::in);
	assert (fin.is_open());
	getline(fin, line);
	assert (!fin.fail());
	#ifndef NDEBUG
	cerr << "[InputParser] InputParser() '" << line << "'" << endl;
	#endif /* NDEBUG */
	sin.str(line);
	sin.clear();
}

void InputParser::finishLine() {
	getline(fin, line);
	#ifndef NDEBUG
	cerr << "[InputParser] finishLine() <- '" << line << "'" << endl;
	#endif /* NDEBUG */
	sin.str(line);
	sin.clear();	
}

int64_t InputParser::readInt() {
	int64_t value;
	sin >> value;
	#ifndef NDEBUG
	cerr << "[InputParser] readInt() -> " << value << endl;
	#endif /* NDEBUG */
	assert (!sin.fail());
	return value;
}

uint64_t InputParser::readUInt() {
	uint64_t value;
	sin >> value;
	#ifndef NDEBUG
	cerr << "[InputParser] readUInt() -> " << value << endl;
	#endif /* NDEBUG */
	assert (!sin.fail());
	return value;
}

double InputParser::readReal() {
	double value;
	sin >> value;
	#ifndef NDEBUG
	cerr << "[InputParser] readReal() -> " << value << endl;
	#endif /* NDEBUG */
	assert (!sin.fail());
	return value;
}

char InputParser::readChar() {
	char value;
	sin >> value;
	#ifndef NDEBUG
	cerr << "[InputParser] readChar() -> " << value << endl;
	#endif /* NDEBUG */
	assert (!sin.fail());
	return value;
}
