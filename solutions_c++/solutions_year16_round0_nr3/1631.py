#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

#define f first
#define s second
#define mp(a,b) make_pair(a,b)

vector<pair<string,vector<int> > > answer;

int main()
{
    //freopen("C-large.in","r",stdin);
    //freopen("C-large.out","w",stdout);
    int t,n,J;
    cin>>t>>n>>J;
    int i,j;
    n/=2;
    for(i=0;i<J;i++){
        string s="11";
        for(j=0;j<n-2;j++){
            if(i&(1<<j))
                s+="11";
            else
                s+="00";
        }
        s+="11";
        vector<int> tmp;
        for(j=2;j<=10;j++)
            tmp.push_back(j+1);
        answer.push_back(mp(s,tmp));
    }
    printf("Case #1:\n");
    for(i=0;i<answer.size();i++){
        cout<<answer[i].f;
        for(j=0;j<answer[i].s.size();j++)
            cout<<" "<<answer[i].s[j];
        cout<<endl;
    }
    return 0;
}
