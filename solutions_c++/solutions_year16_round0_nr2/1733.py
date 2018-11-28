#include<iostream>
#include<stdio.h>
#include<string.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<set>
#include<math.h>
#include<map>
using namespace std;

#define mp make_pair
#define pb push_back

int t;
string s;

int main()
{
    freopen ("B-large.in","r",stdin);
    freopen ("op2-2.out","w",stdout);
    cin>>t;
    for(int cas=1;cas<=t;cas++) {
        int cnt=0;
        cin>>s;
        for(int i=1;i<s.size();i++) {
            if(s[i]!=s[i-1])
                cnt++;
        }
        if(s[s.size()-1]=='-')
            cnt++;
        cout<<"Case #"<<cas<<": "<<cnt<<"\n";
    }
}
