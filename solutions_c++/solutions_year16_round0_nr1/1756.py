#include<bits/stdc++.h>
#define LONG_LONG_MAX	9223372036854775807LL
using namespace std;
void f(set<int>& s, long long n)
{
    do
    {
        s.insert(n%10);
        n=n/10;
    } while(n>0);
}
int main()
{


    freopen("GoogleCodeJam2016.txt", "r", stdin);
    freopen("GoogleCodeJam2016_output.txt", "w", stdout);

    int t;
    cin>>t;
    //t = 1000000;
    for(int tc=1;tc<=t;tc++)
    {


        long long n = tc;
        cin>>n;

        if(n==0)
        {
            cout<<"Case #"<<tc<<": "<<"INSOMNIA"<<endl;continue;
        }

        //n = tc;
        set<int>s;
        f(s, n);
        long long tmp = n;
        int cnt=1;
        while(s.size()!=10)
        {

            n+=tmp;
            cnt++;
            f(s, n);
        }

        cout<<"Case #"<<tc<<": "<<n<<endl;
        //cout<<cnt<<endl;

    }


}
