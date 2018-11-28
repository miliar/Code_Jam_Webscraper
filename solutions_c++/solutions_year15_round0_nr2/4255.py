//
//  main.cpp
//  gcj_B
//
//  Created by Ivan_L on 2015.4.11.
//  Copyright (c) 2015年 Ivan_L. All rights reserved.
//

#include <iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main(int argc, const char * argv[]) {
    ifstream ifile;ofstream ofile;ifile.open( "B-large.in" );ofile.open( "small_out_file.out" );
    int T,n;
    int p[10000];
    ifile>>T;
    for (int i=1;i<=T;i++)
    {
        ifile>>n;
        for(int i=0;i<n;i++)ifile>>p[i];
        int ans=2147483647;
        for(int i=1;i<=1000;i++)
        {
            int s=0;
            for(int j=0;j<n;j++)s+=(p[j]+i-1)/i-1;
            ans=ans<s+i?ans:s+i;
        }
        ofile<<"Case #"<<i<<": "<<ans<<endl;
    }
    ifile.close();
    ofile.close();
    return 0;
}
