#include <iostream>
#include <fstream>
using namespace std;
long long int pow1(long long int i,long long int n)
{
    long long int ans=1;
    while(n>=1)
    {
        ans=ans*i;
        n--;
    }

    return ans;
}
int main()
{
    long long int T,S,K,C,i;
    ofstream file1;
    file1.open("F.txt");
    cin >>T;

    for(i=1;i<=T;i++)
    {
        cin >>K>>C>>S;
        long long int ans=1;

        file1 <<"Case #"<<i<<": ";
        while(S>=1)
        {
            file1 <<ans<<" ";
            ans=ans+pow1(K,C-1);
            S--;
        }

        file1<<endl;
    }

    return 0;
}
