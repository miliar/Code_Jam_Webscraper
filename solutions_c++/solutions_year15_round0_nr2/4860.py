//
//  main.cpp
//  codeB
//
//  Created by Junxing Wang on 4/11/15.
//  Copyright (c) 2015 Junxing Wang. All rights reserved.
//

#include <iostream>

using namespace std;

int a[1000+5];

int main(int argc, const char * argv[]) {

    int t,n;
    //cout<<"a";
    cin>>t;
    for (int ti=0; ti<t; ti++){
        cin>>n;
        int y = 0;
        for (int i=0; i<n; i++){
            cin>>a[i];
            if (a[i]>y)
                y = a[i];
        }
        int ans = 1000;
        for (int k=1; k<=y; k++){
            int s=k;
            for (int i=0; i<n; i++)
                s += (a[i]-1)/k;
            if (s<ans)
                ans = s;
        }
        cout<<"Case #"<<ti+1<<": "<<ans<<endl;
    }
    return 0;
}
