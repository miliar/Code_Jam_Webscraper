#include<iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<time.h>

using namespace std;

struct name 
 {
  string s;
  int v1;
  int v2;
  int v3;
 };

bool tmp(name A,name B)
 {
  return (A.s.size()<B.s.size() || (A.s.size() == B.s.size() && A.s<B.s));
 }

string L,R;
string mp;
string m,q;
int i,k,a[50];
vector <name> v;
vector <string> answers;
name kmp;

string reverse(string A,int l,int r)
 {
  q.erase();
  for (int o=r;o>=l;o--) q+=A[o];
  return q;
 }

void check(int a1,int a2)
 {
  m.clear();
  for (int o=1;o<=i;o++)
   m+=(char)('0'+a[o]);
  kmp.s=m;
  kmp.v1=a1;
  kmp.v2=a2;
  kmp.v3=1;
  v.push_back(kmp);
 }

void df(int now,int a1,int a2)
 {
  if (now == i+1) {check(a1,a2);return;}
  if (now == 1)
   {
    a[now]=1;
    df(now+1,a1+1,a2);
    a[now]=2;
    df(now+1,a1,a2+1);
    return;
   } else
   {
    if (a2 == 1)
     {
      a[now]=0;
      df(now+1,a1,a2);
      return ;
     }
    if (a1 == 4)
     {
      a[now]=0;
      df(now+1,a1,a2);
      return;
     }
    a[now]=0;
    df(now+1,a1,a2);
    a[now]=1;
    df(now+1,a1+1,a2);
   }
 }

int sum[300+10];
int l[300+10];
string w;

bool res(string A,string B)
 {
  if (A.size()<B.size()) return true;
  if (A.size()>B.size()) return false;
  if (A<=B) return true;
 }

int tT,pop,t,j;

string sq(string A)
 {
  int len=A.size();
  int o=0,h=0,now=0,to=0;
  for (o=1;o<=300;o++) sum[o]=0;
  for (o=0;o<len;o++)
   {
    to=A[o]-'0';
    for (h=1;h<=300;h++) l[h]=0;
    for (h=0;h<len;h++)
     l[300-len+h+1]=A[h]-'0';
    for (h=1;h<=300;h++) l[h]*=to;
    for (h=300;h>=1;h--) l[h-1]+=l[h]/10,l[h]%=10;
    for (h=150;h<=300;h++) sum[h-now]+=l[h];
    for (h=300;h>=1;h--) sum[h-1]+=sum[h]/10,sum[h]%=10;
    now++;
   }
  w.clear();
  for (o=1;o<=300;o++) if (sum[o]) break;
  for (;o<=300;o++) w+=(char)(sum[o]+'0');
  return w;
 }

bool palin(string A)
 {
  for (int o=0;o<A.size();o++)
   if (A[o] != A[A.size()-o-1]) return false;
  return true;
 }

main()
 {
  freopen("input.in","r",stdin);
  freopen("output.out","w",stdout);
  for (i=1;i<=25;i++)
   df(1,0,0);
  
  k=v.size();
  for (i=0;i<k;i++)
   {
    kmp=v[i];
    kmp.s=kmp.s+'0';
    kmp.v3=2;
    v.push_back(kmp);
    kmp.s[kmp.s.size()-1]='1';
    kmp.v1++;
    v.push_back(kmp);
    kmp.v1--;
    if (kmp.v1 < 4 && kmp.v2 < 1)
     {
      kmp.s[kmp.s.size()-1]='2';
      kmp.v2++;
      v.push_back(kmp);
     }
   }
  
  kmp.s="1";kmp.v1=1;kmp.v2=0;kmp.v3=2;v.push_back(kmp);
  kmp.s="2";kmp.v1=0;kmp.v2=2;kmp.v3=2;v.push_back(kmp);
  kmp.s="3";kmp.v1=0;kmp.v2=0;kmp.v3=2;v.push_back(kmp);
  
  for (i=0;i<v.size();i++)
   if (v[i].v3 == 1) v[i].s=v[i].s+reverse(v[i].s,0,v[i].s.size()-1); else
                     v[i].s=v[i].s+reverse(v[i].s,0,v[i].s.size()-2);
  
  sort(v.begin(),v.end(),tmp);
  for (i=0;i<v.size();i++)
   {
    mp=sq(v[i].s);
    if (palin(mp)) answers.push_back(mp);
   }
  
  cin>>tT;
  for (t=1;t<=tT;t++)
   {
    cin>>L>>R;
    pop=0;
    for (j=0;j<answers.size();j++)
     if (res(L,answers[j]) && res(answers[j],R)) pop++;
    cout<<"Case #"<<t<<": "<<pop<<endl;
   }
  
 }
