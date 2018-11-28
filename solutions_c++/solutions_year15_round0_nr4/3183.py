#include <iostream>
#include <fstream>

using namespace std;
int main()
{
    int T, X, R, C;
    FILE *fp = fopen("D-small-attempt5.in", "r");
    FILE *op = fopen("out.txt", "w");
    if(fp == NULL) return -1;

    fscanf(fp, "%d", &T);
    for(int i =0; i < T; i++)
    {
        fscanf(fp, "%d %d %d", &X, &R, &C);
        if((R*C == 3 || R*C == 4) &&(X==3 || X==4))
        {
            fprintf(op, "Case #%d: RICHARD\n", i+1);
            continue;
        }
        if(R*C == 8 && X == 4)
        {
            fprintf(op, "Case #%d: RICHARD\n", i+1);
            continue;
        }
        if(X> R*C)
        {
            fprintf(op, "Case #%d: RICHARD\n", i+1);
        }
        else
        {
            if((R*C)%X != 0)
            {
                fprintf(op, "Case #%d: RICHARD\n", i+1);
            }
            else
            {
                fprintf(op, "Case #%d: GABRIEL\n", i+1);
            }
        }
    }
    fclose(fp);
}
