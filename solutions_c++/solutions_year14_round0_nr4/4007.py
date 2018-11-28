             /*
     shubham_1286(shubham verma)
                                   */
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<vector>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<list>
#include<deque>
#include<bitset>
#include<limits.h>
#include<sstream>
#define max(x,y) x>y?x:y
#define min(x,y) x<y?x:y
#define sd(a)  scanf("%d",&a);
#define slld(a)  scanf("%lld",&a);
#define sllu(a)  scanf("%llu",&a);
#define pd(a)  printf("%d\n",a);
#define plld(a)  printf("%lld\n",a);
#define pllu(a)  printf("%llu\n",a);
#define inf INT_MAX
#define low INT_MIN
#define mod 1000000009
#define ull unsigned long long
#define ll long long
using namespace std;
double naomi[1010];
double ken[1010];
bool nao[1010];
bool ke[1010];
int main()
{
// freopen("c:\\users\\verma\\desktop\\dla.txt","r",stdin);
  //freopen("c:\\users\\verma\\desktop\\ela.txt","w",stdout);
  int t,test_case=1;
  sd(t);
  while(test_case<=t)
  {
        int n;
        sd(n);
        
        for(int i=0;i<1010;i++)
        nao[i]=false,ke[i]=false;
        
        for(int i=0;i<n;i++)
        scanf("%lf",&naomi[i]);
        
         for(int i=0;i<n;i++)
        scanf("%lf",&ken[i]);
  
  
       sort(naomi,naomi+n);
       sort(ken,ken+n);
       bool temp=true;int indx=0,coun=0,opt=0;
       
       for(int i=n-1;i>=0;i--)
       {
            temp=true;
            for(int j=0;j<=n-1;j++)
            {
 //                cout<<i<<" "<<j<<" "<<nao[j]<<" "<<ken[i]<<"  "<<naomi[j]<<endl;
                if(ken[i]<naomi[j] && !nao[j])
                {
   //                 cout<<i<<" "<<ken[i]<<" hhh "<<naomi[j]<<endl;
                    coun++;
                    nao[j]=true;
                    temp=false;
                    break;
                }
               
            }
             if(temp)
                {
                    nao[indx]=true;
                     indx++;
                }
        }
        
        
        temp=true;
        indx=0;
        for(int i=n-1;i>=0;i--)
        {
            temp=true;
            for(int j=0;j<=n-1;j++)
            {
                if(naomi[i]<ken[j] && !ke[j])
                {
                    ke[j]=true;
                    temp=false;
                    break;
                }
            }
            if(temp)
            {
                opt++;
                ke[indx]=true;
                indx++;
            }
        }
        
        
        printf("Case #%d: %d %d\n",test_case,coun,opt);
       
            
        test_case++;
        
                
            }
                
}
