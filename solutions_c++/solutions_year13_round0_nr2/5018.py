#include<stdio.h>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int info(vector < vector <int> > v ,int i,int j,int n,int m)
{
    int cns = 0;
    for(int l = 0; l < n; l++)
    {
        if(v[l][j]>v[i][j])
        {
            cns=1;
            break;
        }
    }
    if(cns==1)
   {
       for(int l = 0; l < m; l++)
        {
            if(v[i][l] > v[i][j])
            return 1;
        }
   }
    return 0;
}
int main()
{
    int t,k=1,z;
    cin>>t;
    for (int y = 1; y <= t; y++) {
        int n,m,i,j,c=0;
		vector < vector <int> > v (105, vector <int> (105));
       cin>>n>>m;
        for(i=0; i < n; i++){
            for(j = 0; j < m; j++){
            cin >> v[i][j];
            }
        }
        for(i = 0; i < n; i++){
            for(j = 0; j < m; j++){
                if(info (v,i,j,n,m) == 1){
                    c=1;
                    break;
                    }
                }
            if(c == 1)
            break;
            }
        if(c != 1)
        cout<<"Case #"<<y<<": "<<"YES"<<endl;
        else
         cout<<"Case #"<<y<<": "<<"NO"<<endl;
    }
    return 0;
}
