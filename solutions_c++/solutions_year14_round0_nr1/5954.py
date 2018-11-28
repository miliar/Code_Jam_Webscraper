
//Author£ºCY
//School: CUST

#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<cmath>
#include<stdlib.h>
#include<iomanip>
#include<list>
#include<deque>
#include<map>
#include <stdio.h>
#define PI 3.1415926535897
using namespace std;
int a[5][5];
int b[5][5];
int main()
{
    int t;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    cin>>t;
    int copt=t;
    while(t--){
        int ans1,ans2;
        cin>>ans1;
        int i,j;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                cin>>a[i][j];
            }
        }
        cin>>ans2;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                cin>>b[i][j];
            }
        }
        int temp;
        int num=0;
        int counum=0;
        for(i=1;i<=4;i++){
            temp=a[ans1][i];
            for(j=1;j<=4;j++){
                if(b[ans2][j]==temp)
                {
                    num++;
                    counum=temp;
                    break;
                }
            }
        }
        cout<<"Case #"<<copt-t<<": ";
        if(num==1){
            cout<<counum<<endl;
        }
        else if(num==0)
            cout<<"Volunteer cheated!"<<endl;
        else
            cout<<"Bad magician!"<<endl;
    }
    return 0;
}
