//
//  main.cpp
//  Jam
//
//  Created by Beibin Li on 14-4-11.
//  Copyright (c) 2014年 Beibin. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>

using namespace std;



int union_find(vector<int> v1, vector<int> v2)
//return -1 if no common
// return 0 if more than one common
{
    int rst = -1;
    int count = 0;

    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            if(v1[i] == v2[j]){
                rst = v1[i];
                count++;
                if(count>=2){
                    return 0;
                }
            }
        }
    }
    return rst;
}

void one_case(int caseNum)
{
    int ans1, ans2, x;
    cin >> ans1;

    vector< vector<int> > deck1;
    vector< vector<int> > deck2;

    deck1.resize(4);

    for(int i=0; i<4; i++){
        deck1[i].resize(4);
        for(int j=0; j<4; j++){
            cin >> x;
            deck1[i][j] = x;
        }
    }

    cin >> ans2;

    deck2.resize(4);
    for(int i=0; i<4; i++){
        deck2[i].resize(4);
        for(int j=0; j<4; j++){
            cin >> x;
            deck2[i][j] = x;
        }
    }

    ans1--;
    ans2--;

    vector<int> a1 = deck1[ans1];
    vector<int> a2 = deck2[ans2];

    int rst = union_find(a1, a2);



    cout<< "Case #" << caseNum+1 <<": ";
    if(rst==-1){
        //no rst
        cout<<"Volunteer cheated!";

    }else if(rst==0){
        //two rst
        cout<<"Bad magician!";
    }else{
        cout << rst;
    }


    cout<<endl;
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

