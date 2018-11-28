/* 
 * File:   main.cpp
 * Author: nitin
 *
 * Created on 13 November, 2012, 9:13 PM
 */

#include<iostream>
#include<vector>
#include<fstream>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int palindrome_check(long t)
{
    int i=1,min=0,result,iindex;
    while(t/(i*10)!=0)
    {
        i=i*10;
        min++;
    }
    if (min == 0)
        return 1;
    int number[min+1];
    iindex = 0;
    while(i>=1)
    {
        number[iindex] = t/i;
        t = t%i;
        i = i/10;
        iindex++;
    }
    result = 1;
    for(int i=0;i<min/2+1;i++)
    {
        if(number[i] != number[min-i])
            result = 0;
    }
    return result;
}

int main()
{
    int test,t,result,count,root;
    long higher,lower;
    ifstream myfile ("example.txt");
    myfile>>t;
    test = t;
    while(t--)
    {
        count = 0;
        myfile>>lower>>higher;
        for(int i=lower;i<=higher;i++)
        {
            result = palindrome_check(i);
            if(result){
                root = (int)(sqrt(i));
                if(root*root==i)
                    result = palindrome_check(root);
                else
                    result = 0;
            }
            if(result)
                count++;
        }
        cout<<"Case #"<<test-t<<": "<<count<<"\n";
    }
}