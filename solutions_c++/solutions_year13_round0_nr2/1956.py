#include<iostream>
#include<fstream>
#include<map>
#include<stdlib.h>
#include<stdio.h>
#include<assert.h>

using namespace std;

map<char, char> charmap;

void eval(int** lawn, ofstream& outfile, int N, int M)
{
/*
    for (int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            outfile << lawn[i][j]<< " ";
        }
        outfile << "\n";
    }
*/

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            int curr = lawn[i][j];

            bool flag1 = true;
            bool flag2 = true;
            for(int k = 0 ; k < N; k++ )
            {
                if (curr >= lawn[k][j])
                {
                }
                else
                {
                    flag1 = false;
                }
            }
            for(int l = 0; l < M; l++)
            {
                if(curr >= lawn[i][l])
                {
                }
                else
                {
                    flag2 = false;
                }
            }
            if(flag1 == false && flag2 == false)
            {
                outfile << "NO";
                return;
            }
        }
    }

    outfile << "YES";
    return;
}

int main()
{
    char getch;
    //ifstream infile ("B-small-attempt0.in");
    //ifstream infile ("B-large.in");
    //ifstream infile ("input.txt");
    int ** lawn;
    //FILE* fin = fopen("input.txt", "r");
    //FILE* fin = fopen("B-small-attempt0.in", "r");
    FILE* fin = fopen("B-large.in", "r");
    ofstream outfile;
    outfile.open("output.txt");
    int numTests = 0;
    int N = 0;
    int M = 0;

    fscanf(fin, "%d", &numTests);
    cerr << numTests << endl;
    for (int i = 0; i < numTests; i++)
    {
        outfile << "Case #" << i+1 << ": ";
        cerr << "Case #" << i+1 << ": ";
        fscanf(fin, "%d %d", &N, &M);
        cerr << " N = " << N << " , M = " << M << endl;
        lawn = (int**) malloc(N * sizeof(int*));
        for (int j = 0; j < N; j++)
        {
            lawn[j] = (int*) malloc(M * sizeof(int));
            for (int k = 0; k < M; k++)
            {
               int temp = 0;
               fscanf(fin, "%d", &temp);
               lawn[j][k] = temp;
            }
        }

        eval(lawn, outfile, N, M);
        if((i+1) < numTests)
        {
            outfile << "\n";
        }

        for (int j = 0; j<N; j++)
        {
            free(lawn[j]);
        }
        free (lawn);
    }

    //assert(feof(fin));
    fclose(fin);
/*
    if (infile.is_open())
    {
        while (!infile.eof())
        {
            //infile.get(getch);
            getch = infile.get();
            //if ()
            if (getch >= '0' && getch <= '9')
            {
                temp = temp * 10 + getch - '0';
                continue;
            }
            if (getch == '\n' )
            {
                if (index == 0)
                {
                     numlines = temp; 
                }
                else
                {
                    scorearr[(rowindex - 3)] = temp;
                    temp = 0;

                    for (int k = 0; k < numDancers; k++)
                    {
                        cout << scorearr[k] << " : " << lstScore << " : " << numSup << endl;
                        int temp1 = lstScore -1;
                        int temp2 = lstScore -2;
                        if (temp1 < 0)
                            temp1 = 0;
                        if (temp2 < 0)
                            temp2 = 0;
                        if (scorearr[k] >= (lstScore + 2* temp1))
                        {
                            res++;
                        }
                        else
                        {
                            if (numSup > 0)
                            {
                                if (scorearr[k] >= (lstScore + 2*temp2))
                                {
                                    res++;
                                    numSup--;
                                }
                            }                            
                        }
                    }

                    outfile << res <<"\n";

                }
                index++;

                if (index <= numlines)
                {
                    outfile << "Case #" << index << ": ";
                }

                rowindex =0;
                    temp =0;
                    scorearr = NULL; 
                    numDancers = 0;
                    numSup = 0;
                    lstScore = 0;
                    res = 0;

                continue;
            }
            if (getch == ' ')
            {
                if (rowindex == 0)
                {
                    if (index > 0)
                    {
                        numDancers = temp;
                        temp = 0;
                        scorearr = (int *) malloc (numDancers * sizeof(int));                        
                        
                    }
                    rowindex++;
                }
                else if (rowindex == 1)
                {
                    if (index > 0)
                    {
                        numSup = temp;
                        temp = 0;                        
                    }
                    rowindex++;
                }
                else if (rowindex == 2)
                {
                    if (index > 0)
                    {
                        lstScore = temp;
                        temp = 0;
                    }
                    rowindex++;
                }
                else if (rowindex > 2)
                {
                    if (index > 0)
                    {
                        scorearr[(rowindex - 3)] = temp;
                        temp = 0;
                    }
                    rowindex++;
                }
                continue;
            }
        }

    }
    else
    {
        cout << "unable to open file\n";
    }
*/
    return 0;
}
