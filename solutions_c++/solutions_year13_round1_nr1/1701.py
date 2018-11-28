#include<iostream.h>
#include<string>
#include<fstream>
#include<list>
#include<stack>
#include<queue>
#include<math.h>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<map>
using namespace std;
unsigned long long int T,r,t,num1,num2;

int main()
{
    ifstream fin("in.IN");ofstream fo("out.txt");
    fin>>T;
    for(int i1=0;i1<T;i1++)
    {
        fin>>r>>t;
        num1=(sqrt(pow(2*r-1,2)+8*t)+1-2*r)/4;
        fo<<"Case #"<<i1+1<<": "<<num1<<endl;
    }
}
