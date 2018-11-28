#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<vector>
#include<map>
#include<algorithm>
#include<limits.h>
#include<set>
#include<math.h>
 
using namespace std;
#define lli long long int
#define ulli unsigned long long int
#define in(t) scanf("%d",&t)
#define inlf(t) scanf("%lf",&t)
#define inl(t) scanf("%ld",&t)
#define inll(t) scanf("%lld",&t)
#define inlu(t) scanf("%llu",&t)
#define MOD 1000000007

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    #endif
    
    int t,n,i,ans,cases,f,c,d,g,h;
    in(t);
    for(cases=1;cases<=t;cases++)
    {
    ans=f=c=d=g=h=0;
    in(n);
    string s1,s2,s3="",s4="";
    int l1,l2,freq1[150]={0},freq2[150]={0},size1[150]={0},size2[150]={0},l3,l4;
    cin>>s1>>s2;
    l1=s1.length();
    l2=s2.length();
    
    for(i=0;i<l1-1;i++)
    {
    if(s1[i]==s1[i+1])
    size1[(int)(s1[i])]++;
    else
    {
    size1[(int)(s1[i])]++;
    freq1[c++]=size1[(int)(s1[i])];
    size1[(int)(s1[i])]=0;
    }
    }
    size1[(int)(s1[l1-1])]++;
    freq1[c++]=size1[(int)(s1[l1-1])];
    for(i=0;i<l2-1;i++)
    {
    if(s2[i]==s2[i+1])
    size2[(int)(s2[i])]++;
    else
    {
    size2[(int)(s2[i])]++;
    freq2[d++]=size2[(int)(s2[i])];
    size2[(int)(s2[i])]=0;
    }
    }
    size2[(int)(s2[l2-1])]++;
    freq2[d++]=size2[(int)(s2[l2-1])];
    
    for(i=0;i<l1-1;i++)
    {
    if(s1[i]!=s1[i+1])
    s3+=s1[i];
    }
    s3+=s1[l1-1];
    
    
    for(i=0;i<l2-1;i++)
    {
    if(s2[i]!=s2[i+1])
    s4+=s2[i];
    }
    s4+=s2[l2-1];
    
    //cout<<s3<<" "<<s4<<"\n";
    
    l3=s3.length();
    l4=s4.length();
    
    if(s3==s4)
    {
    for(i=0;i<l3;i++)
    {
    if(freq1[i]>freq2[i])
    {
    ans=ans+(freq1[i]-freq2[i]);
    }
    
    else
    {
    ans=ans+(freq2[i]-freq1[i]);
    }
    }
    printf("Case #%d: %d\n",cases,ans);
    }
    
    else
    printf("Case #%d: Fegla Won\n",cases);
    
    }
    return 0;
}
    
    
