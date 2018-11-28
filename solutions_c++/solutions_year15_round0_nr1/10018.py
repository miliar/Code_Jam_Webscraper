//
//  main.cpp
//  Qualification_01
//
//  Created by 鍾有志 on 2015/4/11.
//  Copyright (c) 2015年 鍾有志. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    fstream input;
    fstream output;
    
    input.open("A-small-attempt0.in",ios::in);
    if(!input){
        cout<<"Input File Can't Open"<<endl;
        exit(1);
    }
    output.open("sol-small.txt",ios::out);
    if (!output) {
        cout<<"Output File Can't Open"<<endl;
        exit(1);
    }
    string writeStr;
    int testCases=0;
    while (!input.eof()) {
        input>>testCases;
        cout<<"testCases:"<<testCases<<endl;
        
        int SiMax = 0;
        int curTotalAuds;
        int friendNeed;
        string SiKth;
        
        for (int i=1; i<=testCases; i++) {
            input>>SiMax;
            input>>SiKth;
            curTotalAuds = 0;
            friendNeed = 0;
            for(int j=0; j<=SiMax ;j++){
                char temp;
                temp = SiKth[j];
                int intTemp = temp - '0';
                //cout<<j<<"[ooo]"<<intTemp<<endl;
                if (intTemp != 0) {
                    if (curTotalAuds >= j) {
                        curTotalAuds += intTemp;
                        //cout<<j<<"[xxx]"<<curTotalAuds<<endl;
                    }else{
                        int tempNeed = j-curTotalAuds;
                        //cout<<j<<"[add]"<<tempNeed<<endl;
                        
                        friendNeed += tempNeed;
                        curTotalAuds += friendNeed;
                        curTotalAuds += intTemp;
                        //cout<<j<<"[cur]"<<curTotalAuds<<endl;
                    }
                }
            }
            cout<<"Case #"<<i<<": "<<friendNeed<<endl;
            writeStr="Case #"+to_string(i)+": "+to_string(friendNeed)+"\n";
            output << writeStr;
            //cout<<SiMax<<" "<<SiKth<<endl;
            //cout<<SiKth.size()<<endl;
        }
        //cout<<"Case #"<<i<<": "<<sol<<endl;
        //writeStr="Case #"+to_string(i)+": "+to_string(sol)+"\n";
        //output << writeStr;
        
        output.close();
    }
    return 0;
}