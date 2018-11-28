//
//  main.cpp
//  Reverge of the Pancakes
//
//  Created by Qiu Xin on 9/4/16.
//  Copyright © 2016 Qiu Xin. All rights reserved.
//

#include <iostream>
using namespace std;




int main(int argc, const char * argv[]) {
    int runNum, ans, sizeStr, j;
    cin >> runNum;
    for (int i=1;i<=runNum;i++)
    {
        string cur;
        cin>>cur;
        ans=0;
        sizeStr=cur.size();
        j=0;
        while (j<sizeStr&&cur[j]=='-')
            j++;
        if (j>0)
            ans++;
        while (1)
        {
            while (j<sizeStr&&cur[j]=='+')
                j++;
            if (j==sizeStr)
                break;
            ans+=2;
            while (j<sizeStr&&cur[j]=='-')
                j++;
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
