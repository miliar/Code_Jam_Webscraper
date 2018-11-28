#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std ;
int main()
{
    int t,t1=1 ;
    FILE *p ;                               //Second part of ans woking..
    p=fopen("output.txt","w") ;
    cin>>t ;
    while(t1<=t)
    {
        int n,i ;
        double a[15],b[15] ;
        cin>>n ;
        for(i=1;i<=n;i++)
        {
            cin>>a[i] ;
        }
        for(i=1;i<=n;i++)
        {
            cin>>b[i] ;
        }
        int ans1=0,ans2=0 ;
        sort(a+1,a+n+1) ;
        sort(b+1,b+n+1) ;
        /*for(i=1;i<=n;i++)
        {
            cout<<a[i]<<" " ;
        }
        cout<<"\n" ;
        for(i=1;i<=n;i++)
        {
            cout<<b[i]<<" " ;
        }
        cout<<"\n" ;
        bool visit[15] ;
        for(i=1;i<=n;i++)
        {
            visit[i]=false ;
        }*/
        int k=0,ct=n;
        for(i=n;i>0;i--)
        {
            if(a[i]>b[ct])
            {
                k++ ;
                ans1++ ;
            }
            else
            {
                ct-- ;
            }
        }
        int j ;
        int ast,bst,ae,be ;
        ast=1;bst=1;ae=n;be=n;
        for(i=1;i<=n;i++)
        {
            if(a[i]>b[bst])
            {
                ans2++ ;
                bst++ ;

            }
        }
        /*for(i=n;i>0;i--)
        {
            if(a[i]>b[i])
            {
                ans2++ ;
            }
            else
            {
                j=i ;
                while(j>0)
                {
                    if(a[i]>b[j])
                    {
                        ans2++ ;
                        break ;
                    }
                    j-- ;
                }
                i=j ;

            }
        }*/
       /* if(ans1==n)
        {
            ans2=n ;
        }
        else
        {
        for(i=ae;i>=ast;i--)
        {
             ;
            if(a[i]>b[be])
            {
                bst++ ;
                ans2++ ;
            }
            else
            {
                while(a[i]<b[be] && be>=bst)
                {
                    ast++ ;
                    be-- ;
                }
           // cout<<a[i]<<" "<<b[be]<<"\n" ;
            //cout<<ast<<" "<<i<<"\n" ;
            if(a[i]>b[be])
            {
                bst++ ;
                ans2++ ;
            }

            }

            //cout<<a[i]<<" "<<b[be]<<"\n" ;

            //cout<<i<<" "<<ans2<<"\n" ;
        }
        }*/
        //cout<<ans2<<" "<<ans1<<"\n" ;
        fprintf(p,"Case #%d: %d %d\n",t1,ans2,ans1) ;
        t1++ ;
    }
    return 0 ;
}

