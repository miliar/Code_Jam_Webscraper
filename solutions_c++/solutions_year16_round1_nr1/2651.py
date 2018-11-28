#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<math.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<string>
#include<cmath>
#include<set>
#include<stack>

using namespace std;

int main()
{
    freopen("/Users/shitian/Desktop/gcj/gcj/A-large.in", "r", stdin);
    freopen("/Users/shitian/Desktop/gcj/gcj/out.txt", "w", stdout);
    int tcase;
    cin>>tcase;
    for(int tca=1;tca<=tcase;tca++){
        cout<<"Case #"<<tca<<": ";
        string s;
        cin>>s;
        deque<char>v;
        v.push_back(s[0]);
        for(int i=1;i<s.length();i++){
            if(s[i]>=v[0]){
                v.push_front(s[i]);
            } else {
                v.push_back(s[i]);
            }
        }
        while(v.size()){
            cout<<v.front();
            v.pop_front();
        }
        cout<<endl;
    }
    return 0;
}