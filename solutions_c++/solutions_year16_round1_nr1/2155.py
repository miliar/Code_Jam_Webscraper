#include <iostream>
#include <stdio.h>

//#include <algorithm>
#include <string.h>

using namespace std;

int main()
{
    FILE* in, *out;
    if((in=fopen("A-large.in", "rt"))==NULL)
    {
        cout<<"Input file not found."<<endl;
        getchar();
        return 1;
    }
    if((out=fopen("A-large.out", "wt"))==NULL)
    {
        cout<<"Cannot create output file."<<endl;
        getchar();
        return 2;
    }

    int T;
    fscanf(in, "%d", &T);
    char str[2000], last[2000];
    fgets(str, sizeof(str), in);

    for(int t=0; t!=T; ++t)
    {
        fgets(str, sizeof(str), in);
        strcpy(last, "");
        int size=0;
        for(int i=0; i<strlen(str); ++i)
        {
            if(str[i]>='A' && str[i]<='Z')
                size=i+1;
            else
                break;
        }

        str[size]='\0';

        last[0]=str[0];
        last[1]='\0';

        char toFront[2000], toBack[2000];

        for(int i=1; i<size; ++i)
        {
            toFront[0]=str[i];
            strcpy(toFront+1, last);

            strcpy(toBack, last);
            int temp_size=strlen(toBack);
            toBack[temp_size]=str[i];
            toBack[temp_size+1]='\0';

            if(strcmp(toFront, toBack)>0)
                strcpy(last, toFront);
            else
                strcpy(last, toBack);
        }

        fprintf(out, "Case #%d: %s\n", t+1, last);
    }


    fclose(in);
    fclose(out);
    return 0;
}
