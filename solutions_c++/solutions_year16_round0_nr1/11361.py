#include<iostream>
#include<fstream>
using namespace std;
int j=0,test,digits[10],number,digit,k=1,flag=0,input[101];
void storeDigits(int number2)
{
    //temp=number2;
    while(number2>0)
        {
            digit=number2%10;
            for(int i=0;i<=j;i++)
            {
                if(digit==digits[i])
                {
                    flag=1;
                }
            }
            if(flag==0)
            {
                digits[j]=digit;
                j++;
            }
            flag=0;
            number2=number2/10;
        }
}
int main()
{
    ifstream myfile;
    ofstream yourfile;
    myfile.open("C:\\Users\\Pavilion\\Downloads\\A-small-attempt7.in");
    for(int i=0;i<101;i++)
    {
        myfile>>input[i];
    }
    myfile.close();
    yourfile.open("solution6.txt");
    for(int i=1;i<=100;i++)
    {
        if(input[i]!=0)
        {
        for(int i=1;i<10;i++)
        {
            digits[i]=-1;
        }
        j=0;
        while(1)
        {
            storeDigits(k*input[i]);
            if(j==10)
            {
                break;
            }
            k++;
        }
        yourfile<<"Case #"<<i<<": "<<k*input[i]<<"\n";
        k=1;
        }
        else
            yourfile<<"Case #"<<i<<": "<<"INSOMNIA\n";
    }
    //yourfile.close();
}
