#include <fstream>
#include<iostream>
using namespace std;
ifstream in("count.in");
ofstream out("count.out");
int f[10];
bool checkfreq(int f[10]){
    int i;
    for(i=0;i<=9;i++)
        if(f[i]==0)
            return false;
    return true;
}
void markdigits(int f[10], long n){
    while(n>0){
            f[n%10]++;
            n=n/10;
        }
}
long findno(long n){
    if(n==0)
        return -1;
    else{
        int i,m=n;
        for(i=0;i<=9;i++)
            f[i]=0;
        n=0;
        while(!checkfreq(f)){
            n=n+m;
            markdigits(f, n);
        }
        return n;
    }
}

int main()
{
    int t,i,n,r;
    in>>t;
    for(i=1;i<=t;i++){
        in>>n;
        out<<"Case #"<<i<<": ";
        r=findno(n);
        if(r==-1)
            out<<"INSOMNIA";
        else
            out<<r;
        out<<"\n";
    }
    return 0;
}
