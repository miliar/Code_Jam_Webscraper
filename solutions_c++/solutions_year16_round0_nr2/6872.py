//ab.95
#include<iostream>
#include<string.h>
#include<fstream>
#include<stdlib.h>
using namespace std;
typedef unsigned long long ull;
int hsh[10];

int main()
{
ull var1,var2,var3,var4,cnt=0;
ull T,N,sum=0,s2=0,fall=0;
char inp[101];

ifstream fin;
fin.open("GCJTA.txt");
ofstream fin2;
fin2.open("GCJRESA.txt");
//cin>>T;
fin>>T;
var2=T;
while(T--)
{
    cnt=0;
    fin>>inp;
    //cin>>inp;
    for(var1=0,var3=1;var1<strlen(inp)-1;var1++)
    {
        if(inp[var1]==inp[var3])
        {
            var3++;
        }
        else if(inp[var3]=='\0')
        {
            break;
        }
        else
        {
            cnt++;
            inp[var1]=inp[var3];
            var3++;
        }
    }
    if(inp[var1]=='-')
    {
        cnt++;
    }
    fin2<<"Case #"<<var2-T<<": "<<cnt<<endl;
}
fin.close();
fin2.close();

return 0;

}
