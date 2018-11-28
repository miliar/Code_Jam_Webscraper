#include<iostream>
#include<algorithm>
#define MOD 1000000007
 
using namespace std;
 
int main()
{
    long long int tc,t,a,b,c,i,j,k,n,m,sum=0;
    cin >> tc;
    for(i=0;i<tc;i++)
    {
        cin >> a >> b >> c;
        cout << "Case #" << i+1 << ": " << (a*(b-1))/c+c << endl;
    }
}