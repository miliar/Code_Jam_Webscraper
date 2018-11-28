#include <iostream>
#include <stdio.h>
#include <cstring>
#include <list>
using namespace std;

int main()
{
    FILE * inFile;
    FILE * outFile;
    char a[1001];
    int t, s_size;
    inFile = fopen ("A-large.in","r");
    outFile = fopen ("A-small-practice.out","w+");
    fscanf(inFile, "%d", &t);
    list <char> d;
    for(int i = 0; i<t;i++)
    {
        fscanf(inFile, "%s", a);
        s_size = (int)strlen(a);
        d.push_front(a[0]);
        for(int j=1;j<s_size;j++)
        {
            if(d.front()<=a[j])
                d.push_front(a[j]);
            else
                d.push_back(a[j]);
        }
    fprintf(outFile, "Case #%d: ", i+1);
    for (list<char>::iterator it=d.begin(); it != d.end(); ++it)
        fprintf(outFile, "%c", *it);
    fprintf(outFile, "\n");
    d.clear();
    }
    return 0;
}
