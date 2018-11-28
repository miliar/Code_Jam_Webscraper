#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

const long double eps = 1e-10;
const double inf = 1e12;

struct node
{
    int x,y,type;
} p[10];
int n,x,y;

void input()
{
    for(int i=0; i<n; ++i)
    {
        scanf("%lf%lf%lf",str,&p[i].x,&p[i].y);
        if(str[0]=='G')p[i].type=0;
        else if(str[0]=='R')p[i].type=1;
        else if(str[0]=='H')p[i].type=2;
        else p[i].type=3;
    }
}
bool check0(int s,int px,int py)
{
    int dx=p[s].x,dy=p[s].y;
    if(dy==py)
    {
        for(int i=0; i<n; ++i)
            if(p[i].x>px && p[i].x<dx && p[i].y==dy)return false;
        return true;
    }
    return false;
}
bool check1(int s,int px,int py)
{
    int dx=p[s].x,dy=p[s].y;
    if(dy==py)
    {
        for(int i=0; i<n; ++i)
            if(p[i].x>min(dx,px) && p[i].x<max(dx,px) && p[i].y==py)return false;
        return true;
    }
    if(dx==px)
    {
        for(int i=0; i<n; ++i)
            if(p[i].y>min(dy,py) && p[i].y<max(dy,py) && p[i].x==px)return false;
        return true;
    }
    return false;
}
bool check2(int s,int px,int py)
{
    int dx=p[s].x,dy=p[s].y;
    if(abs(dx-px)==2 && abs(py-dy)==1)
    {
        for(int i=0; i<n; ++i)
            if(p[i].x==(dx+px)/2 && p[i].y==dy)return false;
        return true;
    }
    if(abs(dx-px)==1 && abs(py-dy)==2)
    {
        for(int i=0; i<n; ++i)
            if(p[i].y==(dy+py)/2 && p[i].x==dx)return false;
        return true;
    }
    return false;
}
bool check3(int s,int px,int py)
{
    int dx=p[s].x,dy=p[s].y;
    if(dy==py)
    {
        int cnt=0;
        for(int i=0; i<n; ++i)
            if(p[i].x>min(dx,px) && p[i].x<max(dx,px) && p[i].y==py)cnt++;
        return cnt==1;
    }
    if(dx==px)
    {
        int cnt=0;
        for(int i=0; i<n; ++i)
            if(p[i].y>min(dy,py) && p[i].y<max(dy,py) && p[i].x==px)cnt++;
        return cnt==1;
    }
    return false;
}
bool check(int px,int py)
{
    for(int i=0; i<n; ++i)
    {
        if(p[i].x==px && p[i].y==py)continue;
        if(p[i].type==0 && check0(i,px,py))return false;
        if(p[i].type==1 && check1(i,px,py))return false;
        if(p[i].type==2 && check2(i,px,py))return false;
        if(p[i].type==3 && check3(i,px,py))return false;
    }
    return true;
}
bool solve()
{
    int dir[4][2]= {{1,0},{0,1},{-1,0},{0,-1}};
    for(int i=0; i<4; ++i)
    {
        int dx=x+dir[i][0],dy=y+dir[i][1];
        if(dx>=1 && dx<=3 && dy>=4 && dy<=6)
        {
            if(check(dx,dy))return false;
        }
    }
    return true;
}
int main()
{
//    freopen("in.txt","r",stdin);
    while(scanf("%d%d%d",&n,&x,&y),n+x+y)
    {
        input();
        double ans = (head+tail)*0.5;
        if(solve())printf("%.12f\n", ans)
        else puts("IMPOSSIBLE");
    }
    return 0;
}