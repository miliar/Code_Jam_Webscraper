#include <stdio.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <assert.h>

using namespace std;

#define LL long long
#define yes "YES"
#define no "NO"
#define MAX 1000005
#define pb push_back

#define cas "Case #"


int main()
{
    int test,row,x;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin>>test;
    for(int k=1;k<=test;k++){
        vector<int> a;
        vector<int> b;
        vector<int> ans(4);
        vector<int>:: iterator it;
        cin>>row;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                if(i==row) cin>>x , a.pb(x);
                else cin>>x;
        cin>>row;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                if(i==row) cin>>x , b.pb(x);
                else cin>>x;

        sort(a.begin(),a.end());
        sort(b.begin(),b.end());

        //for(int i=0;i<a.size();i++) cout<<a[i]<<" ";cout<<endl;
        //for(int i=0;i<b.size();i++) cout<<b[i]<<" ";cout<<endl;

        it=set_intersection(a.begin(),a.end(),b.begin(),b.end(),ans.begin());
        ans.resize(it-ans.begin());

        if(ans.size()==1){
            cout<<cas<<k<<": "<<ans[0]<<endl;
        }
        else if(ans.size()>1){
            cout<<cas<<k<<": Bad magician!"<<endl;
        }
        else if(ans.size()==0){
            cout<<cas<<k<<": Volunteer cheated!"<<endl;
        }

    }
    return 0;
}
