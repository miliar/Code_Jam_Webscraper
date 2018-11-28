//
//  main.cpp
//  2
//
//  Created by Zhou Sun on 5/31/14.
//  Copyright (c) 2014 Zhou Sun. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;
int main(int argc, const char * argv[])
{
    int ts,n,x;
    cin>>ts;
    for (int tt=1; tt<=ts; tt++) {
        cin>>n;
        vector<int>v;
        for (int i=0; i<n; i++) {
            cin>>x;
            v.push_back(x);
        }
        int sum=0;
        for (int i=n-1;i>=0; i--) {
            int mi=0;
            for (int j=0; j<v.size(); j++) {
                if(v[j]<v[mi])
                    mi=j;
            }
            sum+=min(mi,i-mi);
            v.erase(v.begin()+mi);
            
        }
        cout<<"Case #"<<tt<<": "<<sum<<endl;
    }
    return 0;
}

