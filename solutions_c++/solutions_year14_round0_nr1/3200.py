#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <algorithm>

using namespace std;

int main()
{
    freopen("1.in","r",stdin);
    freopen("2.txt","w",stdout);
    int num1[5][5],num2[5][5];
    int T,a,b;
    cin>>T;
    for(int l=1; l<=T; l++)
    {
        cin>>a;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                cin>>num1[i][j];
        cin>>b;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                cin>>num2[i][j];
        int n=0,m;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            {
                if(num1[a-1][i]==num2[b-1][j])
                {
                    n++;
                    m=num1[a-1][i];
                }
            }
        cout<<"Case #"<<l<<": ";
        if(n==1)
            cout<<m<<endl;
        else if(n==0)
            cout<<"Volunteer cheated!"<<endl;
        else if(n>1)
            cout<<"Bad magician!"<<endl;
    }
    return 0;
}
