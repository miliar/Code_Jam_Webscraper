#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

ifstream inFile("A-large.in",ios::in);
ofstream outFile("A-large.out",ios::out);
bool nums[10];

void function1(long long int r)
{
    long long int temp;

    while(r>0)
    {
        temp = r%10;

        if(temp==0)
            nums[0]=1;
        else if(temp==1)
            nums[1]=1;
        else if(temp==2)
            nums[2]=1;
        else if(temp==3)
            nums[3]=1;
        else if(temp==4)
            nums[4]=1;
        else if(temp==5)
            nums[5]=1;
        else if(temp==6)
            nums[6]=1;
        else if(temp==7)
            nums[7]=1;
        else if(temp==8)
            nums[8]=1;
        else if(temp==9)
            nums[9]=1;

        r /= 10;
    }
}

int main()
{
    int t;
    long long int n;
    long double max;
    bool flag;

    max = pow(10,6);

    inFile>>t;
    if(t>100)
        t=100;

    for(int i=1; i<=t; i++)
    {
        long long int result;
        flag = 0;
        for(int j=0; j<10; j++)
        {
            nums[j]=0;
        }

        inFile>>n;
        if(n<0)
            n=0;
        if(n>max)
            n=max;
        if(n==0)
        {
            outFile<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }

        for(long long int j=1;!flag; j++)
        {
            result = j*n;
            function1(result);
            if(nums[0]&&nums[1]&&nums[2]&&nums[3]&&nums[4]&&nums[5]&&nums[6]&&nums[7]&&nums[8]&&nums[9])
                flag = 1;
        }

        if(flag)
            outFile<<"Case #"<<i<<": "<<result<<endl;
        else
            outFile<<"Case #"<<i<<": INSOMNIA"<<endl;
    }

    return 0;
}
