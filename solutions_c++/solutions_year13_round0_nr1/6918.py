#include "jamLoader.h"

jamLoader::jamLoader(string filename)
{
	//Open the input file
	inFile.open(filename.c_str());
	if(!inFile)
	{
		success = false;
		cout << "Error opeing file\n";
	}
	else
	{
		success = true;
	}
}

int jamLoader::getSingleInt()
{
	string str;
	getline(inFile,str);
	return atoi(str.c_str());
}

vector<int> *jamLoader::getInts()
{
	//Create the numbers
	vector<int> *integers;
	integers = new vector<int>;

	//
	string str;
	getline(inFile,str);

	//Split into the different characters
	string token;
    istringstream iss(str);
	while(iss.eof() == false)
	{
		iss >> token;
		//Push the new item onto the array
		integers->push_back(atoi(token.c_str()));
	}

	return integers;
}


vector<string*> *jamLoader::getStrings()
{
	//Set up the strings
	vector<string*> *results;
	results = new vector<string*>;

	//
	string str;
	getline(inFile,str);

	//Split into the different characters
	string token;
    istringstream iss(str);
	while(iss.eof() == false)
	{
		iss >> token;
		//Push the new item onto the array
		results->push_back(new string(token));
	}

	return results;
}

vector<string*> *jamLoader::getStringsDelim(char *delim, int numberDelim)
{
	string str;
	getline(inFile,str);

	vector<string*> *strOut = new vector<string*>;

	//Convert all of the delimeters in the string to the same delimeters
	for(int i = 0;i < numberDelim;i++)
	{
		replace(str.begin(),str.end(),delim[i],'~');
	}
	istringstream iss(str);

	for(string item;getline(iss, item,'~');)
	{
		if(item.size() != 0)
		{
			//cout << "Found token: " << item << endl;
			strOut->push_back(new string(item));
		}
	}

	return strOut;
}

string* jamLoader::getString()
{
	string str;
	getline(inFile,str);
	string *newString = new string(str);

	return newString;
}

jamLoader::~jamLoader(void)
{
	if(success = true)
	{
		inFile.close();
	}
}
