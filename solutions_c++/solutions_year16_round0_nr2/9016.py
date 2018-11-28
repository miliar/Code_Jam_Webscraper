#include <iostream>
#include<string>
#include <algorithm>
#include <fstream>

using namespace std;

bool isHappy(string str);
string swapStr(string str, long len);
string changeSign(string str, long len);


int main()
{
    ifstream fin("B-large.in");
    ofstream fout("outputLarge.out");

    long numCase; //number of test cases
    string str,tempStr;
    long flipCount = 0,len = 0;;
    long i;
    fin>>numCase;
    long x=0;

    for(i = 1;i<=numCase;i++)
    {
        fin>>str;
        tempStr = str;

        len = str.length();

        while(!isHappy(str))
        {
            /*
            if((str[0] == '+') && !isHappy(str) && !(flipCount==0) )
            {
                str[0] = '-';
                flipCount++;
            }
            if(isHappy(str))
            {
                break;
            }*/

            while((str[x] != '-') && !isHappy(str))
            {
                x++;
            }
            //cout<<x<<endl;
            if(x!=0)
            {
                if(x==1)
                {
                    str[0] = '-';
                    flipCount++;
                }
                else
                {
                    str = swapStr(str,x);
                    str = changeSign(str,x);
                    flipCount++;
                }
                x=0;

            }

            if(str[len-1]=='-')
            {
                str = swapStr(str,len);
                str = changeSign(str,len);
                flipCount++;
            }

            while((str[x] != '-') && !isHappy(str))
            {
                x++;
            }
            //cout<<x<<endl;
            if(x!=0)
            {
                if(x==1)
                {
                    str[0] = '-';
                    flipCount++;
                }
                else
                {
                    str = swapStr(str,x);
                    str = changeSign(str,x);
                    flipCount++;
                }
                x=0;

            }

            /*
            if((str[0] == '+') && !isHappy(str) )
            {
                str[0] = '-';
                flipCount++;

            }
            if(isHappy(str))
            {
                break;
            }*/
            len--;
        }

        fout << "Case #" << i << ": "<<flipCount <<endl;
        flipCount =0;
        x=0;
    }

    return 0;
}


bool isHappy(string str)
{
    long len=0,count=0;
    len = str.length();
    long i;
    for(i = 0; i< str.length(); i++)
    {
        if(str[i] == '+')
        {
            count++;
        }
    }
    if(count == str.length())
    {
        return true;
    }
    else
    {
        return false;
    }
}

string swapStr(string str, long len)
{
    long i = 0;
    long mid = len/2;
    while(i<mid)
    {
        swap(str[i],str[len-1]);
        len--;
        i++;
    }
    return str;
}

string changeSign(string str, long len)
{
    long i;
    for(i = 0; i<len; i++)
    {
        if(str[i] =='+')
        {
            str[i]= '-';
        }
        else
        {
            str[i] = '+';
        }
    }
    return str;
}
