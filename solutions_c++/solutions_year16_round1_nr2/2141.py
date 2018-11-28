//
//  main.cpp
//  Rank and File
//
//  Created by Qiu Xin on 16/4/16.
//  Copyright © 2016 Qiu Xin. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;


int main(int argc, const char * argv[]) {
    int runNum, length;
    cin >> runNum;
    for (int i=1;i<=runNum;i++)
    {
        cin>>length;
        vector<vector<int>> store(length*2-1,vector<int>(length,0));
        for (int j=0;j<length*2-1;j++)
            for (int k=0;k<length;k++)
                cin>>store[j][k];
        vector<int> ans(length,0), miss(length,INT_MAX);
        vector<int> visited(length*2-1,0);
        int misK, count, misID, k1, k2;
        for (int j=0;j<length;j++)
        {
            k1=k2=-1;
            for (int k=0;k<length*2-1;k++)
            {
                if (visited[k]==1)
                    continue;
                if (store[k][j]<miss[j])
                {
                    k1=k;
                    k2=-1;
                    miss[j]=store[k][j];
                    count=1;
                }
                else
                    if (store[k][j]==miss[j])
                    {
                        k2=k;
                        count++;
                    }
            }
            if (k1>=0)
                visited[k1]=1;
            if (k2>=0)
                visited[k2]=1;
            if (count==1)
                misID=j;
        }
        for (int k=0;k<length*2-1;k++)
            if (store[k][misID]==miss[misID])
            {
                misK=k;
                break;
            }
        for (int j=0;j<length;j++)
        {
            if (j==misID)
            {
                ans[j]=store[misK][j];
                continue;
            }
            ans[j]=store[misK][j];
            for (int k=0;k<length*2-1;k++)
                if (store[k][j]==miss[j]&&store[k][misID]!=store[misK][j])
                    ans[j]=store[k][misID];
                    
        }
        cout<<"Case #"<<i<<":";
        for (int j=0;j<length;j++)
            cout<<' '<<ans[j];
        cout<<endl;
    }
    return 0;
}
