#include<iostream>
#include<fstream>
using namespace std;
int palindrome(long long int num)
{
    int arr[20],i=0,j=0;
    while(num/10||num%10)
    {
        arr[i]=num%10;
        num=num/10;
        i++;

    }
    i--;
    j=0;
    while(j<i)
    {
        if(arr[i]!=arr[j])
            return 0;
        i--;
        j++;

    }
    return 1;
}
int main()
{
    long long int num,T,i=0,A,B,tilla,counter;
    ifstream infile("C-small-attempt0.in");
    ofstream outfile("output.txt");
    infile>>T;

    for(i=0;i<T;i++)
    {
        infile>>A>>B;

        tilla=1;
        counter=0;
        while(tilla*tilla<A)
            tilla+=1;
            while(tilla*tilla<=B)
            {
                if(palindrome(tilla))
                {
                    if(palindrome(tilla*tilla))
                    {
                       counter++;
                    }
                }
                tilla+=1;
            }
            outfile<<"Case #"<<i+1<<": "<<counter<<endl;


    }
    return 0;
}

