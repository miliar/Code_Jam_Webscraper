//
//  main.cpp
//  CodeJam
//
//  Created by Yen Feng Cheng on 4/9/16.
//  Copyright © 2016 Yen-Feng Cheng. All rights reserved.
//

#include <iostream>
using namespace std;

bool isAllOne(bool digit[10]) {
	for ( int i=0; i<10; i++ ) {
		if (digit[i]==0) return 0;
	}
	return 1;
}

int main(int argc, const char * argv[]) {
	// insert code here...
	
	int T, N, x=1;
	cin>>T;
	for ( int i=0; i<T; i++ ) {
		cin>>N;
		
		if ( N==0 ) {
			cout<<"Case #"<<x<<": INSOMNIA"<<endl;
			x++;
		}else {
			bool digit[10]={0};
			int tmp, k;
			for ( k=1; isAllOne(digit)==0; k++ ) {
				tmp = N*k;
				while ( tmp!=0 ) {
					digit[tmp%10]=1;
					tmp/=10;
				}
			}
			cout<<"Case #"<<x<<": "<<N*(k-1)<<endl;	//k or k-1
			x++;
		}
	}
	
    return 0;
}

