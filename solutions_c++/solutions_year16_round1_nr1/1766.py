//
//  main.cpp
//  A
//
//  Created by 방성원 on 2016. 4. 16..
//  Copyright © 2016년 makesource. All rights reserved.
//

#include <stdio.h>
#include <deque>
#include <string.h>
using namespace std;

deque<char> ans;
char s[1111];
int N;

int main() {
    int T; scanf ("%d",&T); for (int test = 1; test <= T; test ++ ){
        scanf ("%s", s+1); N = (int)strlen(s+1);
        ans.push_back(s[1]);
        for (int i=2;i<=N;i++) {
            if (ans.front() <= s[i]) ans.push_front(s[i]);
            else ans.push_back(s[i]);
        }
        
        printf ("Case #%d: ",test);
        for (int i=0;i<ans.size();i++) printf ("%c",ans[i]);
        printf("\n");
        ans.clear();
    }
    return 0;
}
