#ifndef __MAGICTRICK__
#define __MAGICTRICK__

#include "cppFun.h"


class MagicTrick : public FileProcessor
{
public:
	MagicTrick(std::ifstream& inputFile);
	~MagicTrick() {}

	void Process(int caseNumber);
};


#endif
