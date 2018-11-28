#include<iostream>
#include<stdio.h>
#include<sstream>
#include<math.h>
using namespace std;
bool pal(int a);
bool sqr(int a);
int main()
{
    int t,c=0;
    char A[10],B[10];
    int X,Y;
    int a[1001]={0},i,j;
    cin>>t;
    for(int T=1;T<=t;T++)
    {
     c=0;
     cin>>A>>B;
     i=0;j=0;
     while(A[i]=='0')i++; while(A[i]) A[j++]=A[i++]; A[j]='\0';
     i=0;j=0;
     while(B[i]=='0')i++; while(B[i]) B[j++]=B[i++]; B[j]='\0';
     X = atoi (A);Y = atoi(B);
     
     for(i=X;i<=Y;i++) if(a[i]) c++;
                       else {
                             if(pal(i) && sqr(i)){
                                                  c++;
                                                  a[i]=1;
                                                  }
                            }
     
     cout<<"Case #"<<T<<": "<<c<<"\n";
    }
    return 0;
}
bool pal(int a)
{
     string s;
     stringstream convert; 
     convert << a;
     s = convert.str();
     int l=s.length();
     if(l==1) return true;
     
     for(int i=0;i<l/2;i++)
     if(s[i]==s[l-1-i]);
     else return false;
     return true;
}
bool sqr(int a)
{
    int root = sqrt(a);
    if(a == (root*root)) return pal(root);
}

