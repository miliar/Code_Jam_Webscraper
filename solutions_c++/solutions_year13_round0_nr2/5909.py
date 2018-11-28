#include <Windows.h>

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#include <vector>
#include <map>
#include <set>
#include <list>

int SearchDirectory(
		std::vector<std::string> &refvecFiles,
		const std::string        &refcstrRootDirectory,
		const std::string        &refcstrExtension,
		bool                     bSearchSubdirectories = true)
{
	std::string     strFilePath;             // Filepath
	std::string     strPattern;              // Pattern
	std::string     strExtension;            // Extension
	HANDLE          hFile;                   // Handle to file
	WIN32_FIND_DATA FileInformation;         // File information


	strPattern = refcstrRootDirectory + "\\*." + refcstrExtension;

	hFile = ::FindFirstFile(strPattern.c_str(), &FileInformation);
	if(hFile != INVALID_HANDLE_VALUE)
	{
		do
		{
			if(FileInformation.cFileName[0] != '.')
			{
				strFilePath.erase();
				strFilePath = refcstrRootDirectory + "\\" + FileInformation.cFileName;

				if(FileInformation.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
				{
					if(bSearchSubdirectories)
					{
						// Search subdirectory
						int iRC = SearchDirectory(refvecFiles,
							strFilePath,
							refcstrExtension,
							bSearchSubdirectories);
						if(iRC)
							return iRC;
					}
				}
				else
				{
					refvecFiles.push_back(strFilePath);
				}
			}
		} while(::FindNextFile(hFile, &FileInformation) == TRUE);

		// Close handle
		::FindClose(hFile);

		DWORD dwError = ::GetLastError();
		if(dwError != ERROR_NO_MORE_FILES)
			return dwError;
	}
}

/************************************************************************/
/*                             MAIN                                     */
/************************************************************************/
bool isVerticalCutPossible(size_t columnId, unsigned int height, unsigned int lawn[100][100], size_t rowCount)
{
    for(size_t rowId=0;
        rowId != rowCount;
        ++rowId)
    {
        if (lawn[rowId][columnId] > height)
        {
            return false;
        }
    }
    return true;
}

int main(int argc, const char* argv[])
{
	/*
	 * Selecting input file
	 */
	if(argc < 2)
	{
		std::cerr << "Directory must be provided." << std::endl;
		return -1;
	}

	std::string roundDirectory(argv[1]);

	std::vector<std::string> filesList;
	SearchDirectory(filesList, roundDirectory, "in");

	std::string infilePath;
	if(filesList.size()>1)
	{
		unsigned int fileNumber = 0;
		for(std::vector<std::string>::iterator fileIt = filesList.begin();
			fileIt != filesList.end();
			++fileIt, ++fileNumber)
		{
			std::cout << fileNumber << " : " << *fileIt << std::endl;
		}
		std::cin >> fileNumber;
		infilePath = filesList[fileNumber];
	}
	else if (filesList.size()==1)
	{
		infilePath = filesList[0];
	}
	else
	{
		std::cerr << "No \".in\" file in directory : " << roundDirectory << std::endl;
		return -1;
	}

	std::string filenameBody(
		infilePath.substr(
			infilePath.find_last_of('\\')+1,
			infilePath.size()-infilePath.find_last_of('\\')-4 // -1 -".in".length()
		)
	);

	std::string outfilePath(roundDirectory + '\\' + filenameBody + ".out");

	std::cout << std::endl << "SELECTED FILE : " << infilePath << std::endl;
#ifdef DEBUG
	std::cout << "(" << outfilePath << ")" << std::endl;
#endif

	/*
	 * Reading selected file
	 */
	std::ifstream infile;
	infile.open (infilePath, std::ios::in);

	std::ofstream outfile;
	outfile.open (outfilePath, std::ios::out);


	std::string line;
	getline(infile, line);

	std::istringstream iss(line);

	unsigned int gNbCases;
	iss >> gNbCases;

#ifdef DEBUG
	std::cout << "Nb test cases : " << gNbCases << std::endl;
#endif

	//
	// Init
	//
    unsigned int lawn[100][100];
    unsigned int maxHeightRows[100];
    unsigned int maxHeightCols[100];

	//
	// Cases
	//
	for (unsigned int testId=0;
		testId < gNbCases;
		++testId)
	{
        for (size_t id = 0;
             id < 100;
             ++id)
        {
            maxHeightRows[id]=0;
            maxHeightCols[id]=0;
        }
		/*
		 * Case analysis
		 */
		bool result=true;

		getline(infile, line);
        std::istringstream lawnDefIss(line);
        size_t N, M;
        lawnDefIss >> N >> M;
        

        for(size_t nlineId=0;
            nlineId != N;
            ++nlineId)
		{
    		getline(infile, line);
            std::istringstream lineDefIss(line);
            
            for(size_t mcolId=0;
                mcolId != M;
                ++mcolId)
            {
                unsigned int height;
                lineDefIss >> height;
                lawn[nlineId][mcolId] = height;
                if (height > maxHeightRows[nlineId])
                {
                    maxHeightRows[nlineId] = height;
                }
                if (height > maxHeightCols[mcolId])
                {
                    maxHeightCols[mcolId] = height;
                }
            }
		}

#ifdef DEBUG
        std::cout << std::endl << "Lawn #" << testId << std::endl;
        for(size_t nlineId=0;
            nlineId != N;
            ++nlineId)
		{
            for(size_t mcolId=0;
                mcolId != M;
                ++mcolId)
            {
                std::cout << lawn[nlineId][mcolId];
            }
            std::cout << std::endl;
		}

#endif

        /*for(size_t nlineId=0;
            result && (nlineId != N);
            ++nlineId)
		{
            unsigned int previousHeight = lawn[nlineId][0];
            for(size_t mcolId=1;
                result && (mcolId != M);
                ++mcolId)
            {
                unsigned int currentHeight = lawn[nlineId][mcolId];
                int diff = currentHeight-previousHeight;
                if (diff>0)
                {
                    result = isVerticalCutPossible(mcolId-1, previousHeight, lawn, N);
                }
                else if (diff<0)
                {
                    result = isVerticalCutPossible(mcolId, currentHeight, lawn, N);
                }
                previousHeight = currentHeight;
            }
		} */
        for(size_t nlineId=0;
            result && (nlineId != N);
            ++nlineId)
		{
            for(size_t mcolId=0;
                result && (mcolId != M);
                ++mcolId)
            {
                unsigned int currentHeight = lawn[nlineId][mcolId];
//                 if (currentHeight < maxHeightRows[nlineId])
//                 {
//                     result = isVerticalCutPossible(mcolId, currentHeight, lawn, N);
//                 }
                result = ( (currentHeight == maxHeightRows[nlineId]) || (currentHeight == maxHeightCols[mcolId]) );
            }
		}

#ifdef DEBUG
        std::cout << std::endl << "Result : " << (result ? "YES" : "NO") << std::endl;
#endif

		outfile  << "Case #" << testId+1 << ": " << (result ? "YES" : "NO") << std::endl;


		/************************************************************************/
		/* ENDED CASE                                                           */
		/************************************************************************/
	}
	infile.close();
	outfile.close();
}