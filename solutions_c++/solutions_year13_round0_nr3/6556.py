#include<stdio.h>
#include<fstream>
#include<iostream>
#include<math.h>
bool isPalindrone(int x)
{
    int arr[100];
    int length=0;
    int i=0;
    while(x>0)
    {
        arr[i]=x%10;
        length++;
        x/=10;
        i++;
    }
    length--;
    for(i=0;i<length;i++,length--)
    {
        if(arr[i]!=arr[length])
            return false;
    }
    return true;
}
int main()
{
    int nooftest=0,i,a,b,answer=0;
    std::fstream reader;
    std::fstream writer;
    reader.open("C:\\Users\\Parth\\Downloads\\C-small-attempt1.in");
    writer.open("C:\\Users\\Parth\\Desktop\\output.txt");
    char str[1000];
    reader>>str;
    i=0;
    while(str[i]!='\0')
    {
        nooftest*=10;
        nooftest+=((int)str[i])-48;
        i++;
    }
    int n=nooftest;
    while(n>0)
    {
        answer=0;
        a=0;b=0;
        reader>>str;
        std::cout<<str<<"\n";
        i=0;
        while(str[i]!='\0')
        {
            a*=10;
            a+=str[i]-48;
            i++;
        }
        i=0;
        reader>>str;
        while(str[i]!='\0')
        {
            b*=10;
            b+=str[i]-48;
            i++;
        }

        for(i=ceil(sqrt(a));i<=sqrt(b);i++)
        {

            if(isPalindrone(i))
            {
                if(isPalindrone(i*i))
                    {
                    answer++;
                    }
            }
        }
        n--;
        writer<<"Case #"<<nooftest-n<<": "<<answer<<"\n";

    }


}
