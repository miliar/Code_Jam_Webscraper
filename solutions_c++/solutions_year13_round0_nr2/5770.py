#ifndef LAWN_CUTTER_H
#define LAWN_CUTTER_H
/**
 * @file
 * @brief Class used to check if it is possible to cut a lawn
 * @author Benjamyn
 */

#include "Lawn.h"

class LawnCutter {
	public:
		bool canCutLawn(const Lawn *lawn) const;
};

#endif
