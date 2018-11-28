#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int main()
{
    ifstream f1;
    ofstream f2;
    f1.open("B-large.in");
    f2.open("output.out");
    int c=1,t,x,r,col;
    string str;
	f1>>t;
    while(c<=t)
    {
               f2<<"Case #"<<c++<<": ";
               f1>>str;
               x = r = 0;
               int ans = 0;
               col = str.length();
               for(int i=0;i<col;i++)
               {
               		if(str[i]=='+')r=1;
               		else
               		{
               			if(r==1)
               			{
               				ans = ans + 2;
               				while(str[i]=='-' && i<col)i++;
               				i--;
               			}
               			else
               			{
               				ans = ans + 1;
               				while(str[i]=='-' && i<col)i++;
               				i--;
               			}
               		}
               }
			   f2<<ans<<endl;
	}
	f1.close();
    f2.close();
    //system("pause");
    return 0;
    }
