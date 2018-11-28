#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<cstring>
#include<iostream>

#define loop(i,N) for(i=0;i<N;i++)
#define loop1(i,N) for(i=1;i<N;i++)
#define loop2(i,x,N) for(i=x;i<N;i++)

#define revloop(i,N) for(i=N;i>0;i--)
#define revloop2(i,x,N) for(i=x;i>N;i--)

#define s(n) scanf("%d",&n)
#define s2(n,k) scanf("%d %d",&n,&k)
#define p(n) printf("%d\n",n)
#define p2(n,k) printf("%d %d\n",n,k)

#define sl(n) scanf("%ld",&n)
#define sl2(n,k) scanf("%ld %ld" ,&n,&k)

#define pl(n) printf("%ld\n",n)
#define pl2(n,k) printf("%ld %ld\n",n,k)


#define sll(n) scanf("%lld",&n)
#define sll2(n,k) scanf("%lld %lld" ,&n,&k)

#define pll(n) printf("%lld\n",n)
#define pll2(n,k) printf("%lld %lld\n",n,k)


//#define sll(n) n=fastInput()

#define sc(n) scanf("%c",&n)

//#define ss(n) scanf("%s",n)

#define sf(n) scanf("%f",&n)

#define pb(n) push_back(n)



#define MOD 1000000007

#define MAX7 10000000
#define MAX6 1000000
#define MAX5 100000
#define MAX4 10000
#define MAX3 1000

typedef unsigned long long int ulli;
typedef signed long long int slli;
typedef unsigned long int uli;
typedef signed long int sli;

using namespace std;

inline ulli fastInput() {
    ulli val = 0;
    char c = getchar_unlocked();
    while (c<33) c = getchar_unlocked();
    while (c>33) val = (val<<1) + (val<<3) + (c-'0'), c = getchar_unlocked();
    return val;
}
int N,K,i,j,k,l;
int ar[MAX6];

string str;
vector<char> fin;


void main2()
{
fin.clear();
cin>>str;

//cout<<str;
char ch;
fin.push_back(str[0]);
loop1(i,str.length())
{
if(str[i]>=fin[0])
fin.insert(fin.begin()+0,str[i]);
else fin.push_back(str[i]);

}
loop(i,fin.size())
cout<<fin[i];

cout<<endl;
}
int T,test;


int main()
{
s(T);
char g;
sc(g);
loop1(test,T+1)
{
printf("Case #%d: ",test);
main2();
}

return 0;
}

