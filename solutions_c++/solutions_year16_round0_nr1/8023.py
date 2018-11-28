#include<bits/stdc++.h>
using namespace std;

long long a[20];

int main()
{
    ifstream in ("A-large.in");
    ofstream out ("largeSheep.txt");

    long long t;
    long long n;

    in>>t;

    for(long long ts=1;ts<=t;ts++){
        in>>n;

        memset(a,0,sizeof a);

        if(n==0){
            out<<"Case #"<<ts<<": "<<"INSOMNIA"<<endl;
            continue;
        }

        long long temp;
        long long c = 0;
        for(long long i=1;1;i++){
            temp = n*i;

            while(temp){
                if(a[temp%10]==0){
                    a[temp%10]=1;
                    c++;
                }
                temp/=10;
            }

            if(c==10){
                out<<"Case #"<<ts<<": "<<n*i<<endl;
                break;
            }

        }
    }

    return 0;
}
