#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
#define ll long long int

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    freopen("B.txt","r",stdin);
    freopen("Aout.txt","w",stdout);
    int t;
    cin>>t;
    for(int q=1;q<=t;++q) 
    {
        int n;
        cin>>n;
        char a[n+10];
        cin>>a;
        //cout<<n<<" "<<a<<"**";
        int people=0,extra=0;
        for(int i=0;i<n+1;++i)
        {
            if(a[i]=='0')
            continue;
            int peopleneeded=i;
            if(people<peopleneeded)
            {
                extra+=peopleneeded-people;
                people=peopleneeded;
                //cout<<i<<" "<<extra<<"**";
            }
            people+=(a[i]-48);
        }
        printf("Case #%d: %d\n",q,extra);
    } 
    return 0;
}
