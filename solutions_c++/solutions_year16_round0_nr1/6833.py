/* do something */

#include <bits/stdc++.h>
#define ll long long
#define over999 1234567890
#define fi first
#define se second
#define mp make_pair
#define pb push_back

using namespace std;

int k=0;
bool done[11];

void check(int x)
{
    while(x>0)
    {
        if(!done[x%10])done[x%10]=true,k++;
        x/=10;
    }
}

int main(){
    int t,n;
    cin >> t;
    for(int lap=1;lap<=t;lap++)
    {
        cin >> n;
        cout << "Case #"<< lap << ": ";
        if(n==0){cout << "INSOMNIA"<< endl; continue;}
        for(int i=0;i<10;i++)
            done[i]=false;
        int p=n;
        k=0;
        while(k < 10)
        {
            check(p);
            p+=n;
        }
        
        cout << p-n << endl;
        
    }
    return 0;
}