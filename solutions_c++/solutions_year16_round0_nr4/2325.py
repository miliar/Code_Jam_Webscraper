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
    long long int num,z=1,k,c,s,t,i,x;
    ofstream outputFile;
    outputFile.open("out.txt");
    ifstream inputFile;
    inputFile.open("D-small-attempt1.in");
    inputFile>>t;
    while(t--){
        inputFile>>k>>c>>s;
        num = power(k,c);
        if(k==1)
        {
            outputFile<<"Case #"<<z<<": 1"<<"\n";
        }
        else{
            x=(num-1)/(k-1);
            outputFile<<"Case #"<<z<<": ";
            for(i=0;i<num;i=i+x)
            {
                outputFile<<i+1<<" ";
            }
            outputFile<<"\n";
        }
        z++;
    }
    inputFile.close();
    outputFile.close();
    return 0;
}
