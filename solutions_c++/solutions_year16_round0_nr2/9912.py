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
        std::string curstring;
        int count=0;
        std::cin>>curstring;
        for (int j=0; j<curstring.length()-1; j++)
        {
            if (curstring[j+1]!=curstring[j])
                count++;
        }
        if (curstring[curstring.length()-1]=='-')
            count++;
        std::cout<<"Case #"<< i+1<< ": " << count<< std::endl;
    }
    // insert code here...
    return 0;
}
