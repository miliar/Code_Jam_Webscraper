#include <bits/stdc++.h>
/*#include <boost/multiprecision/cpp_int.hpp> */
#define ll long long
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define gc getchar_unlocked
#define pp pair<int,int>
#define bigint boost::multiprecision::cpp_int
#define bsize 600
using namespace std;

int main()
{
    int t,n;
    string s;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        cin>>n>>s;
        int curr=s[0]-'0',an=0;

        for(int i=1;i<s.length();i++)
        {
            if(curr>=i)curr+=s[i]-'0';
            else
            {
                an+=i-curr;
                curr=i+s[i]-'0';
            }
        }
        cout<<"Case #"<<z<<": "<<an<<"\n";
    }

return 0;
}
