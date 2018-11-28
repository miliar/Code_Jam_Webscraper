#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int plate[1005],n;

int calculate_method1()
{
    int sum=0;

    for(int i=1;i<n;i++)
    {
        if(plate[i]<plate[i-1])
            sum=sum+plate[i-1]-plate[i];
    }

    return sum;
}


int calculate_method2()
{
    int sum=0;
    int diff[1005];

    for(int i=1;i<n;i++)
    {
        diff[i-1]=plate[i-1]-plate[i];
    }

    int max=*max_element(diff,diff+n-1);

    for(int i=0;i<n-1;i++)
    {
        if(plate[i]<=max)
            sum=sum+plate[i];
        else
            sum=sum+max;

    }

    return sum;
}

int main()
{
    int test;

    fin>>test;

    for(int j=1;j<=test;j++)
    {
        fin>>n;

        for(int i=0;i<n;i++)
            fin>>plate[i];

        int m1=calculate_method1();
        int m2=calculate_method2();

        fout<<"Case #"<<j<<": "<<m1<<" "<<m2<<endl;

    }

    return 0;
}
