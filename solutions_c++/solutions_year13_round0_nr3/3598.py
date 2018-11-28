#include <fstream>
#include <cmath>
#include <string>
bool issq(long long int);
bool ispal(long long int);
using namespace std;
ifstream cin;
ofstream cout;
int main()
{
    int t;
    long long int n,m;
    cin.open("input.txt");
    cout.open("output.txt");
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n>>m;
        cout<<"Case #"<<i+1<<": ";
        long long int res=0;
        for(int j=n;j<=m;j++)
        {
            if(issq(j)&&ispal(j)&&ispal(sqrt(j))) {/*cout <<j<<" ";*/ res++;}
        }
        cout<<res<<endl;
    }
    cin.close();
    cout.close();
    return 0;
}
bool issq(long long int x)
{
    long long int y;
    y=sqrt(x);
    if((y*y)==x) return true;
    else return false;
}

bool ispal(long long int x)
{
    string y;
    char c;
    int t;
    while(x>0)
    {
        t=x%10; x=x/10;
        c=t+48;
        y.insert(0,1,c);
    }
    t=y.length();
    for(int i=0; i<t/2;i++)
    {
        if(y[i]!=y[t-1-i]) return false;
    }
    return true;
}
