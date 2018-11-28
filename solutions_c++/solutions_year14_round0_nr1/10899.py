#include <iostream>
#include <fstream>

int main(int argc, char* argv[])
{
	if (argc < 2) return -1;

	std::string sFile = argv[1];

	// read file
	std::ifstream file;
	file.open(sFile, std::ios::in|std::ios::binary);

	std::ofstream resultFile("result.txt",std::ios::binary);

	int caseNum = 0;
	file>>caseNum;

	int matrix1[4 * 4]={0};
	int matrix2[4 * 4]={0};
	for(int i = 0; i < caseNum; ++i)
	{
		// read row num in arrangement first
		int rowNumInFirst = -1;
		file>>rowNumInFirst;

		int j = 0;
		// read data to matrix
		for(; j <4; ++j)
		{
			file>>matrix1[j*4+0]>>matrix1[j*4+1]>>matrix1[j*4+2]>>matrix1[j*4+3];
		}

		// read row num in arrangement second
		int rowNumInSecond = -1;
		file>>rowNumInSecond;

		// read data to matrix
		for(j=0;j<4;++j)
		{
			file>>matrix2[j*4+0]>>matrix2[j*4+1]>>matrix2[j*4+2]>>matrix2[j*4+3];
		}

		if (rowNumInFirst<=0||rowNumInFirst>4||rowNumInSecond<=0||rowNumInSecond>4)
			return -2;

		int sameCount = 0;
		int sameValue=-1;
		for(int m=0;m<4;++m)
		{
			for(int n=0;n<4;++n)
			{
				if (matrix1[(rowNumInFirst-1)*4+m]==matrix2[(rowNumInSecond-1)*4+n])
				{
					sameCount++;
					sameValue=matrix1[(rowNumInFirst-1)*4+m];
					break;
				}
			}
			if (sameCount>=2)  break;
		}

		// Output result
		//std::cout<<"Case #"<<i+1<<": ";
		resultFile<<"Case #"<<i+1<<": ";
		if (sameCount==0)
		{
			//std::cout<<"Volunteer cheated!" << std::endl;
			resultFile<<"Volunteer cheated!" << "\n";
		}
		else if (sameCount==1)
		{
			//std::cout << sameValue << std::endl;
			resultFile << sameValue  << "\n";
		}
		else if (sameCount > 1)
		{
			//std::cout << "Bad magician!" << std::endl;
			resultFile << "Bad magician!"  << "\n";
		}
	}
	file.close();
	resultFile.close();
	return 0;
}

