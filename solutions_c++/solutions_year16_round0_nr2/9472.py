//============================================================================
// Name        : pancake.cpp
// Author      : Xining Li
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
//
//  main.cpp
//  pancake
//
//  Created by songnan on 16/4/8.
//  Copyright (c) 2016Äê songnan. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
const char happy='+';
const char unhappy='-';
int Count_Node(string s){
    //vector<int> cal;
    char flag=s[0];
    int count=0;
    string s1=s;
    for(int i=0;i<s.length();i++){
        if(flag!=s[i]){
            //cout<< i << "\n";
            flag=s[i];
            //cal.push_back(i-1);

//            //output_string
//            string s_after_node=s.substr(i);
//            //cout << s_after_node<<'\n';
//            string s_before_node="";
//            for(int j=0;j<i;j++){
//                s_before_node+=flag;
//            }
//            s1=s_before_node+s_after_node;
//            cout << "s1="<<s1<< '\n';

            count++;
        }
    }
    if(flag==unhappy){
//        s1="";
//        for(int i=0;i<s.length();i++){
//            s1+=happy;
//        }
//        cout<<"s1="<<s1<<'\n';
        count++;
    }
//    for(int i=0;i<cal.size();i++){
//        cout<< cal[i]<<'\n';
//    }


    return count;

}

int main(int argc, const char * argv[]) {
	ifstream myfile;
	ofstream out("output.txt");
	int n;
	myfile.open("input.in");
	    if (myfile.fail())
	    {
	        cout << "Read file fail!!!" << endl;
	        return -1;
	    }
	    myfile >> n;
	    string s;
	    for(int i=0;i<n;i++){
	    	myfile>> s;
	    	out <<"Case #"<<i+1<<": "<< Count_Node(s)<<'\n';
	    }
	    myfile.close();
	    out.close();
    return 0;
}
