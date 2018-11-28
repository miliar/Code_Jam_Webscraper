/**
* Magick Trick - by : Jay Sam Nuel Hechanova
**/

#include <iostream>
#include <sstream>
#include <fstream>

#include <stdlib.h>

int main (int argc, char **argv)
{
	int arrange1[4];
	int arrange2[4];

	std::string caseNo;
    std::string row1;
    std::string row2;
	
	std::string rows;
    std::string tmp;
	
	std::fstream ofs ("magick-trick-small.out", std::fstream::out | std::fstream::app);
	std::fstream ifs ("magick-trick-small.in", std::fstream::in);

	if (ifs.is_open())
	{
		// ask for number of cases
		std::getline(ifs, caseNo);
		
		for (int caseCnt=0; caseCnt<atoi(caseNo.c_str()); caseCnt++)
		{
			std::getline(ifs, row1);

			int rIndx;
			for (rIndx=1; rIndx<=4; rIndx++)
			{
				if (rIndx != atoi(row1.c_str()))
					std::getline(ifs, tmp);
				else
					std::getline(ifs, rows);
			}
			std::istringstream stream1(rows);

			int col1 = 0;
			while (stream1.good())
			{
				stream1 >> arrange1[col1++];
			}
			
			std::getline(ifs, row2);
			
			rows = "";
			for (rIndx=1; rIndx<=4; rIndx++)
			{
				if (rIndx != atoi(row2.c_str()))
					std::getline(ifs, tmp);
				else
					std::getline(ifs, rows);
			}
			std::istringstream stream2(rows);
			
			int col2 = 0;
			while (stream2.good())
			{
				stream2 >> arrange2[col2++];
			}
			
			ofs << "Case #" << caseCnt+1 << ": ";
			
			int found = 0;
			int card = 0;
			for (int aIndx1=0; aIndx1<4; aIndx1++)
			{
				for (int aIndx2=0; aIndx2<4; aIndx2++)
				{
					if (arrange1[aIndx1] == arrange2[aIndx2])
					{
						found++;
						card = arrange1[aIndx1];
					}
				}
			}
			
			switch(found)
			{
				case 0:
					ofs << "Volunteer cheated!" << std::endl;
					break;
				case 1:
					ofs << card << std::endl;
					break;
				default:
					ofs << "Bad magician!" << std::endl;
					break;
			}
		}

		ofs.close();
		ifs.close();
	}
	else
	{
		std::cout << "error opening file";
	}

    return 0;
}