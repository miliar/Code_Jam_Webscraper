#include<iostream>
#include<cmath>
#include<string>
#include<cstdio>

using namespace std;

bool isFair(double);
double modulo(double,double);

int main(void)
{
    int A=0, B=0,T=0, cpt=0;
    cin >> T;
    for(int i=0 ; i<T ; i++)
    {
        cpt=0;
        cout << "Case #" << i+1 << ": ";
        cin >>A;
        cin >>B;
        for(double j=A ; j<=B ; j++)
        {
            if(floor(sqrt(j))==sqrt(j))
            {
                if(isFair(j) && isFair(sqrt(j)))
                cpt++;
            }
        }
        cout<<cpt <<endl;
    }
    return 0;
}

bool isFair(double number)
{
    double numberReversed=0;
    int numberOfDigits=floor(log10(number)+1);
    for(int i=1 ; i<=numberOfDigits ; i++)
    {
        numberReversed+=((modulo(number,(pow(10,i)))-modulo(number,(pow(10,i-1))))/pow(10,i-1))*pow(10,numberOfDigits-i);
    }
    return numberReversed==number;
}

double modulo(double a, double b)
{
    double q=floor(a/b);
    double r=a-b*q;
    return r;
}
