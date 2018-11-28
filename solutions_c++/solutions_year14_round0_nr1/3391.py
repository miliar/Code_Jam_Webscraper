#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include<cmath>
#include <sstream>
#include <algorithm>
using namespace std;


int  main()
{
    freopen("A-small-attempt0.in",  "r", stdin);
    freopen("A.out",  "w", stdout);

    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        int a,b;
        cin>>a;
        int boardA[4][4],boardB[4][4],ansa[4],ansb[4];
        for(int j=0; j<4; j++){
            for(int l=0; l<4; l++){
                cin>>boardA[j][l];
                if(j+1==a)
                    ansa[l]=boardA[j][l];
            }
        }

        cin>>b;
        for(int j=0; j<4; j++){
            for(int l=0; l<4; l++){
                cin>>boardB[j][l];
                if(j+1==b)
                    ansb[l]=boardB[j][l];
            }
        }
        sort(ansa,ansa+4);
        sort(ansb,ansb+4);

        int c=0,last=0;
         for(int j=0; j<4; j++){
            for(int l=0; l<4; l++){
             if(ansa[j]==ansb[l]){
                c++;
                last=ansa[j];
             }
            }
         }


        cout<<"Case #"<<i<<": ";
        if(c==0)
            cout<<"Volunteer cheated!"<<endl;
        else if(c==1)
            cout<<last<<endl;
        else
            cout<<"Bad magician!"<<endl;

    }

    return 0;
}
