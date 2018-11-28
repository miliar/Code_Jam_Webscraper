#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define square(A) A*A

using namespace std;

bool isPalindrome(long m)
{
    char str[101];
    int length,i;
    ltoa(m,str,10);
    length=strlen(str);
    for(i=0; i<length/2; i++)
    {
        if(str[i]!=str[length-i-1])
            break;
    }
    if(i == length/2)
        return true;
    else return false;

}

int main()
{
    freopen("C:/Users/Doris/code practise/google-jam-2/a.in", "r", stdin);
    freopen("C:/Users/Doris/code practise/google-jam-2/b.out", "w", stdout);
    int t, n, count=0;
    long A, B;
    cin>>t;
    n=t;
    while(t--)
    {
        cin>>A>>B;
        for(long i=1; square(i)<=B; i++)
        {
            if( isPalindrome(i) && isPalindrome(square(i)) && square(i)>=A)
                count++;

        }
        cout<<"Case #"<<n-t<<": "<<count<<endl;
        count=0;
    }
    return 0;
}
