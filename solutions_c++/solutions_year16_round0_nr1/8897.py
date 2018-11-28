#include <iostream>
#include <math.h>
#include <stack>
#include <fstream>
using namespace std;
#include <string.h>
#include <vector>


int main()
{

    ifstream file("A-large.in");
    ofstream answ("final_out.out");
    string str;
    int n;
    int ans;
    int temp;
    int a[10];
    int count=0;
    while(getline(file,str,'\n'))
    {   n=0;
        count++;
        for(int k=0;k<str.length();k++)
        {
            n+=pow(10,k)*(static_cast<int>(str[str.length()-k-1])-48);

        }

    for(int i=0;i<=9;i++){a[i]=0;}
    int j=1;

    int para=n;
    int flag;
    if(n==0){answ<<"Case #"<<count<<": "<<"INSOMNIA"<<endl; continue;}
    while(1>0)
    {   temp=para;

        while(temp!=0)
        {

            a[temp%10]=1;
            temp/=10;

        }
        j++;
        ans=para;
        para=n*j;
        flag=0;
        for(int i=0;i<10;i++)
        {
            if(a[i]==0){flag=1;break;}
        }
        if(flag==0){break;}

    }

    answ<<"Case #"<<count<<": "<<ans;
    if(count!=100){answ<<endl;}
    }
    answ.close();
}
