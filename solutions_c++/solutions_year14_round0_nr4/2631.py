//
//  main.cpp
//  GCJQD
//
//  Created by Ningchen Ying on 4/12/14.
//  Copyright (c) 2014 Ningchen Ying. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstdio>

using namespace std;

double a[1010],b[1010];

int main(int argc, const char * argv[])
{
    
    int T,N;
    freopen("/Users/YNingC/Documents/CodeForces/GCJQD/GCJQD/D-large.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJQD/GCJQD/D-large.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        cin>>N;
        for(int i=0;i<N;i++){
            cin>>a[i];
        }
        for(int i=0;i<N;i++){
            cin>>b[i];
        }
        sort(a,a+N);
        sort(b,b+N);
        int k=0,kk=0;
        int j=N-1;
        for(int i=N-1;i>=0 && j>=0;i--){
            while(j>=0){
                if(b[i]>a[j]){
                    j--;
                    k++;
                    break;
                }
                j--;
            }
        }
        j=N-1;
        for(int i=N-1;i>=0 && j>=0;i--){
            while(j>=0){
                if(a[i]>b[j]){
                    j--;
                    kk++;
                    break;
                }
                j--;
            }
        }
        
        cout<<"Case #"<<cas<<": "<<kk<<" "<<N-k<<endl;
    }
    return 0;
}

