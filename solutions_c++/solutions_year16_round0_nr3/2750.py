#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int T,N,J,x=0;;
    cin>>T>>N>>J;
    string no=" 3 4 5 6 7 8 9 10 11\n";
    string str="1000000000000001";
    string cpy=str;
    cout<<"Case #1:\n";
    cout<<cpy<<no;
    x++;
    for(int i=1;i<N-1;i++)
    {
        for(int j=i+1;j<N-1;j=j+2)
        {
            cpy[i]='1';
            cpy[j]='1';
            cout<<cpy<<no;
            x++;
            cpy=str;
        }

    }
    return 0;
}
