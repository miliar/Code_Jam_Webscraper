#include<stdio.h>
#include<algorithm>
using namespace std;

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

double f[1009] , s[1009];
int n;

int main()
{
    
    int i , a , j , cases , ret , ret1;
    int caseID = 0;
    
    fscanf(in,"%d",&cases);
    while(cases--)
    {
        fscanf(in,"%d",&n);
        for(i=0;i<n;i++)
            fscanf(in,"%lf",&f[i]);
        for(i=0;i<n;i++)
            fscanf(in,"%lf",&s[i]);
        
        sort(f,f+n);
        sort(s,s+n);
        
        ret = ret1 = 0;
        
        a = 0;
        for(i=0;i<n;i++)
        {
            ret1++;
            while(a < n && s[a] < f[i]) a++;
            if(a < n) ret1-- , a++;
        }
        
        j = n-1;
        for(i=n-1;i>-1;i--)
            if(f[j] > s[i]) ret++ , j--;
        
        fprintf(out,"Case #%d: %d %d\n",++caseID,ret,ret1);
        
    }
    
    return 0;
}
