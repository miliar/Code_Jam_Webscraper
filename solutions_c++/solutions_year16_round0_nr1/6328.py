//#include <iostream>
//#include <fstream>
//#include <stdio.h>
//#include <stdlib.h>
//#include <dlfcn.h>
//#include <sstream>
//#include <vector>
#include<bits/stdc++.h>


using namespace std;

string Int_to_string(int number)
{
    stringstream ss;
    ss << number;
    return ss.str();
}

int main()
{
    ofstream fs("nombre.txt");
    int T;
    long long N;
    cin>>T;

    int tmp;
    for(int i=0;i<T;++i)
    {
        cin>>N;
        if(N==0)
            fs<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        tmp=0;
        string n;
        int dig[10]={0};
        for(long long j=1,o_N=N;j<100;++j,o_N=N*j)
        {
            n=Int_to_string(o_N);
            for(int k=0;k<n.size();++k)
            {
                int q=n[k]-'0';
                if(dig[q]==0)
                {
                    ++tmp;

                    dig[q]=1;
                }
            }
            if(tmp==10)
            {
                fs<<"Case #"<<i+1<<": "<<n<<endl;
                break;
            }
        }
    }
    fs.close();
    return 0;
}
