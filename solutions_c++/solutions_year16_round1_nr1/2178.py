//
//  main.cpp
//  Last Word
//
//  Created by Qiu Xin on 16/4/16.
//  Copyright © 2016 Qiu Xin. All rights reserved.
//

#include <iostream>
using namespace std;


int main(int argc, const char * argv[]) {
    int runNum, sizeStr, j;
    cin >> runNum;
    for (int i=1;i<=runNum;i++)
    {
        string cur;
        cin>>cur;
        string ans;
        sizeStr=cur.size();
        ans+=cur[0];
        for (j=1;j<sizeStr;j++)
            if (cur[j]>=ans[0])
                ans=cur[j]+ans;
            else
                ans+=cur[j];
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
