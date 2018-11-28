#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
int main()
{
    ifstream fin("input.in");
    ofstream fout("output.txt");
    int tt;
    fin>>tt;
    for(int t=1;t<=tt;t++)
    {
        fout<<"Case #"<<t<<": ";
        LL n;
        fin>>n;
        if(n==0)
        {
            fout<<"INSOMNIA"<<endl;
            continue;
        }
        int f=0;
        set<LL> s;
        for(LL i=1;i<=100000;i++)
        {
            LL k=i*n;
            while(k)
            {
                s.insert(k%10);
                k/=10;

            }
            if(s.size()==10)
            {
                f=1;
                fout<<i*n<<endl;
                break;
            }
        }
        if(!f&&!n)fout<<"INSOMNIA"<<endl;

    }

}
