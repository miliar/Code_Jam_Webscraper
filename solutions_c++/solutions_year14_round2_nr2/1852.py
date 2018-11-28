//
//  main.cpp
//  repeat
//
//  Created by Beibin Li on 14-5-3.
//  Copyright (c) 2014年 Beibin. All rights reserved.
//

#include <iostream>

using namespace std;



int one_case(int caseNum)
{

    int A, B, X;
    cin >> A >> B >> X ;


    int count = 0 ;

    for(int i=0 ;i<A; i++){
        for(int j=0; j<B; j++){
            if((i&j)<X) count++;
        }
    }

    cout<<"Case #"<<caseNum+1<<": "<<count<<endl;



    return 0;

}



int main(int argc, const char * argv[])
{


    //these two lines should be quoted out. Used for Xcode
    //    ifstream arq(getenv("try"));
    //    cin.rdbuf(arq.rdbuf());

    int numCase = 0;
    cin >> numCase;

    for(int i=0; i<numCase; i++){
        one_case(i);
    }


    return 0;
}