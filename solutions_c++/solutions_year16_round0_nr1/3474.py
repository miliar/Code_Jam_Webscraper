#include <bits/stdc++.h>
//#include<fstream>
using namespace std;
int main()
{
    cout.tie(0);
    std::ios::sync_with_stdio(false);
    ifstream fin;
    fin.open("input.in",ios::in);
    ofstream fout;
    fout.open("output.txt",ios::out);
    int t,T;
    fin>>T;
    for(t=1;t<=T;t++)
    {
        long long i=1,n,temp;
        set<int> s;
        fin>>n;
        if(n==0) {fout<<"Case #"<<t<<": INSOMNIA"<<endl; continue;}
        temp=n;
            while(temp>0)
            {
                s.insert(temp%10);
                temp=temp/10;
            }
            while(true)
            {
                temp=i*n;
                while(temp>0)
                {
                    s.insert(temp%10);
                    temp=temp/10;
                }
                if(s.size()==10)
                {
                    break;
                }
                i++;
            }
        if(s.size()==10)
                fout<<"Case #"<<t<<": "<<i*n<<endl;
            else
                fout<<"Case #"<<t<<": INSOMNIA"<<endl;
    }
    return 0;
}
