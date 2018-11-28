/* 
 * File:   main.cpp
 * Author: Dayanand
 *
 * Created on 13 April 2013, 11:06
 */

#include <cstdlib>
#include"stdio.h"
#include"math.h"

using namespace std;

/*
 * 
 */
bool IsthenoPalindrome(long long int actual_no)
{
    long long int no = actual_no,j;
    if(actual_no % (long long int)pow(10,1) == 0)
        return false;
    int no_of_digits = 0;
    for(long long int i = 0;;i++)
    {
           if(no/pow(10,i) < 1.00)
           {
               no_of_digits = i;
               break;
           }
               
    }
    long long int test = 0;
    for(j=no_of_digits;j>=1;j--)
    {
        long long int tmp = 0;
        tmp = actual_no % (int)pow(10,1);
        actual_no = (long long int)actual_no / (long long int)pow(10,1);
        test += tmp*(long long int)pow(10,j-1);
    }
    if(test == no)
        return true;
    return false;
}
bool IsthenoSquareanditsrootapalindrome(int i)
{
    long double sqrt_float = sqrt(i);
    long int sqrt_int = (long long int)sqrt(i);
    if((double)sqrt_float == (double)sqrt_int)
    {
        if(IsthenoPalindrome(sqrt_int))
                return true;
    }
    
    return false;
}

int FindFairandSquareNos(long long int first_no,long long int second_no)
{
    long int count = 0;
    for(long long int i = first_no;i<=second_no;i++)
    {
        if(IsthenoPalindrome(i))
           if(IsthenoSquareanditsrootapalindrome(i))
                count++;
        
    }
    return count;
}
int main(int argc, char** argv) {

    int no_of_test_cases;
    freopen("fairandsquare.txt" ,"r+",stdin);
    freopen("fairandsquare_out.txt" ,"w+",stdout);
    scanf("%d\n",&no_of_test_cases);
    for(int i = 0;i<no_of_test_cases;i++)
    {
       long long int first_no;
        long long int second_no;
        scanf("%lld",&first_no);
        scanf("%lld",&second_no);
        long int count = FindFairandSquareNos(first_no,second_no);
        printf("Case #%d: %ld\n",i+1,count);
    }
    return 0;
}

