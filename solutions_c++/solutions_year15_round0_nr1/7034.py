#ifdef _WIN32
    #include <conio.h>
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <string>
#include <iostream>
#include <istream>
#include <ostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <stack>
#include <vector>
#include <list>
#include <regex>
#include <random>
#include <chrono>
#include <algorithm>
using namespace std;

typedef signed int      S32;
typedef unsigned int    U32;
typedef unsigned short  U16;
typedef unsigned char   U8;

ifstream inputfile;
string input_string;

int get_input()
{
    input_string.clear();
    getline(cin, input_string);
    return 0;
}

void tokenize(string line, vector<string> &results)
{
    // construct a stream from the string
    stringstream str(line);

    // use stream iterators to copy the stream to the vector as whitespace separated strings
    istream_iterator<string> iterat(str);
    istream_iterator<string> end;
    results = vector<string>(iterat, end);
}

template<class TYPE>
TYPE** create_2D_Array(S32 row, S32 col)
{
    TYPE** arr = (TYPE**) malloc(row * sizeof(TYPE*)); //Array of pointers, each shd point to an array
    for(int i = 0; i < row; i++)
    {
        arr[i] = (TYPE*) malloc(col * sizeof(TYPE)); //Array of data
        memset(arr[i], 0, col * sizeof(TYPE));
    }

    return arr;
}

template<class TYPE>
void delete_2D_Array(TYPE** &array, S32 row)
{
    for(int i = 0; i < row; i++)
        free(array[i]);
    free(array);
}

template<class TYPE>
void delete1DimArray(TYPE* array)
{
    free(array);
}

template<class TYPE>
TYPE* create1DimArray(S32 size)
{
    TYPE* arr = (TYPE*) malloc(size * sizeof(TYPE)); //Array of data    
    memset(arr, 0, (size * sizeof(TYPE)));
    return arr;
}

template<class TYPE>
void show_1D_array(vector<TYPE> &data_array, S32 input_size, const char* stringToShow)
{
    if(!data_array.size() || !input_size || !stringToShow)
        return;

    cout << endl;
    printf("%s \n", stringToShow);
    for(int iterate = 0; iterate < input_size; iterate++)
        cout << data_array[iterate] << " ";
    cout << endl;
}

template<class TYPE>
void show_2D_Array(TYPE** array, S32 row, S32 col)
{
    for(int i = 0; i < row; i++)
    {
        for(int j = 0; j < col; j++)
            cout << array[i][j] << " ";
        cout << endl;
    }
}

char** get_2D_Array_with_chars(int rows, int cols)
{
    char** input_array = create_2D_Array<char>(rows, cols);

    for(int i = 0; i < rows; i++)
    {
        get_input();
        for(int j = 0; j < cols; j++)
            input_array[i][j] = (char)input_string[j];
    }

    return input_array;
}

S32** get_2D_Array_with_integers(int rows, int cols)
{
    S32** input_array = create_2D_Array<S32>(rows, cols);

    for(int i = 0; i < rows; i++)
    {
        get_input();
        vector<string> tokens;
        tokenize(input_string, tokens);

        for(int j = 0; j < tokens.size(); j++)
        {
            char* pEnd;
            input_array[i][j] = strtol(tokens[j].c_str(), &pEnd, 10);
        }
    }

    return input_array;
}

void just_get_integer_input(string &input_string, vector<S32> &data)
{
    vector<string> tokens;
    tokenize(input_string, tokens);

    data.clear();
    data.resize(tokens.size());

    if(*input_string.c_str() == '*')
    {
        data[0] = 42;
        return;
    }

    for(int i = 0; i < tokens.size(); i++)
    {
        char* pEnd;
        data[i] = strtol(tokens[i].c_str(), &pEnd, 10);
    }
}

int runTestCase(int SMAX, char* audience)
{
	int total_count			= SMAX+1;//No need to do strlen
	int current_stand_count = 0;
	int friends_needed		= 0;

	if(total_count == 1)
		return 0;

#if 0
	printf("SMAX: %d \n", SMAX);
	printf("Audience: %s \n", audience);
	printf("total_count: %d \n", total_count);
#endif

	for (int i  = 0; i < total_count; i++)
	{
		int inThisRow = audience[i] - '0';
		if(!inThisRow)
			continue;

#if 0
		printf("\n Index: %d, inThisRow: %d \n", i, inThisRow);
		printf("BEFORE: current_stand_count: %d, friends_needed: %d \n", current_stand_count, friends_needed);
#endif

		int extra_needed = 0;
		if(i > current_stand_count)
			extra_needed = abs(i - current_stand_count);

		current_stand_count += inThisRow + extra_needed;
		friends_needed      += extra_needed;

#if 0
		printf("AFTER: extra_needed: %d, current_stand_count: %d, friends_needed: %d \n", extra_needed, current_stand_count, friends_needed);
		_getch();
#endif
	}

	return friends_needed;
}

//#define LOCAL

int main()
{
	ofstream outFile("C:\\Repos\\Git\\micmgmt\\MY_PROGRAMS\\Data structures\\COMPETE\\Problems\\CodeJam\\Problems\\2015\\Shyness\\output.txt");
	//ifstream inputfile("C:\\Repos\\Git\\micmgmt\\MY_PROGRAMS\\Data structures\\COMPETE\\Problems\\CodeJam\\Problems\\2015\\Shyness\\io\\input.txt");
	ifstream inputfile("C:\\Users\\bkosaraj\\Downloads\\A-large.in");
	

	if(!inputfile.is_open() || !outFile.is_open())
    {
        cout << "Files operations failed" <<endl;
        _getch();
        return -1;
    }

	vector<int> readData;
	getline(inputfile, input_string);
	just_get_integer_input(input_string, readData);
	int testCases = readData[0];
	
	//cout << "Number of test cases " << testCases << endl;

	for(int testCaseNo = 1; testCaseNo <= testCases; testCaseNo++)
	{
		string input_string;
		getline(inputfile, input_string);

		char* pch;
		pch = strtok((char*)input_string.c_str(), " ");
		int SMAX = atoi(pch);

		char* audience = strtok (NULL, " ");

		int friends_needed = 0;
		if(SMAX)
			friends_needed = runTestCase(SMAX, audience);

#ifdef LOCAL
		cout    << "Case #" << testCaseNo << ": " << friends_needed;
#endif
		outFile << "Case #" << testCaseNo << ": " << friends_needed;
		outFile.flush();

		if(testCaseNo < testCases)
		{
#ifdef LOCAL
			cout	<< endl;
#endif
			outFile << endl;
			outFile.flush();
		}
	}

#ifdef LOCAL
	_getch();
#endif
}
