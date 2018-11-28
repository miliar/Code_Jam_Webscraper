#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int t,n;
    ifstream iff; iff.open ( "inp.in" ) ;
    ofstream opp; opp.open ( "op.txt" ) ;
    iff>>t;
    for(int i=1;i<=t;i++)
    {
        int ans=0,cur=0;;
        string s;
        iff>>n;
        iff>>s;

        for(int j=0;j<=n;j++)
        {
            if( cur<j )
            {
                ans+=( j-cur );
                cur=j ;
            }
            cur += (s[j]-'0') ;
        }
        opp<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
