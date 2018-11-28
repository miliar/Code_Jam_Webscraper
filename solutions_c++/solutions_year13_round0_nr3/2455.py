#include<iostream>
#include<stdio.h>
using namespace std;

bool pallindrome(long long number)
{
    long long rev = 0;
    long long temp = number;
    while(temp!=0)
    {
        int d = temp%10;
        temp = temp/10;
        rev = rev*10 + d;
    }
    if(rev == number)
        return true;
    return false;
}
long long arr[200];

int main()
{
    long long sq;
    int index = 0 ;
    for(int x = 1 ; x <=2001002 ; x++ )
    {
        sq = (long long)x*x;
        if(pallindrome(x) && pallindrome(sq) == true)
        {
            arr[index++] = sq;
            //cout << x << " " << sq <<"\n";
        }

    }
    //cout <<index;
    int t;
    cin >> t;
    int case_n = 0;
    while(t--)
    {
        case_n++;
        long long a ,b ;
        int start =-1;
        int end = index;
        scanf("%lld%lld" , &a , &b);
        for(int x= 0 ; x< index ; x++)
        {
            if(start ==-1 && arr[x] >=a)
            {
                start =x;
            }
            if(start > -1 && arr[x] > b)
            {
                end = x;
                break;
            }
        }
        cout <<"Case #" <<case_n << ": " << end -start << "\n";
    }


    return 0;

}
