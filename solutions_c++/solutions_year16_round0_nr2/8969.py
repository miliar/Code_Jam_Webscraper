#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <cstdio>
#include <math.h>
#include <time.h>
#include <string.h>
#include <sstream>
#include <vector>
#include <queue>
#include <bitset>
#include <algorithm>
using namespace std;

int main()
{
    //  freopen("B-large.in","r",stdin);
    //  freopen("DATA.txt","w",stdout);
    int t; cin>>t;
    for(int i = 0; i < t; i++){
        string s; cin>>s;
      //  cout<<s<<endl;
        int ans = 0;
        int cur_ind = 0;
        while(1){
            int temp = s[cur_ind];
            while(1){
                cur_ind++;
                if(cur_ind==s.size()) break;
                if(s[cur_ind]!=temp){
                    ans++;
                    break;
                }
            }
            if(cur_ind==s.size()) break;
        }
        if(s[cur_ind-1]=='-') ans++;
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    return 0;
}




