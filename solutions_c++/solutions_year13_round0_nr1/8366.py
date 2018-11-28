#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
using namespace std;

bool debugFlag = false;

#define FOR(i,n) for(int i = 0 ; i < n ; ++i)
#define DEBUG if (debugFlag)


char * get_input(char * filename){
    std::ifstream is(filename);
    // Determine the file length
    is.seekg(0, std::ios_base::end);
    std::size_t size=is.tellg();
    is.seekg(0, is.beg);
    // Create a vector to store the data
    char * input = new char[size];
    // Load the data
    is.read(input, size);
    // Close the file
    is.close();

    return input;
}

char XO(char a, char b, char c, char d){
    int xCount = 0, oCount = 0, tCount = 0;
    char line[4];
    line[0] = a;
    line[1] = b;
    line[2] = c;
    line[3] = d;

    FOR(i, 4){
        switch (line[i]){
            case 'X':++xCount;
                     break;
            case 'O':++oCount;
                     break;
            case 'T':++tCount;
                     break;
            default :return '.';
        }
    }

    if (xCount + tCount == 4 && tCount <= 1)
        return 'X';
    if (oCount + tCount == 4 && tCount <= 1)
        return 'O';
    if ((oCount + xCount + tCount) == 4)
        return 'D';
    return '.';
}

char tttt(char * tp){
    char * count = new char[256];
    memset(count, 0, 256);

    //Rows
    FOR(i, 4){
        count[XO(tp[0 + i * 5], tp[1 + i * 5], tp[2 + i * 5], tp[3 + i * 5])] += 1;
        if (count['X'])
            return 'X';
        if (count['O'])
            return 'O';
    }
    if (count['D'] == 4)
        return 'D';
    DEBUG
        cout << "Count of D : " << (int)count['D'] << endl ;
    //Cols
    FOR(i, 4){
        count[XO(tp[i], tp[i + 5], tp[i + 10], tp[i + 15])]++;
        if (count['X'])
            return 'X';
        if (count['O'])
            return 'O';
    }
    //Diagonals
    count[XO(tp[0], tp[6], tp[12], tp[18])]++;
    count[XO(tp[3], tp[7], tp[11], tp[15])]++;
    if (count['X'])
        return 'X';
    if (count['O'])
        return 'O';

    return '.';
}

int main(){
    int T;
    char * input = get_input("input");
    DEBUG
        cout << input << endl ;

    sscanf(input, "%d", &T);
    DEBUG
        cout << T << endl ;

    int i;
    for(i = 0 ; ; ++i)
        if (input[i] == '\n')
            break;

    char * tttt_ptr = input + i + 1;
    DEBUG
        cout << tttt_ptr << endl ;

    ofstream fout("output");
    int caseN = 1;
    while (*tttt_ptr){
        switch(tttt(tttt_ptr)){
            case('X'):fout << "Case #" << caseN << ": X won" << endl ;
                      break;
            case('O'):fout << "Case #" << caseN << ": O won" << endl ;
                      break;
            case('D'):fout << "Case #" << caseN << ": Draw" << endl ;
                      break;
            default  :fout << "Case #" << caseN << ": Game has not completed" << endl ;
                      break;
        };
        caseN++;
        tttt_ptr += 21;
    }

    return 0;
}


