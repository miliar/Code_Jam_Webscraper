#include "CGCJLib.hpp"
#include <sstream>

std::string CGCJLib::getSourcePath() {
	std::stringstream sstream;
	sstream << getenv("HOME") << "/Downloads/codejam-commandline-1.2-beta1/source";
	return sstream.str();
}
