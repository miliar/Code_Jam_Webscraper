
#ifndef _PRECOMP_H
#define _PRECOMP_H

#include <cmath>
#include <sstream>
#include <cstdlib>
#include <stack>
#include <climits>
#include <cassert>
#include <iostream>  
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <functional>

const std::string currentDateTime() {
	time_t     now = time(0);
	struct tm  tstruct;
	char       buf[80];
	localtime_s(&tstruct, &now);
	strftime(buf, sizeof(buf), "%Y-%m-%d.%X", &tstruct);

	return buf;
}

#endif
