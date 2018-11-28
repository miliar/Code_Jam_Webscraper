#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<bitset>
#include<algorithm>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<iomanip>
#include<climits>
#include<cstdlib>
#include<cmath> 
using namespace std;
int main()
{
        int te;
        cin>>te;
for(int x=1;x<=te;x++)
{
   int a[4][4];
   int row;
   cin>>row;
   for(int i=0;i<4;i++)
     for(int j=0;j<4;j++)
        cin>>a[i][j];
vector<int>v;
for(int i=0;i<4;i++) v.push_back(a[row-1][i]);
   cin>>row;
   for(int i=0;i<4;i++)
     for(int j=0;j<4;j++)
        cin>>a[i][j];
bool flg=0,printed=0;
int ans;
for(int i=0;i<4;i++)
{
        if(printed) break;
        for(int j=0;j<4;j++)
        {
                if(flg==1 && a[row-1][j]==v[i]) 
                {
                        printf("Case #%d: Bad magician!\n",x);
printed=1;
break;                        
                }
               else if(a[row-1][j]==v[i]){ ans=v[i]; flg=1; }
        }

}
if(!printed && flg==0){ 
                        printf("Case #%d: Volunteer cheated!\n",x);
printed=1;
}
if(!printed) printf("Case #%d: %d\n",x,ans);
}
}
