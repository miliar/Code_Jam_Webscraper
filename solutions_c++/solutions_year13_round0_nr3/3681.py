#include<iostream>
#include<fstream>
#include<cstdio>
//#define inp cin
//#define out cout
using namespace std;
int arr[1001];
int main()
{
    ifstream inp("input.txt");
    ofstream out("output.txt");
    arr[0]=0;
    for(int i=1;i<=1000;++i)
    {
        arr[i] = arr[i-1];
        if(i==1 || i==4 || i==9 || i==121 || i==484)
        {
            ++arr[i];
        }
    }
    int t,a,b;
    inp>>t;
    for(int T=1;T<=t;++T)
    {
        inp>>a>>b;
        out<<"Case #"<<T<<": "<<arr[b]-arr[a-1]<<endl;
    }
    return 0;
}
