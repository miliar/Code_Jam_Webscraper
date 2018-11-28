#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
ifstream f("input.txt");
ofstream g("output.txt");
int n;
int64_t isPrime(int64_t x)
{
    for(int64_t i=2; i*i<=x; i++)
        if(x%i==0)
            return i;
    return -1;
}
vector <string> was;
int64_t StringToBaseN(string x, int B)
{
    int64_t p=1;
    int64_t ans=0;
    for(int i=n-1;i>=0;i--)
    {
        ans+=(x[i]-'0')*p;
        p*=B;
    }
    return ans;
}
vector<char> comp;
void generate(int k)
{
    for(int i=0; i<2; i++)
    {
        comp[k]='0'+i;
        if(k==n-2)
        {
            string y="";
            for(int t=0; t<n; t++)
                y+=comp[t];
            was.push_back(y);
        }
        else
            generate(k+1);
    }
}

int main()
{
    int t;
    f>>t;
    int j;
    f>>n>>j;
    if(t==1)
    {
        g<<"Case #1:\n";
        string x;
        comp = vector<char>(n,'0');
        comp[0]=comp[n-1]='1';
        vector <int64_t> nr(9,-1);
        int ok = true;
        generate(1);
        for(int i=0;i<was.size() && j;i++)
        {
            for(int q=2;q<=10;q++)
                nr[q-2]=isPrime(StringToBaseN(was[i],q));
            if(!count(begin(nr),end(nr),-1))
            {
                g<<was[i]<<" ";
                for(int i=0;i<9;i++)
                    g<<nr[i]<<" ";
                j--;
                g<<"\n";
            }

        }

    }
}
