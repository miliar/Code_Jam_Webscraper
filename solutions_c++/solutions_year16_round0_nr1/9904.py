#include <bits/stdc++.h>
#include <fstream>
#include <string>

using namespace std;

void reset(int arr[])
{
    for(int j=0;j<10;j++)
        arr[j]=0;
}

int check(int arr[])
{
    for(int j=0;j<10;j++)
    {
        if(arr[j]==0)
            return 0;
    }
    return 1;
}

void dig_count(int arr[],int n)
{
    while(n)
    {
        arr[n%10]++;
        n=n/10;
    }
}

int main()
{
    long int n,i,j,t;
    int arr[10];
    ofstream output("output large.txt");
    ifstream input("A-large.in");
    input >> t;
    for(j=1;j<=t;j++)
    {
        reset(arr);
        input >> n;
        if(!n)
            output << "Case #" << j << ": INSOMNIA" << endl;
        else
        {
            for(i=1;;i++)
            {
                dig_count(arr,n*i);
                if(check(arr))
                    break;
            }
            output << "Case #" << j << ": " << n*i << endl;
        }
    }
}
