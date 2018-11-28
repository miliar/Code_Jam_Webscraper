#include<fstream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<set>
using namespace std;

ofstream fout("ans.out");
ifstream fin("A-large.in");

int n,t,m;
int a[10001];

int ans;
bool is_use[10001];


bool cmp2(int xx,int yy)
{
     return xx>yy;
}


int main()
{
    int i,j,k,times;
    int temp;
    int p,q;
    fin>>t;
    
    for(times=1;times<=t;times++)
    {
        fin>>n>>m;
        
        for(i=1;i<=n;i++)
        {
            fin>>a[i];
        }
        
        sort(a+1,a+n+1,cmp2);
        
        ans=0;
        p=1;q=n;
        while(p<=q)
        {
            if(a[p]+a[q]<=m && p!=q)
            {
                ans++;
                p++;q--;
            }
            else
            {
                p++;
                ans++;
            }
        }
        
        //fout<<m<<endl;
        //for(i=1;i<=n;i++)
        //{
       //     fout<<a[i]<<' ';
       // }
       // fout<<endl;
        
        fout<<"Case #"<<times<<": ";
        fout<<ans<<endl;
    }
    
    
    system("pause");
    return 0;
}
