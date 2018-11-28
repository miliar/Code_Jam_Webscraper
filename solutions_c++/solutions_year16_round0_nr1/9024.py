#include<bits/stdc++.h>
#define pi 2*acos(0.0)
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define MAX 10000000
using namespace std;

int main ()
{
    ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");
    int testcase,cs=1; fin>>testcase;
    while(testcase--)
    {
        long long number; fin>>number;
        if(number==0)
        {
            fout<<"Case #"<<cs++<<": INSOMNIA"<<endl;
            continue;
        }
        long long i,j=2,k,l,temp,ans,ten=0,result;
        bool found[10];
        for(i=0;i<10;i++) found[i]=false;
        k=number;
        while(ten!=10)
        {
            result=k;
            temp=k;
            while(temp>0)
            {
                ans=temp%10;
                if(found[ans]!=true)
                {
                    found[ans]=true; ten++;
                }
                temp=temp/10;
            }
            k=j*number; j++;
        }
        fout<<"Case #"<<cs++<<": "<<result<<endl;
    }
    return 0;
}
