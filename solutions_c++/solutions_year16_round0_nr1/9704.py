//
//  main.cpp
//  CodeJam16CountingSheep
//
//  Created by Tanu on 4/9/16.
//  Copyright © 2016 Tanu Singhal. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[])
{

    int T;
    cin>>T;
    long int N[T];
    for(int i=0;i<T;i++)
        cin>>N[i];
    
    for(int i=0;i<T;i++)
    {
        if(N[i] == 0)
        {
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
            continue;
        }
        
        int arr[10];
        for(int x=0;x<10;x++)
            arr[x] = 0;
        
        
        for(int nCount = 1; nCount >= 1; nCount++)
        {
            long nVal = N[i]*nCount;
            
            for(long p = nVal; p > 0; p = p/10)
            {
                arr[p%10] = 1;
            }
        
            if(arr[0]&&arr[1]&&arr[2]&&arr[3]&&arr[4]&&arr[5]&&arr[6]&&arr[7]&&arr[8]&&arr[9])
            {
                cout<<"Case #"<<i+1<<": "<<nVal<<endl;
                break;
            }
        }
    }
    
    return 0;
}
