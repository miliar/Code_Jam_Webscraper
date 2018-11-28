//
//  main.cpp
//  Round1B_A
//
//  Created by Sambhav on 5/4/13.
//  Copyright (c) 2013 Sword Software. All rights reserved.
//


#include <iostream>
#include<fstream>

using namespace std;

unsigned long int steps (int f, int l, unsigned long long int n[], unsigned long long int A) {
    unsigned long int result =0, rt;
    unsigned long long int t1;
    
    if (f>=l) return 0;
    
    if (n[f]<A) {
        A += n[f];
        rt = steps(f+1, l, n, A);
        return (rt > l-f)? l-f: rt;
    } else {
        t1 = A;

        for (int i = 0 ; i < (l-f-1); i++) {
            t1 = 2*t1 -1;
            result++;
            if (t1 > n[f]) {
                rt = steps(f+1, l, n, t1+n[f]);
                return (rt > l-f)? result+l-f : rt + result;
            }
        }
        return l-f;
    }
}

int main(int argc, const char * argv[])
{
    
    ofstream op("/Users/sambhav/Dropbox/codejam/2013/Round1B_A/A-small-attempt1.op");
	ifstream ip("/Users/sambhav/Dropbox/codejam/2013/Round1B_A/A-small-attempt1.in");
    
    unsigned long long int T,A,n[100],temp1,temp2;
    int i,j,k,N;
    unsigned long int result;
    
    ip>>T;
    
    for(i=0;i<T;i++)
    {
        //Fetch the input for this test case
        ip>>A>>N;
        for (j=0; j<N; j++) {
            ip>>temp1;
            for (k=0; k<j; k++) {
                if (n[k]>temp1) {
                    temp2 = n[k];
                    n[k] = temp1;
                    temp1 = temp2;
                }
            }
            n[k] = temp1;
        }
        
//        for (j=0; j<N; j++) {
//            cout << n[j] << ", ";
//        }
//        cout << "\n";
        result = steps(0, N, n, A);
        
        cout<<"Case #"<<i+1<<": "<<result<<"\n";
        op<<"Case #"<<i+1<<": "<<result<<"\n";
        
    }
    op.close();
    ip.close();
    return 0;
}



