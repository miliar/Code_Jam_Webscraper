#include <cstdio>
#include <cstring>
#include <algorithm>
#include<iostream>
#include<fstream.h>
#include<math.h>
using namespace std;
long long solve()
{
    long long a,b;
    long long count=0;
    cin>>a>>b;
    for (long long i=ceil(sqrt(a)); i<=sqrt(b); i++) {
    long long rem=0,sum=0;
        long long icopy = i;
        while (icopy!=0) {
            rem = icopy%10;
            icopy = icopy/10;
            sum = sum*10 + rem;
        }
        if (i==sum) {
            long long x=i*i;
            long long xcopy=x;
            rem=0,sum=0;
            while(x!=0)   
            {
                rem=x%10;
                x=x/10;
                sum=sum*10+rem;
            }
            if(xcopy==sum)
            {
                count++;
            }
            
        }
    }
    return count;
}

int main() {
   ofstream myfile;
    myfile.open ("PBig1.txt");
    int tc; scanf("%d\n", &tc);
    for(int g = 0; g < tc; g++) {
                myfile<<"Case #"<<g+1<<": "<<solve()<<endl;
    }
    return 0;
}
    