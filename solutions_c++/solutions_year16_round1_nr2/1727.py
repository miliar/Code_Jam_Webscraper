//
//  main.cpp
//  B2
//
//  Created by 방성원 on 2016. 4. 16..
//  Copyright © 2016년 makesource. All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <memory.h>
using namespace std;

vector<int> ans;
int height[2555];

int main() {
    int T; scanf ("%d",&T); for (int test = 1; test <= T; test ++) {
        int N; scanf ("%d",&N);
        for (int i=1;i<2*N;i++) for (int j=1;j<=N;j++) {
            int k; scanf ("%d",&k); height[k] ++;
        }
        
        for (int i=1;i<=2500;i++) if (height[i] % 2 == 1) ans.push_back(i);
        sort(ans.begin(),ans.end());
        printf ("Case #%d: ",test);
        for (int i=0;i<ans.size();i++) printf("%d ",ans[i]);
        printf("\n");
        
        memset(height, 0, sizeof height);
        ans.clear();
    }
    return 0;
}
