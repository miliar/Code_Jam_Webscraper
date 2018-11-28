#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

#define MAX 100

int a, b;


int judge(int p);
int square_judge(int p);
int mypow(int x);

int main()
{
    //cout<<(int)sqrt(8)<<endl;

    ifstream in("C-small-attempt0.in");
    ofstream out("C-small-attempt0.out");

    int T;

    int i, j, count=1;
    int result;

    in>>T;
    for(count=1; count<=T; count++)
    {
        result=0;
        in>>a>>b;
        for(i=a; i<=b; i++)
        {
            if(judge(i)&&square_judge(i))
            {
                cout<<i<<endl;
                result++;
            }
        }
        out<<"Case #"<<count<<": "<<result<<endl;
    }

    return 0;
}

int judge(int p)
{

    int q=p;
    int temp=0;
    while(q)
    {
        temp=temp*10+q%10;
        q=q/10;
    }
    return (temp==p);
}
int square_judge(int p)
{
    int s=(int)sqrt(p);
    if(mypow(s)<p)
    {
        return 0;
    }
    if(judge(s))
        return 1;
    return 0;
}

int mypow(int x)
{
    return (x*x);
}
