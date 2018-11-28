//
//  main.cpp
//  test4
//
//  Created by Khaled on 4/9/16.
//  Copyright © 2016 Khaled. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
using namespace std;
template <typename T>
string NumberToString ( T Number )
{
    ostringstream ss;
    ss << Number;
    return ss.str();
}
int n,j;

int main(int argc, const char * argv[]) {
    // insert code here...
    int all;
    cin>>all;
    int counter= 1 ;
    string s = "";
    while(counter <= all)
    {
        s = "";
        string needed = "";
        cin>>s;
        for (int i=0;i<s.length();i++)
        {
            needed += "+";
        }
        int trials= 0;
        while( needed != s)
        {
            char start = s[0];
            for (int i=0;i<s.length();i++)
            {
                if (start == s[i])
                {
                    start == '+' ? s[i] = '-' : s[i] = '+';
                }else{
                    break;
                }
            }
            trials++;
        }
        cout<<"Case #"<<counter<<": "<<trials<<endl;
        counter++;
    }
//    string theOne = "";
//    
//    for (int i=0;i<n;i++)
//    {
//        theOne += "1";
//    }
//    for(int i = 1 ; i < n-2 ; i++)
//    {
////        
//    }
    return 0;
}
