#include <iostream>
//#include<conio.h>
#include<string>
#include<vector>
using namespace std;

int main()
{
    freopen("input1.in","r",stdin);
    freopen("output1.out","w",stdout);
    int t;
    int cases=1;
    cin>>t;


    while(t>0)
    {
     int Smax,c=0,invite=0,remain=0;
     cin>>Smax;

     string str;
     cin>>str;
int arr = atoi(str.c_str());
vector<int> v1;

vector<int>::iterator it;
it = v1.begin();

for(int i=0;i<=Smax;i++)
{
       int temp=arr%10;
                it = v1.insert ( it ,temp );
                arr=arr/10;

        }


     for(int i=0;i<=Smax;i++)
     {
         if(str[i]!=0)
         {
                if(i==0)
                {
                    for(int j=0;j<v1[i];j++)
                    {c++;}
                }
                else if(c>=i)
                {
                    for(int j=0;j<(v1[i]);j++)
                    {c++;}
                }
                else
                {
                    remain=i-c;
                    invite+=remain;
                    c+=remain;
                    i--;
                }
         }
     }


cout<<"Case"<<" #"<<cases<<": "<<invite<<endl;
cases++;
        t--;
    }
   // getch();
    return 0;
}
