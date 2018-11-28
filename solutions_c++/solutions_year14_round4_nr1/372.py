//
//  main.cpp
//  a
//
//  Created by Zhou Sun on 5/31/14.
//  Copyright (c) 2014 Zhou Sun. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;
int main(int argc, const char * argv[])
{
    int ts,n,m,x;
    cin>>ts;
    for (int tt=1; tt<=ts;tt++) {
        cin>>n>>m;
        vector<int> v;
        for (int i=0; i<n; i++) {
            cin>>x;
            v.push_back(x);
        }
        sort(v.begin(), v.end());
        int j=n-1;
        int s=0;
        for (int i=0; i<n; i++) {
            s++;
            while (j>i+1 && v[i]+v[j]>m) {
                j--;
            }
            if (j>i && v[i]+v[j]<=m) {
                s--;
                j--;
            }
        }
        cout<<"Case #"<<tt<<": "<<s<<endl;
    }

    return 0;
}

