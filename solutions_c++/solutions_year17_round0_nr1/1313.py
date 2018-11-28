//
//  main.cpp
//  google cj1 q
//
//  Created by Magen on 08/04/2017.
//  Copyright © 2017 Magen. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int T,n;
    string s;
    cin>>T;
    bool first=true;
    for (int i=1; i<=T; i++) {
        if(first)
            first=false;
        else
            cout<<endl;
        cin>>s>>n;
        bool possible=true;
        int sizee=s.size();
        int ans=0;
        for(int j=0;j<sizee;j++)
        {
            if(s[j]=='+')continue;
            if(sizee-j<n)
            {
                possible=false;
                break;
            }
            for(int k=j;k<j+n;k++)
                s[k]=(s[k]=='+') ? '-' : '+';
            ans++;
        }
        cout<<"Case #"<<i<<": ";
        if(possible)
            cout<<ans;
        else
            cout<<"IMPOSSIBLE";
    }
    return 0;
}
