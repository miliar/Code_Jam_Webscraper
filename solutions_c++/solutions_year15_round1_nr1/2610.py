#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

int diff(int a)
{
    if(a<0) return 0;
    else return a;
}

int main()
{
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("output.txt");
    int s1=0,s2=0,max1 = 0,T,N,a[10000];
    in>>T;
    for(int i=0; i<T; i++)
    {
        s1=0; s2=0; max1=0;
        in>>N;
        for(int j=0; j<N; j++) in>>a[j];
        for(int j=1; j<N; j++) s1 += diff(a[j-1]-a[j]);
        for(int j=1; j<N; j++) if(a[j-1]-a[j]>max1) max1 = a[j-1]-a[j];
        for(int j=1; j<N; j++) s2 += min(a[j-1],max1);
        out<<"Case #"<<i+1<<": "<<s1<<" "<<s2<<endl;
    }
}
