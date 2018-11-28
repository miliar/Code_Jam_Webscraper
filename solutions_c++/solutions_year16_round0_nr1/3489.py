#include<bits/stdc++.h>
using namespace std;
#define MAX 2000010

long long  pp[MAX];

long long solve(long long  n)
{
    long long  i=1;

    int buc[20]={0};

    while(1)
    {
        long long  t=n*i;
        while(t)
        {
            buc[t%10]=1;
            t /= 10;
        }
         i++;

         int sum=0;
        for(int j=0;j<10;j++)
            sum += buc[j];
        if(sum==10)
        {
            long long ans = n*(i-1);
            return ans;
        }
    }
}
int main()
{
    for(long long i=1;i<MAX;i++)
    {
        pp[i] = solve(i);
    }

    ifstream IF;
    IF.open("input.txt");
    ofstream OF;
    OF.open("output.txt");
    int t;

    IF >> t;
    for(int tc=1;tc<=t;tc++)
    {
        int n;

        IF >> n;
        if(n==0)
            OF << "Case #" << tc << ": " << "INSOMNIA" << endl;
        else
            OF << "Case #" << tc << ": " << pp[n] << endl;
    }

    OF.close();
    IF.close();
}
