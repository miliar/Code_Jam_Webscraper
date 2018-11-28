#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
//for small dataset: brute force
//1 ≤ T ≤ 100.
//1 ≤ A ≤ B ≤ 1000.
bool isSqure(int num)
{
    double tmp = num;
    double sqrttmp = sqrt(num);
    int sr = int(sqrttmp);
    if(sqrttmp == sr)
        return true;
    else
        return false;
}
bool isFair(int num)
{
    int num_digits[4];
    int count = 0;
    while(num>0)
    {
        num_digits[count] = num%10;
        num /= 10;
        count++;
    }
    for(int i=0;i<count/2;i++)
    {
        if(num_digits[i] != num_digits[count-1-i])
            return false;
    }
    return true;
}
int main()
{
    ifstream datain("C-small-attempt0.in");
    ofstream dataout("C-small-attempt0.out");
    int T;
    datain>>T;
    for(int k=1;k<=T;k++)
    {
        int A,B;
        datain>>A>>B;
        int count = 0;
        for(int num=A;num<=B;num++)
        {
            if(isSqure(num))
            {
                int sr = sqrt(num);
                if(isFair(num) && isFair(sr))
                    count++;
            }
        }
        dataout<<"Case #"<<k<<": "<<count<<endl;
    }

    return 0;
}
