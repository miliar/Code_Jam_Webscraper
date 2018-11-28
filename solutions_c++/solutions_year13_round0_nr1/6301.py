#include <stdio.h>
#include <stdlib.h>

#define MAX_LINE 50

typedef struct
{
    char lines[4][5];
    char* result;
} caseobj;

char xwonStr[] = "X won";
char owonStr[] = "O won";
char drawStr[] = "Draw";
char ncStr[] = "Game has not completed";

int main()
{
    FILE* in = fopen("a.in", "r");
    if (in == NULL)
        exit(1);
    
    //Get fist line in numOfCasesStr
    char numOfCasesStr[MAX_LINE];
    for (int i=0; i < MAX_LINE; i++)
    {
        char c = fgetc(in);
        if (c == '\n' || c == EOF)
        {
            numOfCasesStr[i] = '\0';
            break;
        }
        else
        {
            numOfCasesStr[i] = c;
        }
    }
    //Convert to int
    int numOfCases = atoi(numOfCasesStr);
    
    //Allocate space for cases
    
    caseobj* cases = NULL;
    cases = (caseobj*) calloc(numOfCases, sizeof(caseobj));
    if (cases == NULL)
        exit(2);
    
    /*
    char*** cases = NULL;
    cases = (char***) calloc(numOfCases, sizeof(char**));
    if (cases == NULL)
        exit(2);
    for (int i=0; i < numOfCases; i++)
    {
        cases[i] = NULL;
        cases[i] = calloc(4, sizeof(char**));
        if (cases[i] == NULL)
            exit(3);
        for (int c=0; c < 4; c++)
        {
            cases[i][c] = NULL;
            cases[i][c] = malloc(4+1);
            if (cases[i][c] == NULL)
                exit(4);
            cases[i][c][4] = '\0';
        }
    }*/
    
    
    //Read content from files into cases
    int casenum = 0;
    int casex = 0;
    int casey = 0;
    bool nl = false;
    while (true)
    {
        char c = fgetc(in);
        if (c == '\n')
        { //Newline
            cases[casenum].lines[casex][casey] = '\0';
            if (nl)
            {
                casenum++;
                casex = 0;
                nl = false;
            }
            else
            {
                casex++;
                nl = true;
            }
            casey = 0;
        }
        else if (c == EOF)
        { //Done
            cases[casenum].lines[casex][casey] = '\0';
            break;
        }
        else
        { //Content
            cases[casenum].lines[casex][casey] = c;
            casey++;
            nl = false;
        }
    }
    
    //Close in file
    fclose(in);
    
    //Calculate results
    for (int i=0; i < numOfCases; i++)
    {
        bool xwon = false;
        bool owon = false;
        bool containBlanks = false;
        //Check for blank spots
        for (int l=0; l < 4; l++)
        {
            for (int c=0; c < 4; c++)
            {
                if (cases[i].lines[l][c] == '.')
                    containBlanks = true;
            }
        }
        //Horizontal
        for (int l=0; l < 4; l++)
        {
            char dc = '\0';
            bool trip = false;
            for (int c=0; c < 4; c++)
            {
                if (cases[i].lines[l][c] == 'X')
                {
                    if (dc == '\0')
                    {
                        dc = 'X';
                    }
                    else if (dc == 'O')
                    {
                        trip = true;
                        break;
                    }
                }
                else if (cases[i].lines[l][c] == 'O')
                {
                    if (dc == '\0')
                    {
                        dc = 'O';
                    }
                    else if (dc == 'X')
                    {
                        trip = true;
                        break;
                    }
                }
                else if (cases[i].lines[l][c] == '.')
                {
                    trip = true;
                    break;
                }
            }
            if (!trip)
            {
                if (dc == 'X')
                    xwon = true;
                else if (dc == 'O')
                    owon = true;
                break;
            }
        }
        //Verticle
        for (int l=0; l < 4; l++)
        {
            char dc = '\0';
            bool trip = false;
            for (int c=0; c < 4; c++)
            {
                if (cases[i].lines[c][l] == 'X')
                {
                    if (dc == '\0')
                    {
                        dc = 'X';
                    }
                    else if (dc == 'O')
                    {
                        trip = true;
                        break;
                    }
                }
                else if (cases[i].lines[c][l] == 'O')
                {
                    if (dc == '\0')
                    {
                        dc = 'O';
                    }
                    else if (dc == 'X')
                    {
                        trip = true;
                        break;
                    }
                }
                else if (cases[i].lines[c][l] == '.')
                {
                    trip = true;
                    break;
                }
            }
            if (!trip)
            {
                if (dc == 'X')
                    xwon = true;
                else if (dc == 'O')
                    owon = true;
                break;
            }
        }
        //Diagnal
        char dc = '\0';
        bool trip = false;
        for (int c=0; c < 4; c++)
        {
            if (cases[i].lines[c][c] == 'X')
            {
                if (dc == '\0')
                {
                    dc = 'X';
                }
                else if (dc == 'O')
                {
                    trip = true;
                    break;
                }
            }
            else if (cases[i].lines[c][c] == 'O')
            {
                if (dc == '\0')
                {
                    dc = 'O';
                }
                else if (dc == 'X')
                {
                    trip = true;
                    break;
                }
            }
            else if (cases[i].lines[c][c] == '.')
            {
                trip = true;
                break;
            }
        }
        if (!trip)
        {
            if (dc == 'X')
                xwon = true;
            else if (dc == 'O')
                owon = true;
        }
        dc = '\0';
        trip = false;
        for (int c=0; c < 4; c++)
        {
            if (cases[i].lines[3-c][c] == 'X')
            {
                if (dc == '\0')
                {
                    dc = 'X';
                }
                else if (dc == 'O')
                {
                    trip = true;
                    break;
                }
            }
            else if (cases[i].lines[3-c][c] == 'O')
            {
                if (dc == '\0')
                {
                    dc = 'O';
                }
                else if (dc == 'X')
                {
                    trip = true;
                    break;
                }
            }
            else if (cases[i].lines[3-c][c] == '.')
            {
                trip = true;
                break;
            }
        }
        if (!trip)
        {
            if (dc == 'X')
                xwon = true;
            else if (dc == 'O')
                owon = true;
        }
        
        
        //Output
        if (xwon)
            cases[i].result = xwonStr;
        else if (owon)
            cases[i].result = owonStr;
        else if (containBlanks)
            cases[i].result = ncStr;
        else
            cases[i].result = drawStr;
    }
    
    //Open out file
    FILE* out = fopen("a.out", "w");
    if (out == NULL)
        exit(5);
    
    //Print output
    for (int i=0; i < numOfCases; i++)
    {
        fprintf(out, "Case #%i: %s\n", i+1, cases[i].result);
    }
    
    //Close out file
    fclose(out);
    
    //Free space for cases
    free(cases);
    
    return 0;
}