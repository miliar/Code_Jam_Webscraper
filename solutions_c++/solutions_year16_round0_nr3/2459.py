#include <fstream>
#include<iostream>
using namespace std;
#include<math.h>
#define LL long long
LL power(LL a, LL b)
{
    LL ans = 1;
    while(b > 0)
    {
        if(b%2 == 1)
        {
            ans *= a;
        }
        a *= a;
        b = b>>1;
    }
    return ans;
}
int main()
{
    long long c,i,j,n,times,t,start,maxi,k,e[20],x,y,d,sum,pos,f,b[11],q;
    ofstream outputFile;
    c=0;
    outputFile.open("output.in");

    ifstream inputFile;
    inputFile.open("C-small-attempt1.in");

    outputFile<<"Case #1"<<":"<<endl;

    inputFile>>t;
    while(t--){
        inputFile>>n>>times;
        start = power(2,n-1)+1;
        maxi = power(2,n);
        for(i=start;i<maxi;i=i+2)
        {
            if(c==times)
                break;
            k=i;d=0;
            while(k!=0)
            {
                e[d++]=k%2;
                k=k/2;
            }
            x=0;y=0;
            for(j=2;j<11;j++)
            {
                sum=0;pos=0;
                for(k=0;k<d;k++)
                {
                    sum = sum + e[k] * power(j,pos);
                    pos++;
                }
                for(f=2;f<=sqrt(sum);f++)
                {
                    if(sum%f==0)
                        break;
                }
                if(f<=sqrt(sum))
                    b[y++]=f;
                else {
                        x=1;
                        break;
                }
            }
            if(x!=1)
            {
                for(q=d-1;q>=0;q--)
                    outputFile<<e[q];
                outputFile<<" ";
                for(j=0;j<y;j++)
                    outputFile<<b[j]<<" ";
                outputFile<<"\n";
                c++;
            }
        }
    }
    inputFile.close();
    outputFile.close();
    return 0;
}
