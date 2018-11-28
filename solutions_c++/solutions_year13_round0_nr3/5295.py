#include<fstream>
#include<math.h>
#include<iostream>

using namespace std;

int check_palindrome(unsigned long int num);
int check_square(unsigned long int num1);
void result_check(unsigned long int A,unsigned long int B, fstream &obj, int test_case);

int main()
{
    int T;
    unsigned long int A;
    unsigned long int B;
    fstream in("input.in",ios::in);
    fstream out("output.out",ios::out);
    if(!in || !out)
    {
        return -1;
    }
    else
    {
        while(!in.eof())
        {

            in>>T;
            for(int i=1;i<=T;i++)
            {
                if(in.tellg()==-1) break;
                else
                {
                    in>>A;
                    in>>B;

                    result_check(A,B,out,i);
                }
            }
        }
        in.close();
        out.close();
    }
    return 0;
}

int check_palindrome(unsigned long int num)
{
    unsigned long int rev=0;
    unsigned long int copy=num;
    unsigned long int dig;
    while(num>0)
    {
        dig=num%10;
        rev=rev*10+dig;
        num=num/10;
    };

    if(rev==copy)
     return 1;
     else return 0;
}

int check_square(unsigned long int num1)
{
    unsigned long int sq=sqrt(num1);

    if(check_palindrome(sq)==1 && pow(sq,2)==num1)
    {

        return 1;
    }
    else
    {
        return 0;
    }
}

void result_check(unsigned long int A,unsigned long int B,fstream &obj,int test_case)
{
    unsigned long int num=0;

    while(A<=B)
    {

        if(check_palindrome(A)==1 && check_square(A)==1)
        {
            num++;

        }
        A++;
    };
    obj<<"Case #"<<test_case<<": "<<num<<endl;
}
