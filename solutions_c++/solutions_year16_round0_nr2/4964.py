#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main()
{
    ofstream coutt("output.txt");
    ifstream cinn("input.txt");
    int T;
    cinn>>T;
    for(int ii=0;ii<T;ii++)
    {
        string a;
        cinn>>a;
        int cnt=0;
        for(;;)
        {
            for(int i=a.size()-1;i>=0;i--)
            {
                if(a[i]=='+')a.erase(i,1);
                else break;
            }
            if(a.size()==0)break;
            if(a[0]=='+')
            {
                for(int i=0;i<=a.size();i++)
                {
                    if(a[i]=='+')a[i]='-';
                    else break;
                }
                cnt++;
            }
            reverse(a.begin(),a.end());
            for(int i=0;i<a.size();i++)
            {
                if(a[i]=='-')a[i]='+';
                else a[i]='-';
            }
            cnt++;
        }
        coutt<<"Case #"<<ii+1<<": "<<cnt<<endl;

    }
}
