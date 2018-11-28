/*
By Tianyi Chen. All rights reserved.
Date: 2016-04-09
*/
#include<bits/stdc++.h>
# 1 "/working/1460201571.cpp"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 1 "<command-line>" 2
# 1 "/working/1460201571.cpp"
# 30 "/working/1460201571.cpp"
using namespace std;int __;long long k,c,s,t;int main() {
infile("D:/publish/GCJ/2016-Qualification/D.in"); outfile("D:/publish/GCJ/2016-Qualification/D.out"); scanf("%d",&__);for(int _=1;_<=__;++_) {
printf("Case #%d:",_);  cin>>k>>c>>s;  t=1;  while (--c)t*=k;  for(int i=0;i<k;++i)printf(" %lld",i*t+1);  putchar('\n');; }
}