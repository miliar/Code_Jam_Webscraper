#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#define lli long long int
#define pb push_back
#define mod 1000000007
#define pii pair<int,int>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,a,b,n,tc=0;
    string str;
    cin>>t;
    while(t--){
        cin>>str;
        string temp = "";
        temp+=str[0];
        for(i=1;i<str.size();i++){
            if(str[i]!=temp[temp.size() -1])temp+=str[i];
        }
        int ans = temp.size();
        if(temp[temp.size()-1] == '+')ans--;
        printf("Case #%d: %d\n",++tc,ans);
    }

    return 0;
}

