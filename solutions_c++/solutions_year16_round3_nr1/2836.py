//
//  main.cpp
//  codejam
//
//  Created by Hui Xu on 5/8/16.
//  Copyright © 2016 Hui Xu. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

typedef pair<int,char> pic;

bool pairCompare(const pic& firstElem, const pic& secondElem) {
    return firstElem.first > secondElem.first;
    
}

#define __Test__
int main(int argc, const char * argv[]) {
#ifdef __Test__
    freopen("/Users/huixu/Desktop/APACTEST/codejam/codejam/A-large.in", "r", stdin);
    freopen("/Users/huixu/Desktop/APACTEST/codejam/codejam/A-large.out", "w", stdout);

#endif
    int T;
    cin>>T;
    for (int t=0; t<T; t++) {
        int N;
        cin>>N;
        vector<pic> P(N);
        int sumP=0;
        for (int n=0; n<N; n++) {
            int pi;
            cin>>pi;
            P[n].first=pi;
            P[n].second='A'+n;
            sumP += pi;
        }
        //int standard = sumP/2;
        
        cout<<"Case #"<<t+1<<": ";
        while (sumP!=0) {
            //int index = 0;
            sort(P.begin(), P.end(), pairCompare);
            if (sumP!=3) {
                cout<<P[0].second<<P[1].second<<' ';
                P[0].first --;
                P[1].first --;
                sumP -= 2;
            }else{
                cout<<P[0].second<<' ';
                P[0].first--;
                sumP -= 1;
            }
            
        }
        cout<<endl;
        // 逃掉最多的两组或最多的一组
        
    }
    return 0;
}
