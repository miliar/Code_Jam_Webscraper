
#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output1.txt");
    char S[200];
    long int T,l=0,length,count=0;
    fin>>T;
    while(l<T){
        fin>>S;
        length=strlen(S);
        for(int i=0;i<length-1;i++)
        {
            if(S[i]!=S[i+1]){
                count++;
            }
        }
        if(S[length-1]=='-'){
            count++;
        }
        fout<<"Case #"<<l+1<<": "<<count<<"\n";
        count=0;
        l++;
    }
return 0;
}
