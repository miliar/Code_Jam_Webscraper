// TicTacToeTomek.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define xwin      1
#define owin      2
#define finish    3
#define nofinish  4

char tic[4][5] = {
                    {'.','.','.','.','\0'},
                    {'.','.','.','.','\0'},
                    {'.','.','.','.','\0'},
                    {'.','.','.','.','\0'}
                };
int check()
{
	int k = 0;
    int xPatern[16];
    int oPatern[16];
    int tPatern[16];

	memset(xPatern,0,sizeof(xPatern));
	memset(oPatern,0,sizeof(oPatern));
	memset(tPatern,0,sizeof(tPatern));

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (tic[i][j] == 'X' || tic[i][j] == 'T')
            {
                xPatern[j + k] = 1;
                tPatern[j + k] = 1;
            }
            if (tic[i][j] == 'O' || tic[i][j] =='T')
            {
                oPatern[j + k] = 1;
                tPatern[j + k] = 1;
            }
        }
        k += 4;
    }


    for (int i = 0,j = 0,y = 0; i < 16; y+=4,i=y,j=y)
    {
        if (xPatern[i] == 1 && xPatern[++i] == 1 && xPatern[++i] == 1 && xPatern[++i] == 1)
        {
            return xwin;
        }
        if (oPatern[j] == 1 && oPatern[++j] == 1 && oPatern[++j] == 1 && oPatern[++j] == 1)
        {
            return owin;
        }
    }

            
    for (int j = 0; j < 4; j++)
    {
        int kj = 4;
        if (xPatern[j] == 1 && xPatern[j + (kj * 1)] == 1 && xPatern[j + (kj * 2)] == 1 && xPatern[j + (kj * 3)] == 1)
        {
            return xwin;
        }
        if (oPatern[j] == 1 && oPatern[j + (kj * 1)] == 1 && oPatern[j + (kj * 2)] == 1 && oPatern[j + (kj * 3)] == 1)
        {
            return owin;
        }
    }

            
    int sj = 5;
    int s = 0;
    if (xPatern[s * sj] == 1 && xPatern[s + (sj * 1)] == 1 && xPatern[s + (sj * 2)] == 1 && xPatern[s + (sj * 3)] == 1)
    {
        return xwin;
    }

    if (oPatern[s * sj] == 1 && oPatern[s + (sj * 1)] == 1 && oPatern[s + (sj * 2)] == 1 && oPatern[s + (sj * 3)] == 1)
    {
        return owin;
    }

    sj = 3;
    s = 3;
    if (xPatern[s] == 1 && xPatern[s + (sj * 1)] == 1 && xPatern[s + (sj * 2)] == 1 && xPatern[s + (sj * 3)] == 1)
    {
        return xwin;
    }

    if (oPatern[s] == 1 && oPatern[s + (sj * 1)] == 1 && oPatern[s + (sj * 2)] == 1 && oPatern[s + (sj * 3)] == 1)
    {
        return owin;
    }

	int end = 0;
    for (int i = 0; i < 16; i++)
        if (tPatern[i] == 1)
            end++;
    if(end >= 15)
        return finish;
    else
        return nofinish;
}

int _tmain(int argc, _TCHAR* argv[])
{
	string STRING;
    ifstream infile;
    infile.open ("A-small-attempt1.in");
    int a = 0, i = 0;
	int firstLine = 0;
	int T = 0, result = 0, count = 0;
    string previousLine="";

	ofstream Outputfile;
	Outputfile.open ("F:\\txet3.txt");
    while(a<1) // To get you all the lines.
    {
        getline(infile,STRING); // Saves the line in STRING.

            previousLine=STRING;
            cout<<STRING<<endl; // Prints our STRING.
			
			if(!firstLine)
			{
				T = atol(STRING.c_str());
				firstLine = 1;
			}
			
			else if(firstLine && STRING.length() > 0)
			{
				int j = 0;
				while(j < STRING.length())
				{
					tic[i][j] = STRING[j];
					j++;
				}

				if(i >= 3)
				{
					result = check();

					char strResult[100] ;
					memset(strResult,'\0',sizeof(strResult));
					switch(result)
					{
					case xwin:
						sprintf(strResult,"Case #%d: X won\n",count+1);
						break;
					case owin:
						sprintf(strResult,"Case #%d: O won\n",count+1);
						break;
					case finish:
						sprintf(strResult,"Case #%d: Draw\n",count+1);
						break;
					case nofinish:
						sprintf(strResult,"Case #%d: Game has not completed\n",count+1);
						break;
					}

					strResult[strlen(strResult)]='\0';
					Outputfile << strResult;


					memset(strResult,'\0',sizeof(strResult));
					i = 0;result = 0;
					++count;
					memset(tic,'\0',sizeof(tic));
				}
				else
					i++;
			}
			
			if(count == T) break;

    }
    infile.close();
	Outputfile.close();
	return 0;
}

