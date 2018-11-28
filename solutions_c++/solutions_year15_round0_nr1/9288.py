#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
    //ifstream f;
    //ofstream f1;
    //f.open("D:\\downloads\\A-small-attempt0.txt");
    //f1.open("C:\\Users\\Ankur jain42\\Desktop\\output2.txt");
    freopen("D:\\downloads\\A-large.in","r+",stdin);
    freopen("C:\\Users\\Ankur jain42\\Desktop\\output2.txt","w+",stdout);

    int t,s,count=0,ans=0,a;
    cin>>t;
    string str;
    for(int p=0; p<t; p++)
    {
        count=0;
        ans=0;
        cin>>s;
        cin>>str;
        for(int i=0; i<str.length(); i++)
        {
            if(count>=i)
                count+=str[i]-48;
            else
            {
                a=i-count;
                ans+=a;
                count+=str[i]+a-48;
            }
        }
        cout<<"Case #"<<p+1<<": "<<ans<<"\n";
    }
}

