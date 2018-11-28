#include "iostream"
#include "string"

void getLastWord(const int& iTC, std::string& currWord)
{
		const char* workingWord = currWord.c_str();
		int len = currWord.length();
		char* outputLastWord = new char[len+1];
		outputLastWord[0] = workingWord[0];
		for(int i = 1; i < len ; ++i)
		{
				if(workingWord[i] < outputLastWord[0])
				{
						outputLastWord[i] = workingWord[i];
				}
				else
				{
						for(int j = i ; j >0 ; --j)
						{
								outputLastWord[j] = outputLastWord[j-1];
						}
						outputLastWord[0] = workingWord[i];
				}
		}
		outputLastWord[len] = '\0';
		std::cout<<"Case #"<<iTC<<": " <<outputLastWord <<std::endl;
		delete [] outputLastWord;
}
int main()
{
				int iNumTCs;
				std::cin>>iNumTCs;
				std::string* words = new std::string[iNumTCs];
				for(int i = 0 ; i < iNumTCs;++i)
				{
								std::cin>>words[i];
				}
				for(int i = 0 ; i < iNumTCs;++i)
								getLastWord(i+1,words[i]);
				delete [] words;
				return 0;
}
