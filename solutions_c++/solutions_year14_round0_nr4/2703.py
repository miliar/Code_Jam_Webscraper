//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
using namespace std;
double ar[10009],pr[10009],temp1[10009],temp2[10009],ap[10009],pp[10009];
int check(int a)
{
    int s,d,f,g,h,j,k,l;
    for(s=1;s<=a;s++)
    {
        temp1[s]=ar[s];
    }
    for(s=1;s<=a;s++)
    {
        temp2[s]=pr[s];
    }
    reverse(temp2+1,temp2+a+1);
    for(s=1;s<=a;s++)
    {
        if(temp1[s]>temp2[s]) return 0;
    }
    return 1;
}
int checkk(int a)
{
    int s,d,f,g,h,j,k,l;
    for(s=1;s<=a;s++)
    {
        temp1[s]=ap[s];
    }
    for(s=1;s<=a;s++)
    {
        temp2[s]=pp[s];
    }
    reverse(temp1+1,temp1+a+1);
    for(s=1;s<=a;s++)
    {
        if(temp1[s]<temp2[s]) return 0;
    }
    return s;
}
int checkwar(int a)
{
    int s,d,f,g,h,j,k,l;
    for(s=a;s>=1;s--)
    {
        if(check(s)) return s;
    }
    return 0;
}
int checkdec(int a)
{
    int s,d,f,g,h,j,k,l;
    for(s=a;s>=1;s--)
    {
        if(checkk(s)) return s;
    }
    return 0;
}
int main()
{
    int a,s,d,f,g,h,j,k,l;
    freopen("in.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    cin>>a;
    for(s=1;s<=a;s++)
    {
        cin>>d;
        for(f=1;f<=d;f++)
        {
            cin>>ar[f];
            ap[f]=ar[f];
        }
        for(f=1;f<=d;f++)
        {
            cin>>pr[f];
            pp[f]=pr[f];
        }
        sort(ar+1,ar+d+1);
        sort(pr+1,pr+d+1);
        reverse(pr+1,pr+d+1);
        sort(ap+1,ap+d+1);
        sort(pp+1,pp+d+1);
        reverse(ap+1,ap+d+1);
        g=checkwar(d);
        h=checkdec(d);
        printf("Case #%d: %d %d\n",s,h,d-g);
    }
}
