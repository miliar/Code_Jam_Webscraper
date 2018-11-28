#include<iostream>
#include<fstream>
#include<map>
#include<stdlib.h>
#include<stdio.h>
#include<assert.h>
#include<math.h>

using namespace std;

map<char, char> charmap;

bool palindromes(unsigned long long input)
{
    unsigned long long reverse = 0;
    unsigned long long temp = input;
    while(temp > 0)
    {
        int tmp = temp % 10;
        reverse = reverse *10 + tmp;
        temp = temp / 10;
    }

    if (reverse == input)
        return true;
    else
        return false;
}

void eval( double A, double B, unsigned long long S, unsigned long long T, ofstream& outfile)
{
    unsigned long long num = 0;

    double A_sqrt = sqrt(A);
    double B_sqrt = sqrt(B);

    unsigned long long start;
    unsigned long long end;

    start = (unsigned long long)ceil(A_sqrt);
    end = (unsigned long long)floor(B_sqrt);

    cerr << "start = " << start << " ;  end = " <<  end << endl;

    for(unsigned long long i = start; i <= end; i++)
    {
        if (palindromes(i))
        {
            unsigned long long j = i*i;
            if (j >= S && j <= T)
            {
                if(palindromes(j))
                {
                    num++;
                }
            }
        }
    }

    outfile << num;
    return;
}

int main()
{
    //ifstream infile ("B-small-attempt0.in");
    //ifstream infile ("B-large.in");
    //ifstream infile ("input.txt");
    //FILE* fin = fopen("input.txt", "r");
    //FILE* fin = fopen("C-small-attempt0.in", "r");
    FILE* fin = fopen("C-large-1.in", "r");
    //FILE* fin = fopen("C-large-2.in", "r");
    ofstream outfile;
    outfile.open("output.txt");
    int numTests = 0;
    unsigned long long temp1 = 0;
    unsigned long long temp2 = 0;

    double A = 0;
    double B = 0;

    fscanf(fin, "%d", &numTests);
    for (int i = 0; i < numTests; i++)
    {
        outfile << "Case #" << i+1 << ": ";
        fscanf(fin, "%llu %llu", &temp1, &temp2);

        cerr << "temp1 = " << temp1 << " ;  temp2 = " << temp2 << endl;
        A = (double) temp1;
        B = (double) temp2;
        cerr << "A = " << A << " ;  B = " << B << endl;
        eval(A, B, temp1, temp2, outfile);
        if((i+1) < numTests)
        {
            outfile << "\n";
        }

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
