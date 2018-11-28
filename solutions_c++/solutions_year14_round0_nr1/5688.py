//
// main.cpp
// GJ qualification 1
//
// Created by zhangchi on 14-4-12.
// Copyright (c) 2014Äê ZhangChi. All rights reserved.
//

#include <iostream>
#include <cstdio>

int s[6][6];
int a1[6],a2[6];

void input(int t,int k)
{
for(int i=1;i<5;i++)
{
for(int j=1;j<5;j++)
{
scanf("%d",&s[i][j]);
}
}
if (k==1) {
for (int i=0; i<4; i++) {
a1[i]=s[t][i+1];
}
}
else if(k==2)
{
for (int i=0; i<4; i++) {
a2[i]=s[t][i+1];
}
}
}

void solve()
{
int flag=0,i,t;
for (i=0; i<4; i++) {
for (int j=0; j<4; j++) {
if (a1[i]==a2[j]) {
flag++;
t=i;
}
}
}

if (flag==0) {
printf("Volunteer cheated!\n");
}
else if(flag==1)
{
printf("%d\n",a1[t]);
}
else{
printf("Bad magician!\n");
}
}

int main(int argc, const char * argv[])
{
int T;
int x1,x2;

scanf("%d",&T);
for (int now=1; now<=T; now++) {
memset(s, 0, sizeof(s));
memset(a1, 0, sizeof(a1));
memset(a2, 0, sizeof(a2));

scanf("%d",&x1);
input(x1,1);
memset(s,0,sizeof(s));
scanf("%d",&x2);
input(x2,2);

printf("Case #%d: ",now);
solve();
}
}