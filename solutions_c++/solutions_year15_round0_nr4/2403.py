//
//  main.cpp
//  exa
//
//  Created by Mr.Note on 4/11/15.
//  Copyright (c) 2015 Mr.Note. All rights reserved.
//

#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int calcc(int x,int y,int t){
    if (t==0)
    {
        //max
        if (x>y)
            return x;
        return y;
        
        
    }
    else
    {
        //min
        if (x<y)
            return x;
        return y;
    }
    return 0;
}


int main(int argc, const char * argv[])
{
    
    ifstream in;
    ofstream out;
    in.open("D-small-attempt1.in");
    out.open("output.txt");
    int m,r,c,s,z=1,mn,mx,TMP,flg,area;
    in>>s;
    cout<<s<<endl;
    while (z<=s){
        flg=0;
        
        in>>m;
        in>>r;
        in>>c;
        if (m%2==0)
            TMP=m/2;
        else
            TMP=(m+1)/2;
        area=r*c;
        mx=calcc(r,c,0);
        mn=calcc(r, c, 1);
        
        if ((m==4&&mn<3)||area%m!=0||m>mx||mn<TMP)
            flg=1;
        
        
        if (flg==1)
            out<<"Case #"<<z<<": RICHARD"<<endl;
        else
            out<<"Case #"<<z<<": GABRIEL"<<endl;
        z++;
        
    }
    return 0;
}

