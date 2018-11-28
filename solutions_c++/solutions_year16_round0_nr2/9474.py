/*
Google CodeJam - Qualification Round
Problem B: Revenge of the Pancakes - small input
Author: Matei Iancu
*/
#include <cstring>
#include <string.h>
#include <stdio.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

bool checkHappyStack(char *stack);
void reverseStack(char *stack, int index);

int main()
{
	int i, noTests, rIndex, noOperations;
    char pancakesStack[101];
    	
	
	freopen("B-large.in.txt", "rt", stdin);
	freopen("B-large-output.out.txt", "wt", stdout);
	
	cin>>noTests;
	
	for(i = 0; i < noTests; i++)
	{
		cin>>pancakesStack;
        
        noOperations = 0;
        
        while(!checkHappyStack(pancakesStack))
        {
            for(int j = strlen(pancakesStack) - 1; j >= 0; j--)
            {
                if(strncmp(&pancakesStack[j], "-", 1) == 0)
                {;
                    if(strncmp(&pancakesStack[0], "-", 1) == 0)
                    {
                        reverseStack(pancakesStack, j);
                        noOperations++;
                        break;
                    }
                    else
                    {
                        if(strncmp(&pancakesStack[j-1], "+", 1) == 0)
                        {
                            reverseStack(pancakesStack, j-1);
                            noOperations++;
                            break;
                        }
                    }
                }
            }
        }
		
        cout<<"Case #"<<i + 1<<": "<<noOperations<<"\n";   
	}
	
	fclose(stdin);
	fclose(stdout);
}

bool checkHappyStack(char *stack)
{
    for(int i = 0; i < strlen(stack); i++)
    {
        if(strncmp(&stack[i], "-", 1) == 0)
            return false;
    }
    return true;
}

void reverseStack(char *stack, int index)
{
    int k;
    char buff[101];
    k = 0;
    for(int i = index; i >= 0; i--)
    {
        if(strncmp(&stack[i], "+", 1) == 0)
        {
            buff[k] = '-';
        }
        else
        {
            buff[k] = '+';
        }
        k++;
        // buff[i] = (strcmp(&stack[i], "+"))?'-':'+';
    }
    
    strncpy(stack, buff, index + 1);
    // for(int i = 0; i < index; i++)
    // {
    //     strncpy(&stack[i], &buff[index-i-1], 1);
    //     // stack[i] = buff[index - i - 1];
    // }
    // if(index == 0)
    //     strncpy(&stack[0], &buff[0], 1);
        // stack[0] = buff[0];
}
