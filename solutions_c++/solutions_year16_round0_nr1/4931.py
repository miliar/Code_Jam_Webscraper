#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int num,temp,a[100000],i,i1,hash[11]={0},count=0,count1=1,t;
    long long n;
    ifstream myfile;
    ofstream outfile;
    myfile.open("input.txt");
    outfile.open("output.txt");
    myfile>>t;
    for(i=1;i<=t;i++)
    {
        myfile>>n;for(i1=0;i1<=10;i1++)hash[i1]=0;
        temp=n;count1=1;count=0;
        if(temp==0){outfile<<"Case #"<<i<<": INSOMNIA"<<endl;continue;}
        while(count<10)
        {
                temp=n*count1;
                while(temp>0)
                {
                    {if(hash[temp%10]==0){count++;hash[temp%10]=1;}}
                    temp=temp/10;
                }
                count1++;
        }
       outfile<<"Case #"<<i<<": "<<n*(count1-1)<<endl;
    }
    return 0;
}
