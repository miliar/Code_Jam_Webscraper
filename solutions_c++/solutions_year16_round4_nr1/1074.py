#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <unordered_map>
using namespace std;

string word;
int n,a,b,c,a1,b1,c1;
string ss;

bool bt(int a,int l,int r)
{
    if(a1<0||b1<0||c1<0)
        return 0;
    if(l==r)
    {
        if(a==0)
            a1--;
        if(a==1)
            b1--;
        if(a==2)
            c1--;
        ss[l]=word[a];
        return 1;
    }
    if(a==0)
    {
        return bt(0,l,(l+r)/2)&&bt(2,(l+r)/2+1,r);
    }
    if(a==1)
    {
        return bt(1,l,(l+r)/2)&&bt(0,(l+r)/2+1,r);
    }
    if(a==2)
    {
        return bt(1,l,(l+r)/2)&&bt(2,(l+r)/2+1,r);
    }
    return  0;
}

void sorter(int l,int r)
{
    if(l==r)
        return;
    sorter(l,(l+r)/2);
    sorter((l+r)/2+1,r);
    string ss1;
    if(ss.substr(l,(r-l+1)/2)>ss.substr((l+r)/2+1,(r-l+1)/2))
    {
        for(int f=l;f<=(l+r)/2;f++)
            swap(ss[f],ss[f+(r-l+1)/2]);
    }
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int t;
    cin>>t;
    word="RPS";
    for(int tc=1;tc<=t;tc++)
    {
        cin>>n>>a>>b>>c;
        cout<<"Case #"<<tc<<": ";
        ss="";
        n=(1<<n);
        for(int f=0;f<n;f++)
            ss+='0';
        vector<string>ans;
        a1=a,b1=b,c1=c;
        bt(0,0,n-1);
        sorter(0,n-1);
        ans.push_back(ss);
        a1=a,b1=b,c1=c;
        bt(1,0,n-1);
        sorter(0,n-1);
        ans.push_back(ss);
        a1=a,b1=b,c1=c;
        bt(2,0,n-1);
        sorter(0,n-1);
        ans.push_back(ss);
        sort(ans.begin(),ans.end());
        for(int f=0;f<ans.size();f++){
            int R=0,P=0,S=0;
            for(int f1=0;f1<ans[f].size();f1++)
            {
                if(ans[f][f1]=='R')
                    R++;
                if(ans[f][f1]=='P')
                    P++;
                if(ans[f][f1]=='S')
                    S++;
            }
            if(R==a&&P==b&&S==c){
            cout<<ans[f]<<endl;
                break;
            }
            if(f+1==ans.size())
                cout<<"IMPOSSIBLE\n";
        }
    }
}