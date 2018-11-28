//
//  main.cpp
//  test
//
//  Created by Shreyas Sinha on 09/04/16.
//  Copyright © 2016 Shreyas Sinha. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

typedef long long ll;

ll t,n;
int a[10];

int foo(){
    int count=0;
    ll temp=n;
    while (temp>0) {
        if(a[temp%10]==0){
            count++;
            a[temp%10]=1;
        }
        temp/=10;
    }
    return count;
}

int main() {
    ifstream infile;
    ofstream outfile;
    infile.open("A-large.in");
    outfile.open("output.in");
    infile>>t;
    for(int y=1;y<=t;y++){
        infile>>n;
        if (n==0) {
            outfile<<"Case #"<<y<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        for (int i=0; i<10; i++) {
                a[i]=0;
        }
        int count=0;
        count+=foo();
        int j=2;
        while (count!=10) {
            n=n/(j-1)*j;
            count+=foo();
            j++;
        }
        outfile<<"Case #"<<y<<": "<<n<<endl;
    }
    return 0;
}
