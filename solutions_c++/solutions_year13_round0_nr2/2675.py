#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string.h>

using namespace std;

int arr[10][10];
bool dp[10][10];
int n,m;
int t;

bool atas(int i, int j, int z)
{
     bool bener=true;
     for (int x=0; x<i; x++)
     {
         if (arr[x][j] != z)
         {
            bener=false;
         }
     }
     
     return bener;
 }

bool bawah(int i, int j, int z)
{
     bool bener=true;
     for (int x=i+1; x<n; x++)
     {
         if (arr[x][j] != z)
         {
            bener=false;
         }
     }
     
     return bener;
 }
 
bool kiri(int i, int j, int z)
{
     bool bener=true;
     for (int y=0; y<j; y++)
     {
         if (arr[i][y] != z)
         {
            bener=false;
         }
     }
     
     return bener;
 }
 
bool kanan(int i, int j, int z)
{
     bool bener=true;
     for (int y=j+1; y<m; y++)
     {
         if (arr[i][y] != z)
         {
            bener=false;
         }
     }
     
     return bener;
}

bool cek()
{
     bool bisa=true;
     for (int i=0; i<n; i++)
     {
         for (int j=0; j<m; j++)
         {
             if (arr[i][j]==1)
             {
                 if (!((kanan(i,j,arr[i][j]) && kiri(i,j,arr[i][j]) ) || (atas(i,j,arr[i][j]) && bawah(i,j,arr[i][j]))))
                 {
                     bisa=false;
                     break;
                 }
             }
         }
     }
     
     return bisa;
}

int main ()
{
    scanf("%d",&t);
    for (int z=1; z<=t; z++)
    {
        scanf("%d%d",&n,&m);
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<m; j++)
            {
                scanf("%d",&arr[i][j]);
            }
        }
        
        if (cek()) printf("Case #%d: YES\n",z);
        else
        printf("Case #%d: NO\n",z);
        
        
    }
    
//    system("pause");
    return 0;
}
