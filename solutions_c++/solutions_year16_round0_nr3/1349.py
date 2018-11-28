#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;


unsigned long long int checkPrime(unsigned long long int t)
{
    for(unsigned long long int i =2;i<=(int)sqrt(t/2);i++)
    {
        if (t%i ==0) return i;
    }
    return 0;
}

unsigned long long int power(int x, int y)
{
    if (y==0) return 1;
    unsigned long long int res =x;
    for (int i=2;i<=y;i++) res = res*x;
    return res;
}

unsigned long long int inBase(bool n[], int t)
{
    unsigned long long int res =0;
    for(int i=15;i>=0;i--)
    {
        res = res + n[i]*power(t,15-i);
    }
    return res;
}



int main()
{
    ofstream opf;
    opf.open("output.txt");
    opf << "Case #1: "<<endl;
    int c =0;
    int n=16;
    int j=50;
    bool bit[17];
    for(int i =0;i<=15;i++) bit[i]=0;
    bit[0] = 1;
    bit[15] = 1;
    bool n1[17];
    for(int i =0;i<=15;i++) n1[i]=0;
    n1[14]=1;
    bit[14] =1;
    while (c!=500)
    {
        bool t =false;
        int tmp =0;
        for(int i=14;i>=1;i--)
        {
            tmp = bit[i]+n1[i]+t;
            t = tmp/2;
            bit[i]= tmp%2;
        }
        t = true;
        long long int nd[11];
        for(int i =2;i<=10;i++)
        {
            nd[i] = checkPrime(inBase(bit,i));
            if (nd[i]==0) {t = false;break;}
        }
        if (t)
        {
            for(int i=0;i<=15;i++) opf << bit[i];
            for(int i=0;i<=15;i++) opf << bit[i];
            opf << " ";
            for (int i=2;i<=10;i++) opf << nd[i] << " ";
            opf<<endl;
            c++;
        }
    }

}
