
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include<stdio.h>

using namespace std;

typedef long long         LL;
typedef vector<long long> VL;
typedef vector<int>       VI;

#define LP(i,s,n)   for(int i = s; i < (n); ++i) 


int main()
{

    int T,result;
    int A,L,n;
    char string[200];
    int sum = 0;
    FILE *fInPtr = freopen("Input.txt","r",stdin);
    FILE *fOutPtr = freopen("Output.txt","w",stdout);

    //read no of test cases
    scanf("%d\n",&T);
    LP(i,1,T+1)
    {
        scanf("%s",string);
        scanf("%d",&n);
        L = strlen(string);
        result = 0;
        LP(j,0,L)
        {
            
            int Lastidx = L - j;
            for(int k=Lastidx;k >= n;k--)
            {
                int cnt = 0;
                for(int m =0;m < k; m++)
                {
                    if(string[m+j] == 'a' || string[m+j] == 'e' ||
                       string[m+j] == 'i' || string[m+j] == 'o' ||
                       string[m+j] == 'u' )
                       {
                            cnt = 0;
                       }
                        else
                        {
                            cnt++;
                        }
                       if(cnt == n)
                       {
                            result++;
                            break;
                       }
                }//m 
                    
                
            }//k
        }//j
            
            
        
        
        
        printf("Case #%d: %d\n",i,result);
        
    }//Test cases

    return 0;
    
}
