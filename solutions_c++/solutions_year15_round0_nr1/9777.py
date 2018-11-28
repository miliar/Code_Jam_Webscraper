// CPP file
// Created in Microsoft VS2013 Community 

#include <stdio.h>
#include <tchar.h>

#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

int main()
{
	unsigned int uiT = 0; // test cases

	vector< unsigned int > conSmax;
	vector< vector< unsigned int > > conColAudienceShyness;

	string sFileName = "A-small-attempt0";

	//--------------------- begin - reading from file ---------------------
	FILE *stream;

	if (fopen_s(&stream, (sFileName + ".in").c_str(), "r"))
	{
		cout << "File does not exist" << endl;
	}
	else
	{
		fscanf_s(stream, "%d", &uiT);

		for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
		{
			// reading data for each test case

			unsigned int uiNumber = 0;
			fscanf_s(stream, "%d", &uiNumber);
			conSmax.push_back(uiNumber);
			unsigned int uiTotalAudience = 0;
			fscanf_s(stream, "%d", &uiTotalAudience);
			vector < unsigned int > conAudience;
			for (unsigned int uiI = 0; uiI < uiNumber + 1; ++uiI)
			{
				unsigned int uiAud = uiTotalAudience % 10;
				uiTotalAudience /= 10;
				conAudience.push_back(uiAud);
			}
			std::reverse(conAudience.begin(), conAudience.end());
			conColAudienceShyness.push_back(conAudience);
		}

		// closing file
		fclose(stream);
	}
	//--------------------- end - reading from file -----------------------


	//--------------------- begin - algorithm ---------------------
	vector< unsigned int > conFriends;
	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		unsigned int uiFriend = 0;
		unsigned int uiPeopleStanding = 0;
		for (unsigned int uiK = 0; uiK < conSmax[uiIdx] + 1; ++uiK)
		{
			unsigned int uiPeopleWithShynessK = conColAudienceShyness[uiIdx][uiK];
			if (uiPeopleWithShynessK != 0)
			{
				if ( ( uiPeopleStanding < uiK ) && ( uiK != 0 ) )
				{
					int iPeopleMissing = uiK - uiPeopleStanding;
					assert(iPeopleMissing > 0);
					uiFriend += iPeopleMissing;
					uiPeopleStanding += iPeopleMissing;
				}
				uiPeopleStanding += uiPeopleWithShynessK;
			}
		}
		conFriends.push_back(uiFriend);
	}
	//--------------------- end - algorithm -----------------------


	//--------------------- begin - printing to file ---------------------
	ofstream out;
	out.open(sFileName + ".txt");

	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		out << "Case #" << uiIdx + 1 << ": " << conFriends[uiIdx] << endl;
	}

	out.close();
	//--------------------- end - printing to file -----------------------

	//
	return 0;
}

