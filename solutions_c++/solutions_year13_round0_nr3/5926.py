#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

typedef std::vector<std::string>::iterator StrVIter;
typedef std::vector<std::string>::const_iterator ConstStrVIter;

struct Range{
std::string start;
std::string end;
};
// constants
std::vector<std::string> knownBasesofTwo;
// temporary handles
std::vector<std::string> oneFairSquares;
std::vector<std::string> twoFairSquares;
int isThreeBaseIncluded	 = 0;
std::vector<std::string> combinatorialFairSquares;
int* outputs;

inline long long stringToLongLong(const std::string &fValue)
{
	std::stringstream sstr(fValue);
	long long val;
	sstr >> val;
	return val;
}

inline void split(const std::string &s, std::vector<std::string> &elems, char delim=' ')
{
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
}

inline std::string zeroString(int fZeroCount)
{
	std::string ret_val;
	for(int i=0;i<fZeroCount;++i) ret_val.push_back('0');
	return ret_val;
}

inline std::string installZeros(const std::string &fValue, int fZeroCount)
{
	std::string ret_val;
	std::string zeroStr = zeroString(fZeroCount);
	for(int i=0;i<fValue.length();++i){
		ret_val.push_back(fValue[i]);
		if(i==fValue.length()-1)
			break;
		ret_val += zeroStr;
	}
	return ret_val;
}

void clearTemporaryData()
{
	oneFairSquares.clear();
	twoFairSquares.clear();
	isThreeBaseIncluded	 = 0;
	combinatorialFairSquares.clear();
}

void print(std::vector<std::string> list)
{
	for(StrVIter iter=list.begin(); iter!=list.end(); ++iter) {
		long long value = stringToLongLong((*iter).c_str());
		std::cout<<value<<" -- "<<value*value<<std::endl;
	}
}

bool findIfNotExists(const std::vector<std::string> &list, std::string fValue)
{
	for(ConstStrVIter iter=list.begin(); iter!=list.end(); ++iter)
	{
		if( fValue==(*iter) )
			return false;
	}
	return true;
}

int main(int argc, char** argv)
{
	// BEGIN - compute known bases
	knownBasesofTwo.push_back("2");
	knownBasesofTwo.push_back("22");
	knownBasesofTwo.push_back("121");
	knownBasesofTwo.push_back("212");
	knownBasesofTwo.push_back("11211");
	// END - computer known bases

	Range* inputs;
	int numInputs;
	// BEGIN - Read file
	std::ifstream inputFile;
	inputFile.open("C:\\Users\\prady\\Downloads\\C-small-attempt0.in");
	if(inputFile.good())
	{
		std::string currentLine;
		std::getline(inputFile,currentLine);
		numInputs	= stringToLongLong(currentLine.c_str());
		inputs		= new Range[numInputs];
		currentLine.clear();

		for(int inp=0;inp<numInputs; ++inp)
		{
			std::getline(inputFile,currentLine);
			std::vector<std::string> elems;
			split(currentLine,elems);
			inputs[inp].start = elems[0];
			inputs[inp].end = elems[1];
			currentLine.clear();
		}

		if(inputFile.eof())
			std::cout<<"Reached end of file."<<std::endl;
		else
			std::cout<<"Not reached end of file, some extra lines at the end!"<<std::endl;
	}
	inputFile.close();
	// END - Read file

	/*for(int inp=0;inp<numInputs; ++inp)
		std::cout<<inputs[inp].start<<" "<<inputs[inp].end<<std::endl;
	std::cout<<std::endl;*/

	outputs = new int[numInputs];
	// BEGIN - Processing inputs
	for(int inp=0;inp<numInputs; ++inp)
	{
		long long start = stringToLongLong(inputs[inp].start.c_str());
		long long end = stringToLongLong(inputs[inp].end.c_str());		
		// find base fair square numbers
		{
			// find 1*'s
			{
				std::string ones("1");
				long long value = 1;
				char* holder;
				bool firstCondition = (value>=start && value<=end);
				while( firstCondition || value<start ) {
					// second condition is always false once value goes beyond start
					if(firstCondition)
						oneFairSquares.push_back(ones);
					ones.push_back('1');
					long long temp = stringToLongLong(ones.c_str());
					value = temp*temp;
					firstCondition = (value>=start && value<=end); 
				}
			}
			// find *2*'s
			{
				for(int it=0;it<knownBasesofTwo.size();++it){
					long long value = stringToLongLong(knownBasesofTwo[it].c_str());
					long long sqredValue = value*value;
					if(sqredValue>=start && sqredValue<=end)
						twoFairSquares.push_back(knownBasesofTwo[it]);
				}
			}
			// check for 3*3 = 9
			if(9>=start && 9<=end)
				isThreeBaseIncluded=1;
		}
		// find combinations based on the above base fair square numbers
		// now put zeros where ever necessary to produce more palindromes
		{
			if(oneFairSquares.size())
			{
				// loop through oneFairSquares
				for(StrVIter iter=oneFairSquares.begin(); iter!=oneFairSquares.end(); ++iter)
				{
					std::string currStr = *iter;
					if(currStr.length()>1)
					{
						for(int numOfZeros = 1; ; ++numOfZeros)
						{
							std::string newCombin = installZeros(currStr,numOfZeros);
							long long value = stringToLongLong(newCombin.c_str());
							long long sqredValue = value*value;
							if(sqredValue>=start && sqredValue<=end) {
								if(findIfNotExists(combinatorialFairSquares,newCombin))
									combinatorialFairSquares.push_back(newCombin);
							}
							else
								break;
						}
						if(currStr.length()%2==0)
						{
							int mid = currStr.length()/2;
							int mirror = currStr.length()-1-mid;
							for(int numOfZeros = 1; ; ++numOfZeros)
							{
								std::string zeros = zeroString(numOfZeros);
								std::string temp = currStr;
								temp.insert(mid,zeros);
								long long value = stringToLongLong(temp.c_str());
								long long sqredValue = value*value;
								if(sqredValue>=start && sqredValue<=end) {
									if(findIfNotExists(combinatorialFairSquares,temp))
										combinatorialFairSquares.push_back(temp);
								}
								else
									break;
							}
							// Now use original current string and start replacing 1's with 0's as
							// we move from center and then push each such string as it is also a fair sqaure
							if(currStr.length()>2)
							{
								do{
									std::string temp = currStr;
									temp.replace(mid,1,"0");
									temp.replace(mirror,1,"0");
									long long value = stringToLongLong(temp.c_str());
									long long sqredValue = value*value;
									if(sqredValue>=start && sqredValue<=end) {
										if(findIfNotExists(combinatorialFairSquares,temp))
											combinatorialFairSquares.push_back(temp);
									}
									else
										break;
									mid++;
									mirror--;
								}while(mirror>0 && mid<currStr.length()-1);
							}
						} else if(currStr.length()>3)
						{							
							int mid = currStr.length()/2-1;
							int mirror = currStr.length()-1-mid;
							do{
								std::string temp = currStr;
								temp.replace(mid,1,"0");
								temp.replace(mirror,1,"0");
								long long value = stringToLongLong(temp.c_str());
								long long sqredValue = value*value;
								if(sqredValue>=start && sqredValue<=end) {
									if(findIfNotExists(combinatorialFairSquares,temp))
										combinatorialFairSquares.push_back(temp);
								}
								else
									break;
								mid++;
								mirror--;
							}while(mirror>0 && mid<currStr.length()-1);
						}
					}
				}
			}
			if(twoFairSquares.size())
			{
				// loop through twoFairSquares
				for(StrVIter iter=twoFairSquares.begin(); iter!=twoFairSquares.end(); ++iter)
				{
					std::string currStr = *iter;
					if(currStr.length()>1)
					{
						if(currStr.length()%2!=0)
						{
							for(int numOfZeros = 1; ; ++numOfZeros)
							{
								std::string newCombin = installZeros(currStr,numOfZeros);
								long long value = stringToLongLong(newCombin.c_str());
								long long sqredValue = value*value;
								if(sqredValue>=start && sqredValue<=end) {
									if(findIfNotExists(combinatorialFairSquares,newCombin))
										combinatorialFairSquares.push_back(newCombin);
								}
								else
									break;
							}
							// This one case needs special handling
							if(currStr==std::string("11211"))
							{
								bool forBreak=false;
								for(int numOfZeros = 1;!forBreak; ++numOfZeros)
								{
									std::string zeros = zeroString(numOfZeros);
									int ithElem = 1;
									int mirrorElem = currStr.length()-1;
									do{
										std::string temp = currStr;
										temp.insert(mirrorElem,zeros);
										temp.insert(ithElem,zeros);
										long long value = stringToLongLong(temp.c_str());
										long long sqredValue = value*value;
										if(sqredValue>=start && sqredValue<=end) {
											if(findIfNotExists(combinatorialFairSquares,temp))
												combinatorialFairSquares.push_back(temp);
										}
										else {
											forBreak = true;
											break;
										}
										mirrorElem--;
										ithElem++;
									}while(ithElem<mirrorElem);
								}
							}
						}else {
							int mid = currStr.length()/2;
							int mirror = currStr.length()-1-mid;
							for(int numOfZeros = 1; ; ++numOfZeros)
							{
								std::string zeros = zeroString(numOfZeros);
								std::string temp = currStr;
								temp.insert(mid,zeros);
								long long value = stringToLongLong(temp.c_str());
								long long sqredValue = value*value;
								if(sqredValue>=start && sqredValue<=end) {
									if(findIfNotExists(combinatorialFairSquares,temp))
										combinatorialFairSquares.push_back(temp);
								}
								else
									break;
							}
						}						
					}
				}
			}
		}
		outputs[inp] = oneFairSquares.size()+twoFairSquares.size()
						+combinatorialFairSquares.size()+isThreeBaseIncluded;
		print(oneFairSquares);
		print(twoFairSquares);
		print(combinatorialFairSquares);
		std::cout<<"isThreeBaseIncluded: "<<isThreeBaseIncluded<<std::endl;
		std::cout<<"--------------------"<<outputs[inp]<<"--------------------"<<std::endl;
		clearTemporaryData();
	}
	// END - Processing inputs

	//BEGIN - Write to file
	std::ofstream outputFile;
	outputFile.open("C_output_1stlarge_input.txt");
	if(outputFile.good()) {
		for(int inp=0;inp<numInputs; ++inp) {
			outputFile<<"Case #"<<inp+1<<": "<<outputs[inp]<<std::endl;
		}
	}
	outputFile.close();
	//END - Write to file

	// BEGIN - Free memory
	delete[] inputs;
	delete[] outputs;
	// END - Free memory
	system("pause");
	return 0;
}
