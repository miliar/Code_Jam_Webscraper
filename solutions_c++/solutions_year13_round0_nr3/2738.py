#include<fstream>
#include<algorithm>
#include<sstream>
#include<string>
#include<cmath>
using namespace std;
ifstream fin("Csmall.in");
ofstream fout("Csmall.out");
bool ispal(long long x)
{
    stringstream ss;
    string s;
    ss<<x;
    ss>>s;
    for(int i=0;i<s.size();i++)
    {
        if(s[i]!=s[s.size()-i-1])
        return false;
    }
    return true;
}
int main()
{
    int T;
    fin>>T;
    for(int t=1;t<=T;t++)
    {
        int A,B;
        fin>>A>>B;
        long long ans=0;
        for(int i=A;i<=B;i++)
        {
            double x=sqrt(i);
            if(int((double(x)-int(x))*1000000)!=0)continue;
            if(ispal(i)&&ispal(x))
            ans++;
        }
        fout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
