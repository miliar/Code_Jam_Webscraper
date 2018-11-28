#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

ifstream fin("p1.in");
ofstream fout("p1.out");
int T;

long long power(long long a, int pow)
{
    int result = 1;
    for(int i=0;i<pow;i++)
    {
        result*=a;
    }
    return result;
}

long long countDigit(long long number)
{
    int i=0;
    for(;number!=0;i++)
    {
        number/=10;
    }
    return i;
}

long long firstHalf(long long number)
{
    long long digit = countDigit(number);
    long long half = (digit/2+digit%2);
    for(int i=0;i<half;i++)
    {
        number/=10;
    }
    return number;
}

long long secondHalf(long long number)
{
    long long digit = countDigit(number);
    long long half = digit/2+digit%2;
    long long result = 0;
    for(int i=0;i<half;i++,number/=10)
    {
        long long curDigit = number%10;
        result+=(curDigit*pow(10,i));
    }
    return result;
}

long long reverse(long long number)
{
    long long digit = countDigit(number);
    long long result = 0;
    for(int i=0;i<digit;i++, number/=10)
    {
        long long curDigit = number%10;
        result += (curDigit*pow(10, digit-i-1));
    }
    return result;
}

long long getBase(long long N)
{
    long long digitNum = countDigit(N);
    return power(10, digitNum-1);
}

bool myclean(long long firsthalf)
{
    for(int i=0;firsthalf!=0;i++, firsthalf/=10)
    {
        long long digit = firsthalf%10;
        if(digit==1)
        {
            if(firsthalf<10)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else if(digit==0)
        {
            continue;
        }
        else
        {
            return false;
        }
    }
    return false;
}

long long solve(long long N)
{
    long long digitNum = countDigit(N);
    long long base = getBase(N);
    long long result = 0;
    if(digitNum==1)
    {
        return N;
    }
    long long firsthalf = firstHalf(N);
    long long secondhalf = secondHalf(N);
    
    if(secondhalf==0)
    {
        result+=(solve(N-1));
        result++;
        return result;
    }
    

    if(myclean(firsthalf))
    {
        result+=secondhalf;
    }
    else
    {
        result+=(reverse(firsthalf));
        result++;
        result+=(secondhalf-1);

    }


    result+=(solve(base));
    return result;

}

int main()
{
    fin>>T;
    for(int curcase=0;curcase<T;curcase++)
    {
        long long N;
        long long result = 1;
        fin>>N;
        //cout<<countDigit(10)<<' '<<countDigit(325)<<' '<<countDigit(5)<<'\n';
        cout<<firstHalf(1245)<<' '<<firstHalf(9)<<' '<<firstHalf(10021)<<'\n'; 
        cout<<secondHalf(1245)<<' '<<secondHalf(9)<<' '<<secondHalf(10021)<<'\n'; 
        //cout<<reverse(9)<<' '<<reverse(12345678)<<' '<<reverse(123000)<<'\n';
        cout<<getBase(956)<<' '<<getBase(10)<<'\n';
        cout<<myclean(1000)<<' '<<myclean(100)<<' '<<myclean(1230)<<'\n';
        result = solve(N);
        fout<<"Case #"<<curcase+1<<": "<<result<<'\n';
    }    
}
