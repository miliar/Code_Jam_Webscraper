#include "stdafx.h"
#include "StandupOvation.h"


StandupOvation::StandupOvation(int tc, string values)
	:testCase(tc)
{
	const char* v = values.c_str();
	char vv[2] = { 0, 0 };
	while (*v != 0)
	{
		vv[0] = *v;
		audiance.push_back( atoi(vv) );		
		v++;
	}
}


StandupOvation::~StandupOvation()
{
}

int StandupOvation::process()
{

	int sh_level = 0;
	int clapping = 0;
	int friends = 0;

	contTypeIt cit = audiance.cbegin();

	while (cit != audiance.cend())
	{
		

		if ((clapping + friends) < sh_level)
		{
			friends += ( sh_level - (clapping + friends) );
		}

		clapping += (*cit);
		
		++sh_level;
		++cit;
		
	}

	return friends;

	

}