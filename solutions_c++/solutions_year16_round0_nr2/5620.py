#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void flip (char* stack, int count);

int main(int argc, char *argv[])
{
    FILE *input, *output;
    input=fopen("input", "r");
    output=fopen("output", "w");

    int lines = 0;
    fscanf (input, "%i", &lines);
    printf("Line count: %i\n", lines);

    for (int line=0; line < lines; line++)
    {
        int numCorrect = 0;
        printf("Line %i\n", line);
        char stack[101];
        fscanf (input, "%s", stack);
        int pancakeCount = strlen(stack);
        int flips=0;
        while(numCorrect<pancakeCount)
        {
            //Count correct:
            numCorrect=0;
            for(uint i=0; i < strlen(stack); i++)
            {
                if (stack[pancakeCount-(i+1)]=='+')
                    numCorrect++;
                else
                    break;
            }
            //Count +s on top:
            int top=0;
            for(uint i=0; i < strlen(stack); i++)
            {
                if (stack[i]=='+')
                    top++;
                else
                    break;
            }
            if (numCorrect==pancakeCount)
                break;
            printf("%s numCorrect: %i\n", stack, numCorrect);
            //First flip those on top:
            printf("Flip top %i: ", top);
            flip(stack,top);
            if (top)
                flips++;
            printf("%s\n", stack);
            //Now flip the rest:
            printf("Flip %i: ", pancakeCount-numCorrect);
            flip(stack,pancakeCount-numCorrect);
            if (pancakeCount-numCorrect)
                flips++;
            printf("%s\n", stack);
        }
        printf("Finished Line %i: %s %i, flips: %i\n", line+1, stack, numCorrect, flips);
        fprintf(output, "Case #%i: %i\n", line+1, flips);
    }
    return 0;
}

void flip (char* stack, int count)
{
    if (!count)
        return;
    char temp[count];
    for (int i =0; i < count; i++)
        temp[i]=stack[i];
    for (int i =0; i < count; i++)
        stack[i]=temp[count-(i+1)]=='+'?'-':'+';
}
