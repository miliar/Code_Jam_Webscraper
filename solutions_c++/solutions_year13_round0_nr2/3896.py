#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

typedef char LineType[MAX_LINE_LEN];    // MAX_LINE is defined outside to match the problem needs

// exposed API 
bool readLine(LineType a_line, FILE* a_hInput = stdin);
int  readNumLine(FILE* a_hInput);

char* readFirstToken(LineType a_line);
char* readNextToken();
char* skipToken(char* a_line);  // return the next token

int    readFirstNum(LineType a_line);
int    readNextNum();
double readFirstD(LineType a_line);
double readNextD();

#ifdef STL
    void readLineOfNums(int N, vector<int>&    a_list);
    void readLineOfD   (int N, vector<double>& a_list);
#endif

///////////////////////////////////////////////////////////////////////////////
bool setStdinFromFile(char* a_pFilename);
bool setStdoutToFile (char* a_pFilename);

////////////////////////////// Implementation /////////////////////////////////

inline bool readLine(LineType a_line, FILE* a_hInput)
{
    char* ret = fgets(a_line, sizeof(LineType), a_hInput);
    if (ret == NULL)
        return false;

    return true;
}

inline int readNumLine(FILE* a_hInput = stdin)
{
    LineType line;
    bool fOk = readLine(line, a_hInput);
    assert(fOk);
    if (! fOk)
        return 0;

    int num; 
    sscanf_s(line, "%d", &num);
    return num;
}

//////////////////////////// Tokens /////////////////////////
static char* next_token;

inline char* readFirstToken(LineType a_line)
{
    return strtok_s(a_line, " ", &next_token);  
}

inline char* readNextToken()
{
    return strtok_s(NULL, " ", &next_token);
}

inline int readFirstNum(LineType a_line)
{
    char* token = readFirstToken(a_line);  
    return atoi(token);
}

inline double readFirstD(LineType a_line)
{
    char* token = readFirstToken(a_line);  
    return atof(token);
}

inline int readNextNum()
{
    char* token = readNextToken();
    return atoi(token);
}

inline double readNextD()
{
    char* token = readNextToken();
    return atof(token);
}

inline char* skipToken(char* a_line)   // return the next token
{ 
    while ((*a_line != 0) && (*a_line != 32))
        ++a_line;

    return ++a_line;
}

#ifdef STL

template<class CTYPE>
void readLineOfElements(int N, vector<CTYPE>& a_list, char* a_format)
{
    a_list.clear();

    CTYPE element; 
    for (int i=0; i<N; i++)
    {
        scanf_s(a_format, &element);
        a_list.push_back(element);
    }

    LineType dummy;
    gets_s(dummy, sizeof(dummy));
}

void readLineOfNums(int N, vector<int>& a_list)
{
    readLineOfElements<int>(N, a_list, "%d");
}

void readLineOf64(int N, vector<__int64>& a_list)
{
    readLineOfElements<__int64>(N, a_list, "%I64d");
}

void readLineOfD(int N, vector<double>& a_list)
{
    readLineOfElements<double>(N, a_list, "%lf");
}

#endif

//////////////////////////////////////////////////////////////////

inline bool setStdinFromFile(char* a_pFilename)
{
    FILE* hInput;
    errno_t err = fopen_s(&hInput, a_pFilename, "r");
    assert(err == 0);
    if (err != 0)
        return false;

    *stdin = *hInput;
    return true;
}

inline bool setStdoutToFile(char* a_pFilename)
{
    FILE* hOutput;
    errno_t err = fopen_s(&hOutput, a_pFilename, "w");
    assert(err == 0);
    if (err != 0)
        return false;

    *stdout = *hOutput;
    return true;
}
