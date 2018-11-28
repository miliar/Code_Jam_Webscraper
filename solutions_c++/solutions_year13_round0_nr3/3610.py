#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<math.h>
#include<sstream >
using namespace std;

string intToString(long long int i)
{
    stringstream ss;
    string s;
    ss << i;
    s = ss.str();

    return s;
}

int ispalin(long long int i)
{
    string input=intToString(i);
    if (input == string(input.rbegin(), input.rend()))
    {
        return 1;
    }
    return 0;
}

long long int issquare(long long int a)
{
    double result;
    result= sqrt (a);
    if ((result * result)== a)
        {
            int k=ispalin(result);
            return k;
        }
    else
        return 0;
}



int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
     cin>>t;

    for(int T=1;T<=t;T++)
    {
        long long int A,B,cnt=0;
        cin>>A>>B;

        for(long long int i=A;i<=B;i++)
        {
            int p=ispalin(i);
            int s=issquare(i);

            if(p==1&&s==1)
                cnt++;

        }

        cout<<"Case #"<<T<<": "<<cnt<<"\n";

    }

}

