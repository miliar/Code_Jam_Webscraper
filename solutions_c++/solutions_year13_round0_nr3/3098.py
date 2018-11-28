#include<iostream.h>
#include<string>
#include<fstream>
#include<list>
using namespace std;
int s[100][100],temp[100][100];int T,A,B,num1,num2;

int main()
{
    ifstream fin("in.IN");ofstream fo("out.txt");
    fin>>T;int count1;
    for(int i1=0;i1<T;i1++)
    {
        fin>>A>>B;count1=0;
        for(int i=A;i!=B+1;i++)
        {
            if((i==1)||(i==4)||(i==9)||(i==121)||(i==484)) count1++;
        }
    fo<<"Case #"<<i1+1<<": "<< count1<<endl;
    }
}
