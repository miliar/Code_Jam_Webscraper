
#include <iostream>
//Library to communicate with user
#include <string>
//Library for strings
#include <fstream>
//Library for file handling
#include <array>
//Library for array handling
using namespace std;

string process(string s)
{
    //This function creates the "reduced" version of the string s, without repeated characters
    string proc = "";
    int siz = s.size(), ch = 0;
    proc += s[0];
    for(int i = 1; i < siz; i++)
    {
        if(proc[ch] != s[i])
        {
            proc += s[i];
            ch++;
        }
    }
    return proc;
}

int charCheck(char base, string* s, int N)
{
    int* qty = new int[N];
    int** dist = new int*[N];
    int i, j, k, score = -1;
    //calculates the quantity of char base in each string
    for (i = 0; i < N; i++)
    {
        for(j = 0; j < s[i].size(); j++)
        {
            if(s[i][j] == base)
            {
                k = j;
                qty[i] = 0;
                while(s[i][k] == base)
                {
                    qty[i]++;
                    s[i][k] = '0';
                    k++;
                }
                break;
            }
        }
    }
    //calculates the distance between each string's quantity of that char
    for(i = 0; i < N; i++)
    {
        dist[i] = new int[N];
        for(j = 0; j < N; j++)
            dist[i][j] = abs(qty[i] - qty[j]);
    }
    //finds the minimal one
    for(i = 0; i < N; i++)
    {
        k = 0;
        for(j = 0; j < N; j++)
            k += dist[i][j];
        if(k < score || score == -1)
            score = k;
    }
    return score;
}

int repeat(fstream* filein, int N)
{
    string* s = new string[N];
    string base = "", temp;
    int i, score = 0;
    (*filein) >> s[0];
    base = process(s[0]);
    //checks whether all strings are reducible to the same string
    for(i = 1; i < N; i++)
    {
        (*filein) >> s[i];
        if(process(s[i]) != base)
            return -1;
    }
    //for each character in the base string
    for(i = 0; i < base.size(); i++)
    {
        score += charCheck(base[i], s, N);
    }
    return score;
}

int main()
{
    int T, i;
    int N, k;
    fstream filein, fileout;
    string s;
    bool g = false;
    /**
    Opens files.
    **/
    do{
        cout << "Please type the name of input file: ";
        cin >> s;
        filein.open(s.c_str(), fstream::in);
        g = filein.good();
        if(!g)
            cout << "There was an error loading the file!" << endl;
    }while(!g);

    g = false;
    do{
        cout << "Please type the name of output file: ";
        cin >> s;
        fileout.open(s.c_str(), fstream::out);
        g = fileout.good();
        if(!g)
            cout << "There was an error loading the file!" << endl;
    }while(!g);

    /**
    Starts operating.
    **/
    filein >> T;                                    //Receives number of test cases
    for(i = 0; i < T; i++)
    {
        fileout << "Case #" << i+1 << ": ";
        //Treats (i+1)th case
        filein >> N;
        k = repeat(&filein, N);
        if(k >= 0)
            fileout << k;
        else
            fileout << "Fegla Won";
        fileout << endl;
    }

    filein.close();
    fileout.close();
    return 0;
}
