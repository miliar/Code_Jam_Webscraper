//
//  main.cpp
//  Ominious omino
//
//  Created by Shreyas Sinha on 11/04/15.
//  Copyright (c) 2015 Shreyas Sinha. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;
int main() {
    int flag,t,x,r,c;
    
    ofstream outfile;
    ifstream infile;
    infile.open("D-small-attempt0.in");
    outfile.open("output.in");
    infile>>t;
    for (int k=1; k<=t; k++) {
        infile>>x;
        infile>>r;
        infile>>c;
        flag=0;
        switch (x) {
            case 2:if(!((r*c)%2==0)){
                flag=1;
            }
                break;
            case 3:if(!((r*c)%3==0&&(r*c)>3)){
                flag=1;
            }
                break;
            case 4:if(!((r*c)%4==0&&(r*c)>=12)){
                flag=1;
            }
                break;
        }
        if(flag){
        outfile<<"Case #"<<k<<": RICHARD\n";
        }
        else{
            
            outfile<<"Case #"<<k<<": GABRIEL\n";
        }
    }
    outfile.close();
    infile.close();
    return 0;
}
