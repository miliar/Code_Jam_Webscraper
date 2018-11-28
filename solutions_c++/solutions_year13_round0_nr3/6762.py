#include <iostream>
#include<cmath>
#include<fstream>
#include<string>
#include<sstream>
using namespace std;
bool palindromes(int a);

int main()
{
    int t;
    string manish[100];
    string tos;
   ifstream infile("C-small-attempt1.in");
   int A[100], B[100];
    int d,g=0;
    getline(infile, tos);
    istringstream to(tos);
    to>>t;
    for(int i=0;i<t;i++)
    {
        getline(infile, manish[i]);
        istringstream buffer1(manish[i]);
        if(manish[i].empty())
        {
            A[i]=0;
            B[i]=0;
        }
        else if(!manish[i].empty())
        buffer1>>A[i]>>B[i];
    }
    ofstream outputfile("outputsmall1.txt");
    for(int i=0;i<t;i++)
    {
        d=0;
        if(A[i]<0)
            A[i] = -1*A[i];
        if(B[i]<0)
            B[i]=-1*B[i];

        if(A[i]>B[i])
        {
          int temp4 = A[i];
          A[i]=B[i];
          B[i]=temp4;
        }
        int temp1 = sqrt(A[i]);
        int temp2 = sqrt(B[i]);
        if(sqrt(A[i])>temp1)
            temp1 = temp1 +1;

            if(temp1==0 &&temp2==0)
            {
                outputfile<<"Case #"<<++g<<": "<<""<<endl;
            }
            else{
        for(int r=temp1;r<=temp2;r++)
        {
            if(palindromes(r))
            {
                int temp3 = r*r;
                if(palindromes(temp3))
                {
                    d++;
                }
            }
        }
        outputfile<<"Case #"<<++g<<": "<<d<<endl;
            }
    }
    return 0;
}
bool palindromes(int a)
{
    if(a<10 && a>=0)
    {
        return true;
    }
    else if(a>=10)
    {
    int res = a;
    int man[4];
    bool t = true;
    int i=0;
    while(t)
    {
        man[i] = a%10;
        a=a/10;
        if(a==0)
            t = false;
        i++;
    }

    int zeros = pow(10.0, i-1);
    int num=0;
    for(int j=0;j<i;j++)
    {
        num += man[j]*zeros;
        zeros = zeros/10;
    }
    if(res==num)
    {
        return true;
    }
    else return false;
    }
}
