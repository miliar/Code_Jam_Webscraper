/*ID: amr.f.eldfrawy
LANG: C++
*/
#include <fstream>
#include <string>
#include<iostream>
#include<stdio.h>
#include<vector>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<math.h>
#define INF 1000000
#define MOD  1000000007
#define MAX 100000
using namespace std;
string arr[20];
int F[100];
int Fac(int n )
{
    int res = 1 ;
    for(int i = 1 ; i<=n ; i++)
        res= ( (res%MOD) * (i%MOD))%MOD;

    return res%MOD;
}
int main()
{

     freopen("S.in","r",stdin);
      freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    int q=1;
    while(t--)
    {

        int n ;
        cin >> n ;
        map<string , int >M;
        for (int i=0; i<n; i++)
        {
            cin >> arr[i];
            M[arr[i]]++;
        }
        sort(arr,arr+n);
        int ans = 0;
        do
        {
            int k=0;
            memset(F,-1,sizeof F);
            bool res=0;
            for(int i = 0 ; i < n  &&!res; i++)
            {
                for(int j  =  0 ; j < arr[i].size() && !res; j++)
                {

                    char c = arr[i][j];

                    if(F[c-'a']==-1)
                        F[c-'a']=k;
                    else
                    {
                        if(F[c-'a']!=k-1)
                        {
                            res = 1;
                            break;
                        }
                        else
                        {
                            F[c-'a']=k;
                        }
                    }
                    k++;
                }

            }

            if(!res)
                ans = ((ans%MOD) + 1 )%MOD ;


        }
        while(next_permutation(arr,arr+n));

        for(map<string , int >::iterator it=M.begin() ; it!=M.end() ; it++)
        {
            //cout <<it->second <<endl;
            ans = ((Fac((it->second))%MOD) * (ans%MOD))%MOD ;
        }
        printf("Case #%d: %d\n",q++,ans);
    }



    return  0;
}
