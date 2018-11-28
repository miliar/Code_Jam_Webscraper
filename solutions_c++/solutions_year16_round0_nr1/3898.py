#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <fstream>
using namespace std;
int main()
{
    ifstream input;
    ofstream output;
    input.open("input.txt");
    output.open("output.txt");
    
    int t;
    input>>t;
    
    for(int i=1 ; i<=t ; i++)
    {
        //output<<"Case #"<<i<<":";
        int long long n;
        int long long arr[10]={0};
        input>>n;
        
        int count=0;
        int long long num = 0;
        if(n==0)
            output<<"Case #"<<i<<": INSOMNIA";
        else
        {
            for(int long long j=1 ; count<10 ; j++)
            {
                num+=n;
                int long long temp=num;
                while(temp)
                {
                    int var = temp%10;
                    temp=temp/10;
                    if(arr[var]==0)
                    {
                        arr[var]=1;
                        count++;
                    }
                }
            }
            output<<"Case #"<<i<<": "<<num;
        }
        
        output<<endl;
    }
    output.close();
    input.close();
    return 0;
} 
