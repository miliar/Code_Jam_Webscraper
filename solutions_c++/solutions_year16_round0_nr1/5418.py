#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<set>
#include<map>
#include<climits>
#include<cstring>
#include<list>
#include<fstream>
#include<queue>
#include<sstream>
#include<stack>
#include<iomanip>

using namespace std;
typedef long long LL;

LL mod=1e9+7;

int mark[10];

bool check()
{
    for(int i=0; i<=9; i++)
        if(mark[i]==0)
        return false;

    return true;

}

void marker(int x)
{
    while(x>0)
    {
        mark[x%10]=1;
        x/=10;
    }
}


int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);


    ifstream cin("A-large.in");
    ofstream cout("file.txt");

    int T;
    cin>>T;

    for(int I=0; I<T; I++)
    {
        int n;

        cin>>n;

        for(int i=0; i<10; i++)
            mark[i]=0;

        cout<<"Case #"<<I+1<<": ";

        if(n==0)
        {
            cout<<"INSOMNIA\n";
            continue;
        }

        int x=n;

        while(1)
        {
            marker(n);
            if(check()==true)
            {
                cout<<n<<'\n';
                break;
            }


            n+=x;
        }

    }




}

