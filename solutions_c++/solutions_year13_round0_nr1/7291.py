#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<map>ifct
#define for(i) for(int i=0;i<4;i++)
#define for(j) for(int j=0;j<4;j++)
#define init int cx=0,co=0,ct=0;
#define ifx if(a[i][j] == 'X')
#define ifo if(a[i][j] == 'O')
#define ifd if(a[i][j] == '.')
#define ift if(a[i][j] == 'T')
#define ifcx if(cx + ct > 3)
#define ifaf if (ans == false)
#define ifco if(co + ct >3)
using namespace std;
ifstream input ("A-large.in") ;
ofstream output ("output8.txt") ;
bool ans = false ;
bool ans2 = false ;
char a[4][4] ;
int cd = 0;
int check(int cx,int co,int ct)
{
    ans = false ;
    ifcx
    {
        //cout<<"cx = "<<cx<<"co = "<<co<<"ct = "<<ct<<endl ;
        output<<"X won"<<endl ;
        ans = true;
        ans2 = true ;
        return 1 ;
    }
    ifco
    {
        //cout<<"cx = "<<cx<<"co = "<<co<<"ct = "<<ct<<endl ;
        output<<"O won"<<endl ;
        ans = true ;
        ans2 = true ;
        return 1 ;
    }
    return 0 ;
}
int hf()
{
    init ;
    for(i)
    {
        cx =0 ;co= 0;ct = 0;
        for(j)
    {
        ifx cx++;
        ift ct++;
        ifo co++;
        ifd cd++ ;
        //cout<<"cx = "<<cx<<"co = "<<co<<"ct = "<<ct<<endl ;
    }

   if(check(cx,co,ct)==1)
        ans = true ;
    }
    return 1;
}
int vf()
{

    if(ans2 == true)
        return 0;
    for(j)
    {
        init ;
        for(i)
    {
        ifx cx++;
        ift ct++;
        ifo co++;
    }

   if(check(cx,co,ct)==1)
        ans = true ;
    }
    return 1;
}
int d1()
{

    if(ans2 == true)
        return 0;
    init ;
    for(i)
        for(j)
    {
        if(i != j)
            continue ;
        ifx cx++;
        ift ct++;
        ifo co++;
    }

   if(check(cx,co,ct)==1)
        ans = true ;
    return 1;
}
int d2()
{

    if(ans2 == true)
        return 0;
    init ;
    int k = 4;
    while(k>= 0)
    {
        k-- ;
        for(j)
    {
        if(k+j != 3)
            continue ;
        if(a[k][j] == 'X') cx++;
        if(a[k][j] == 'T') ct++;
        if(a[k][j] == 'O') co++;
    }
    }
   if(check(cx,co,ct)==1)
        ans = true ;
    return 1;
}
int fn()
{
    if(ans2 == true)
        return 0;
        if(cd >0)
            output<<"Game has not completed"<<endl ;
        else
            {
                //cout<<"ans = "<<ans<<endl ;
             output<<"Draw"<<endl ; }
}
using namespace std ;
int main()
{
    int cases ,temp;
    string z;
    getline(input,z) ;
    cases = atoi(z.c_str()) ;
    temp = cases ;
    //cout<<cases<<endl;
    while(cases--)
    {
        cd =0 ;
        ans = false ;
        ans2 = false ;
        string s;
        for(i)
        {
            getline(input,s) ;
            for(j)
            {
                a[i][j] = s[j] ;
            }

        }
        output<<"Case #"<<temp- cases<<": " ;
        hf();
        ifaf vf();
        ifaf d1();
        ifaf d2();
        ifaf fn() ;
        getline(input,s) ;
    }
    return 0;
}
