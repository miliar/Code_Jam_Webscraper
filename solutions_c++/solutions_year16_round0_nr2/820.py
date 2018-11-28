#include <iostream>
using namespace std;
int main()
{
    int t,tt,i,j,cnt;
    string s;
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>s;
        cnt=0;
        for (i=s.size()-1;i>=0;i--)
            if (s[i]=='-')
            {
                cnt++;
                for (j=i;j>=0;j--) s[j]=(s[j]=='+')?'-':'+';
            }
        cout<<"Case #"<<tt<<": "<<cnt<<endl;
    }
    return 0;
}
