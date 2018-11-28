#include<iostream>
#include<sstream>
#include<math.h>
#include<string.h>
using namespace std;
int ispalin(unsigned long long int n)
{
    char *str = new char[15];
    stringstream ss;
    ss<<n;
    ss>>str;
    for (int i=0;i<strlen(str)/2;i++)
    {
        if (str[i]!=str[strlen(str)-i-1])
        {
            delete[] str;
            return 0;
        }
    }
    delete[] str;
    return 1;
}
int main()
{
    unsigned int T, found=0;
    unsigned long long int A, B, sqrtA, sqrtB, palindr[100];
    cin>>T;
    for (int i=0;i<T;i++)
    {
        cin>>A>>B;
        sqrtA = (unsigned long long int)sqrt(A);
        sqrtB = (unsigned long long int)sqrt(B);
        int count=0;
        if (sqrtA*sqrtA<A)
            sqrtA++;
        for (unsigned long long int num = sqrtA; num <= sqrtB; num++)
        {
            if (found>0 && palindr[found-1]>=num)
            {
                for (int m=0;m<found;m++)
                {
                    if(palindr[m]==num)
                    {
                        count++;
                        break;
                    }
                }
            }
            else if (ispalin(num))
            {
                if (ispalin(num*num))
                {   
                    palindr[found]=num;
                    count++;
                    found++;
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<count<<"\n";
    }
    return 0;
}
