//
//  main.cpp
//  codejam
//
//  Created by Yan Zhu on 4/9/16.
//  Copyright © 2016 Yan Zhu. All rights reserved.
//

#include <iostream>
#include <string>

int main(int argc, const char * argv[]) {
    int casenum;
    std::cin>>casenum;
    for (int i=0; i<casenum; i++)
    {
        int K,C,S;
        std::cin>>K;
        std::cin>>C;
        std::cin>>S;
        std::cout<<"Case #"<< i+1<< ": ";
        for (int j=1; j<S; j++)
        {
            std::cout<< j << " ";
        }
        std::cout << S<<std::endl;
    }
    // insert code here...
    return 0;
}
