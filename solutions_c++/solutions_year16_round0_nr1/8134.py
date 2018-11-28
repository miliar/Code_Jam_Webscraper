#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
     ofstream outputFile;
    ifstream inputFile;
    inputFile.open("A-large.in");
   outputFile.open("output.txt");
    int t,a=0;
    inputFile>>t;
    while(a<t)
    {
        unsigned long long n,x;
        inputFile>>n;
        x=n;
        int w=n,y=1;
        int count0=0,count1=0,count2=0,count3=0,count4=0,count5=0,count6=0,count7=0,count8=0,count9=0;
        if(n==0)
           {
               a++;
            outputFile<<"Case #"<<a<<": INSOMNIA"<<endl;
           }
        else
        {
    while(count0==0||count1==0||count2==0||count3==0||count4==0||count5==0||count6==0||count7==0||count8==0||count9==0)
    {
            n=w*y;
            x=w*y;
            y++;
       while(n!=0)
        {
            int b=n%10;
            n=n/10;
            if(b==0)
                count0++;
            else if(b==1)
                count1++;
            else if(b==2)
                count2++;
            else if(b==3)
                count3++;
            else if(b==4)
                count4++;
            else if(b==5)
                count5++;
            else if(b==6)
                count6++;
            else if(b==7)
                count7++;
            else if(b==8)
                count8++;
            else
                count9++;
        }
    }
        a++;
        outputFile<<"Case #"<<a<<": "<<x<<endl;
        }
    }
    outputFile.close();
    return 0;
}
