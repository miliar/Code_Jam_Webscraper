#include<iostream>
#include<fstream>
#include <sstream>
#include<cmath>
#include<string.h>
using namespace std;

char k[1000002];
int flag;

void palin()
{
     int len,i,t,tmp,tmp1;
     len=strlen(k);
     flag=1;

     for(i=0;i<len;i++)
     {
        if(k[i]!='9')
        {
            flag=0;
            break;
        }
     }



    if(flag==1)
    {
        k[0]='1';
        for(i=1;i<len;i++)
          k[i]='0';

        k[len]='1';
        k[len+1]='\0';
        return;
    }

    flag=0;
    for(i=0;i<len/2;i++)
    {
       if(k[i]<k[len-i-1])
       flag=-1;
       else if(k[i]>k[len-i-1] )
       flag=1;

       k[len-i-1]=k[i];
    }


    if(flag==-1 || flag==0)
    {
        t=0;
        if(len%2==0)
        tmp1=len/2-1;
        else
        tmp1=len/2;

        while(k[tmp1-t]=='9')
        {
            k[tmp1-t]='0';
            k[len-1-tmp1+t]='0';
            t++;
        }


        k[tmp1-t]++;
        k[len-1-tmp1+t]=k[tmp1-t];
    }
    return;
}

bool isPalindrome(long long Number)
{

    string Result;          // string which will contain the result
    ostringstream convert;   // stream used for the conversion
    convert << Number;      // insert the textual representation of 'Number' in the characters in the stream
    Result = convert.str();
    for(int i=0,j=Result.size()-1;i<j;i++,j--)
    {
        if(Result[i]!=Result[j])
            return false;
    }
    return true;
}

void setK(long long i)
{
    string Result;          // string which will contain the result
    ostringstream convert;   // stream used for the conversion
    convert << i;      // insert the textual representation of 'Number' in the characters in the stream
    Result = convert.str();
    for(int i=0;i<=Result.size();i++)
    {
        k[i]=Result[i];
    }
}
long long getNo()
{
    long long result=0;
    int i=0;
    while(k[i]!='\0')
    {
        result=result*10+(k[i]-'0');
        i++;
    }
    return result;
}

int main()
{
    ifstream fin("C-large-1.in");
    ofstream fout("out_large.txt");
    int cases;
    long long n,m;
    fin>>cases;
    for(int z=1;z<=cases;z++)
    {
        fin>>n>>m;
        n=ceil(sqrt(n));
        m=sqrt(m);
        setK(n);
        if(!isPalindrome(n))
        {
            palin();
            n=getNo();
        }

        int count=0;
        while(n<=m)
        { //printf("%s\n",k);
            if(isPalindrome(n*n))
                     count++;
            palin();

            n=getNo();
        }

        fout<<"Case #"<<z<<": "<<count<<endl;

    }
}

