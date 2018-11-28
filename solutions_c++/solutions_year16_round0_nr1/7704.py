//
//  main.cpp
//  Codepractice
//
//  Created by Sanya B. Taneja on 09/04/16.
//  Copyright (c) 2016 Name. All rights reserved.
//

#include <iostream>
#include <math.h>


using namespace std;

int main() {

    int flag=0, k,digits, divisor, t, l=1, i, j;
    long int x, m, n, d;
    int count[10];
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin>>t;
    while(t>0)
    {
        
        cin>>n;
        for(int p=0;p<10;p++)
            count[p]=0;
        x=n;
        m=n;
        k=2;
        if(x==0)
        {
            cout<<"Case #"<<l<<": INSOMNIA\n";
        }
        if(x>0)
        {
            do
            {
                
                digits=log10((float)x)+1;
                for(i=digits-1;i>=0;i--)
                {
                    divisor=pow((float)10,i);
                    d=x/divisor;
                    x-=d*divisor;
                    count[d]=1;
                 
                    
                }
                for(j=0;j<10;j++)
                {
                    if(count[j]==0)
                    {
               
                        x=n*k;
                        m=x;
                        k++;
                        flag=0;
                        break;
                        
                    }
                }
                if(j==10)
                {
                    cout<<"Case #"<<l<<": "<<m<<"\n";
                    flag=1;
                    break;
                }
            }while(flag==0);
            
        }
        l++;
        t--;
    }
    getchar();
	return 0;
}