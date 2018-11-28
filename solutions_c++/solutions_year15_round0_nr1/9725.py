#include<fstream>
using namespace std;
int main()
{
    fstream input("input.in",ios::in);
    fstream output("output.out",ios::out);
    int t,n,a,c,i,j;
    string s;
    input>>t;
    for(i=0;i<t;i++)
    {
        input>>n>>s;
        a=0;
        c=s[0]-'0';
        for(j=1;j<=n;j++)
        {
            if(c>=j)
            {
                c+=s[j]-'0';
                continue;
            }
            else if(s[j]!='0')
            {
                a+=j-c;
                c+=a+s[j]-'0';
            }
        }
        output<<"Case #"<<i+1<<": "<<a<<"\n";
    }
    return 0;
}
