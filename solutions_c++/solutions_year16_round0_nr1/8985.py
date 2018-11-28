#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;

int main()
{
    int t;
    ofstream fout ("input.out");
    ifstream fin ("input.in");
    fin>>t;
    int num[10];
    for(int i=1;i<=t;i++){
        long long n;
        fin>>n;
        fout<< "Case #" << i<< ": ";
        if(n==0){
            fout<< "INSOMNIA"<<endl;
            continue;
        }
        for(int k=0;k<10;k++) num[k]=0;
        bool tadhg =true;
        long long h=n;
        int count=0;
        while(tadhg){
            count++;
            h=n*count;
            while(h>0){
                int a =h%10;
                num[a]++;
                h/=10;
            }
            tadhg=false;
            for(int k=0;k<10;k++)
                if(num[k]==0)
                    tadhg=true;
        }
        fout<<n*count<<endl;
    }
    return 0;
}
