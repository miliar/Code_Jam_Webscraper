#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int T,Smax,sum,n;
string k;

int main()
{
    ifstream file;
    file.open("A-large.in",ios::in);
    //ifstream file1;
    //file1.open("Odp.out",ios::out);

    file>>T;
    for(int j=0;j<T;j++)
    {
        sum=0;
        n=0;
        file>>Smax>>k;
        for(int i=0;i<=Smax;i++)
        {
            if(sum<i)
            {
                n+=i-sum;
                sum=i+k[i]-'0';
            }
            else
                sum+=k[i]-'0';
        }
        cout<<"Case #"<<j+1<<": "<<n<<"\n";
        //file1<<"Case #"<<j+1<<": "<<n<<"\n";

    }
}
