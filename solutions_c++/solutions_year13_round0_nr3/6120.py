/*Abram Thiessen
 *COAP 232
 *Assignment 8
 *p490 Q3)
 *18 Mar 2013
 */

#include <iostream>
#include <fstream>

using namespace std;

bool pal(int64_t);
int digits(int64_t);
double root(double num,int r);

int main()
{
    int cases, out;
    int64_t n,j=0,start,finish;
    ifstream inFile;    //input filr
    ofstream outFile;
    inFile.open("C-small-attempt1.in");    //open the file
    outFile.open("square.out");    //open the file
    if (inFile.fail())  //if the file did not open
    {
        cout << "The file did not open";
        return 0;
    }
    inFile>>cases;
    for (int i=1;i<=cases;i++)
    {
        out=0;
        inFile>>start>>finish;
        for (int i=1;i<=start/i;i++)
            n=i*i;
        n=root(start,2);
        if (n*n!=start)
            n++;
        for (n;n*n<=finish;1)
        {
            j=n*n;
            if (pal(n))
            {
                if (pal(j))
                    {out++;}
            }
            n++;
        }
        outFile <<"Case #"<<i<<": "<<out<<endl;
    }
    inFile.close();
    return 0;
}
bool pal(int64_t num)   //this function detertimines if a number is a palindrome
{
    int64_t fmod=1;
    int first,last;
    for (int i=0;i<(digits(num)-1);i++)
        fmod=fmod*10;
    while (1)
    {
        first=num/fmod;
        last=num%10;
        num=num-fmod*first;
        num=num/10;
        fmod=fmod/100;
        if (first==last)
        {
            if (num<10)
                return 1;
        }
        else return 0;
    }
}
int digits(int64_t n)
{
    int64_t i=1;
    int j=0;
    while (i<=n)
    {
        i=10*i;
        j++;
    }
    return j;
}
double root(double num,int r) // this function finds the root of a number to a root r. In the case of this program it is only used for square roots.
{
    double ans=2;
    double chec=0,p;
    int i=0,j=0;
    do
        {
        chec=ans;
        p=1;
        for(i=0;i<(r-1);i++)
            p=p*ans;
        ans=ans-(p*ans-num)/(r*p);
        j++;
        }
    while (p*ans<1e308&&ans!=chec&&j<1000);
    return ans;
}
