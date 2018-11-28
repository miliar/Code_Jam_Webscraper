#include <iostream>
#include <set>
#include <fstream>
using namespace std;
int main()
{
    ifstream cin("A-large.in");
    ofstream cout("alarge.txt");
    int t;
    long long n,m;
    cin>>t;
    set<int> s;
    bool b;
    for(int tt=1;tt<=t;tt++)
    {
        b=1;
        cin>>n;
        m=n;
        while(m)
        {
            s.insert(m%10);
            m/=10;
        }
        if(s.size()==10) {cout<<"Case #"<<tt<<": "<<1<<endl;continue;}
        for(int i=2;i<100000;i++)
        {
            m=n*i;
            while(m)
        {
            s.insert(m%10);
            m/=10;
        }
        if(s.size()==10) {cout<<"Case #"<<tt<<": "<<i*n<<endl;b=0;break;}
        }
        if(b)
        cout<<"Case #"<<tt<<": "<<"INSOMNIA"<<endl;
        s.clear();
    }
    return 0;
}
