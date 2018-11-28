#include <iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<fstream>
using namespace std;
#define gc getchar_unlocked
#define pc putchar_unlocked

//inline void sprint( long long a)
//{
// int i=0;
//char S[20];
//while(a>0)
//{
//    S[i++]=a%10+'0';
//a=a/10;
//}
//--i;
//while(i>=0)
//pc(S[i--]);
//printf(" ");
//}
//inline void lprint( long long a)
//{
// int i=0;
//char S[20];
//while(a>0)
//{
//    S[i++]=a%10+'0';
//a=a/10;
//}
//--i;
//while(i>=0)
//pc(S[i--]);
//pc('\n');
////}
////inline long long uscan()
////{
//    unsigned long long n=0,c=gc();
//while(c<'0'||c>'9')
//c=gc();
//while(c<='9'&&c>='0'){
//n=n*10+c-'0';
//c=gc();}
//return n;
//}
 
int main() {
	ofstream fout("output11.txt");
	ifstream fin("input.txt");
	
long long i,t,n,a[10],j,z,temp,flag;
fin>>t;j=1;
while(j<=t){
    fin>>n;
    flag=0;z=1;
    for(i=0;i<10;i++)a[i]=0;
    fout<<"Case #"<<j<<": ";
    if(n==0){
        fout<<"INSOMNIA";
        
    }
    else {
    while(flag!=1){
        temp=n*z;z++;
        while(temp!=0){
            a[temp%10]=1;
            temp/=10;
        }
        for(i=0;i<10;i++)if(a[i]==0)break;
        if(i==10)flag=1;
    }
    fout<<n*(z-1);
}fout<<endl;j++;
}
// your code goes here
	return 0;
}

