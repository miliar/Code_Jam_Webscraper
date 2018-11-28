#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

#define For(i, a, b) for (int i=a; i<=b; i++)
#define int64 long long
#define maxN 10000

int main() {

    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("codejam.txt");

    int T;
    fin>>T;
    for(int t=1;t<=T;t++)
    {
        int N;
        fin>>N;
        int M=N;
        int result=-1;
        int digits[10]={0};
        for(int i=1;i<10000;i++)
        {
            int m=M;
            while(m>0)
            {
                digits[m%10]=1;
                m/=10;
            }
            bool all=true;
            for(int j=0;j<10;j++)
                if(digits[j]==0)all=false;
            if(all){result=M;break;}
            M+=N;
        }
        fout<<"Case #"<<t<<": ";
        if(result==-1)fout<<"INSOMNIA"<<endl;
        else fout<<result<<endl;
    }


}
