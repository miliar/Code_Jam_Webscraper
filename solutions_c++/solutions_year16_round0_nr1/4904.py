//
#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<climits>
#include<fstream>
#include<iomanip>
#include<queue>
#include<stack>
#define lli long long

using namespace std;

bool used[1000];
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream cin("A.in");
    ofstream cout("A.out");

    lli k,k1;
    int T,n,l=0,T1=0;
    cin>>T;

    while(T)
    {
        T1++;
        cout<<"Case #"<<T1<<": ";
        T--;
        cin>>n;
        if(n==0){cout<<"INSOMNIA\n";continue;}

        memset(used,0,sizeof(used));

        k1=n;k=1; l=0;
        while(1)
        {
            k1=k*n;
            l=0;

            while(k1)
            {
                used[k1%10]=1;
                k1/=10;
            }
            for(int i=0;i<=9;i++)
            {
                if(used[i]==0)l=1;
            }

            if(l==0){cout<<(lli)k*n<<"\n";break;}
            k++;
        }

    }
    return 0;
}


