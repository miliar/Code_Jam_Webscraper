#include<stdio.h>
#include<stdlib.h>
#include<map>
#include<set>
#include<algorithm>
#include<vector>
#include<iostream>
#include<fcntl.h>
#include<unistd.h>
using namespace std ;

#define MAX 1001

typedef long long LL ;

LL sq[MAX] ;
LL sq1[MAX] ;


int check_palindrome( LL num )
{
    vector< LL > v ;
    LL temp=num ;
    while(temp)
    {
        LL md = temp%10 ;
        temp = temp/10 ;
        v.push_back(md) ;

    }
    int len = v.size()-1 ;
    int st=0 ; int ed= len ;
    while(st<=ed)
    {
        if(v[st]!=v[ed])
        {
            return 0 ;
        }
        st++ ;ed-- ;
    }
    return 1 ;
}


int gen_sq()
{
    for(int i=1 ;i<MAX ; i++ ){
        sq1[i]=(LL)(i*i) ;
        if(check_palindrome(i) && check_palindrome((sq1[i])))
         sq[i]=sq[i-1]+1 ;
         else
            sq[i]=sq[i-1] ;
         }
}



int find_bs(LL x)
{
    //scanf("%lld",&x) ;

    int st = 1 ;
    int ed = MAX ;
    LL temp ;

    while(ed-st>1)
    {
        int md = (st+ed)/2 ;
        temp = sq1[md] ;
        if(temp==x)
            return md ;
        if(temp<x)
            st = md ;
        if(temp>x)
            ed = md ;

    }
   // cout<<st<<" "<<ed<<endl ;
    if(sq1[ed]<=x)
    {
        return ed ;
    }
    if(sq1[ed-1]<=x)
    {
        return ed-1 ;
    }
    if(sq1[ed-2]<=x)
    {
        return ed-2 ;
    }
}


int main()
{
    gen_sq() ;
    int test ;
    FILE *fp = freopen("C-small-attempt0.in","r",stdin) ;
    FILE *fp1 = freopen("C-small.out","w",stdout) ;
    scanf("%d",&test) ;
    for( int i=1 ;i<=test;i++)
    {
        int a,b ;
        scanf("%d%d",&a,&b) ;
        int l = find_bs( a ) ;
        //cout<<l<<endl ;
        if(a!=sq1[l])
        l+=1 ;


        int h = find_bs( b ) ;
        //cout<<h<<endl ;
       // cout<<h<<endl ;
       int res =  sq[h]- sq[l-1] ;
       printf("Case #%d: %d\n",i,res) ;

    }
}

