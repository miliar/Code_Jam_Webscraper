/*************************************
**----------------------------------**
*|**********************************|*
*|*  CODE By : Mohd. Ausaf Jafri   *|*
*|*     ECE, MNNIT , Allahabad     *|*
*|*                                *|*
*|*      ausafjafri@gmail.com      *|*
*|*   "Think Twice, Code Once"     *|*
*|**********************************|*
**----------------------------------**
**************************************/

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define vi(v,size) vector<int>v(size) 
#define upto(n) for(int i=0;i<n;i++)
#define from(a,b) for(int i=a;i<=b;i++)
#define rev(a,b) for(int i=a;i>=b;i--)
#define mp make_pair
#define pb push_back
#define mod 1000000007

#define inc(c) scanf("%c",&c);
#define ins(s) scanf("%s",s);
#define ind(n) scanf("%d",&n);
#define inlld(n) scanf("%lld",&n);
#define ind2(n,m) scanf("%d%d",&n,&m);
#define inlld2(n,m) scanf("%lld%lld",&n,&m);

#define opc(c) printf("%c\n",c);
#define ops(s) printf("%s\n",s);
#define opd(n) printf("%d\n",n);
#define oplld(n) printf("%lld\n",n);
#define opd2(n,m) printf("%d %d\n",n,m);
#define oplld2(n,m) printf("%lld %lld\n",n,m);

int main()
{
      int tt,test=1;
      ind(tt)
        while(tt--)
        {   int ans,l=0,plus=0;
            char str[1000];
            //scanf("%c",&ch);
            scanf("%s",str);
            int n=strlen(str);
            for(int i=0;i<n;i++)
            {
                if(str[i]=='+')
                {
                    plus++;
                    l=i+1;
                    while((str[l]=='+')&&(l<n))
                        l++;
                   // printf("l=%d\n",l);
                    i=l;
                }
                
            }
            if(str[n-1]=='+')
                plus=plus-1;
            ans=2*plus + 1;
            if(str[0]=='+')
                ans--;
            
            printf("Case #%d: %d\n",test,ans);
            test++;
        }
}