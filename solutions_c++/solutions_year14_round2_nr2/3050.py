#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
using namespace std;

FILE *input;
FILE *output;

void inputfunction(void);
void processfunction(int A, int B, int K);

int main(void)
{
    input=fopen("/Users/khhan1993/Downloads/B-small-attempt0.in","r");
    output=fopen("/Users/khhan1993/Downloads/output.out","w");
    
    int testcase;
    fscanf(input,"%d", &testcase);
    
    for(int i=0;i<testcase;i++)
    {
        fprintf(output,"Case #%d: ",i+1);
        inputfunction();
    }
    
    fclose(input);
    fclose(output);
    
    return 0;
}

void inputfunction(void)
{
    int A,B,K;
    fscanf(input,"%d %d %d", &A, &B, &K);
    
    processfunction(A,B,K);
}

void processfunction(int A, int B, int K)
{
    int count=0;
    
    for(int i=0;i<A;i++)
    {
        for(int j=0;j<B;j++)
        {
            int temp=i&j;
            //printf("%d ", temp);
            if(temp<K)
                count++;
        }
    }
    
    fprintf(output,"%d\n",count);
}