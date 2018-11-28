#include <iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
#define loop(i,N) for(i=0;i<N;i++)
#define loop1(i,N) for(i=1;i<N;i++)
//#define loop(i,x,N) for(i=x;i<N;i++)

#define s(n) ob>>n
#define p(n) printf("%d",n)

#define sl(n) scanf("%ld",&n)
#define pl(n) printf("%ld",n)


#define sll(n) scanf("%lld",&n)
#define pll(n) printf("%lld",n)

#define sc(n) ob>>n

#define ss(n) scanf("%s",n)

#define sf(n) scanf("%f",&n)

int ans,S,i,k,j,T,X,stand,l=0;
char c;
string line;
int main()
{
fstream ob,ob2;
ob.open("input.txt");
ob2.open("output.txt");
s(T);

while(T--)
{ob2<<"Case #"<<++l<<": ";
s(S);
ob>>line;
//sc(c);
i=0;
stand=0;

ans=0;
//sc(c);
//cout<<c;
c=line[i];
while(i<S)
{++i;
    if((c=='0')&&(stand<i))
    {ans++;stand++;}


        else stand+=(c-48);

    //i++;
c=line[i];
//cout<<c;
}

ob2<<ans<<endl;

}
return 0;
}
