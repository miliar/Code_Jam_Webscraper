#include<iostream>
#include<map>
#include<math.h>

using namespace std;

int rev_num(int num)
{
    int rev=0;
    while(num)
    {
        rev = rev*10 + num % 10;
        num = num /10;
    }
   
    return rev;
}

long long rev_num(long long num)
{
    long rev=0;
    while(num)
    {
        rev = rev*10 + num % 10;
        num = num /10;
    }
    return rev;
}

int compute_numbers(int lower, int higher)
{
    long long square;
    int count = 0;
    for(int i = lower; i<=higher; i++)
    {   
        if(rev_num(i) == i)
        {
            square = i * i;
            if(square == rev_num(square))   
            {
                count++;
            }
        }
    }
    return count;
}

int main()
{
    int num_cases;
    int count = 0;
    int count_pal = 0;
    long long lower, higher;    
    int lower_rt, higher_rt;
    cin>>num_cases;

    while(count < num_cases)
    {
         cin>>lower>>higher;
         lower_rt =  ceil(sqrt(lower));           
         higher_rt = sqrt(higher);
         count_pal = compute_numbers(lower_rt, higher_rt);
         cout<<"Case #"<<++count<<": "<<count_pal<<"\n";
    }
}
