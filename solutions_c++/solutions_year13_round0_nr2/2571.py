#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int info(int arrayy[][105] ,int i,int j,int n,int m)
{
    int randns = 0;
    for(int l = 0; l < n; l++)
    {
        if(arrayy[l][j]>arrayy[i][j])
        {
            randns=1;
            break;
        }
    }
    if(randns==1)
   {
       for(int l = 0; l < m; l++)
        {
            if(arrayy[i][l] > arrayy[i][j])
            return 1;
        }
   }
    return 0;
}
int main()
{
    int t,k=1,z;
    cin>>t;
    for (int test = 1; test <= t; test++) {
        int n,m,i,j,rand=0;
		int arrayy[105][105];
       cin>>n>>m;
        for(i=0; i < n; i++){
            for(j = 0; j < m; j++){
            cin >> arrayy[i][j];
            }
        }
        for(i = 0; i < n; i++){
            for(j = 0; j < m; j++){
                if(info (arrayy,i,j,n,m) == 1){
                    rand=1;
                    break;
                    }
                }
            if(rand == 1)
            break;
            }
        if(rand != 1)
        cout<<"Case #"<<test<<": "<<"YES"<<endl;
        else
         cout<<"Case #"<<test<<": "<<"NO"<<endl;
    }
    return 0;
}
