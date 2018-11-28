#include<cstdio>
#include<string>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cctype>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<fstream>
#include<numeric>
#include<map>
#include<sstream>
#include<iterator>
#define M 100
using namespace std;
typedef long  ll;
int a[M][M];
bool test(int r, int c,int val)
{
    int i;
    for(i=0;i<c;i++)
        if(a[r][i]==val) return true;
    return false;
}
bool tes(int r, int c,int val)
{
    int i;
    for(i=0;i<c;i++)
        if(a[i][r]==val) return true;
    return false;
}
int one(int r, int c, int *al)
{
    int i,j=0;
    for(i=0;i<c;i++)
        if(a[r][i]==1)
        {
            al[j] = i;
            j++;
        }
        return j;
}
int main()
{

	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
    int t, j,cs=1,k,l,n,m,i,c,r;
    int ro[M],co[M],f;
	cin >>t ;
	while(t--)
    {

		        for(i=0;i<10;i++)
			        for(j=0;j<10;j++)
					{
						co[i]=a[i][j] =0;
						 
					}

        f=0;
        cin >> n >>m;
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
            cin >> a[i][j];
        printf("Case #%d: ",cs++);
        for(i=0;i<n;i++)
        {
            if(test(i,m,2)&test(i,m,1))
            {
                k = one(i,m,co);
                for(l=0;l<k;l++)
                {
                    if(tes(co[l],n,2))
                    {
                        f=1;
                        i= n;
                        puts("NO");
                        break;
                    }
                }
            }

        }
        if(!f)puts("YES");

    }
	return 0;
}
