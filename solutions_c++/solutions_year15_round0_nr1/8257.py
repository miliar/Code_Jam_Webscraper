#include<iostream>
#include<fstream>
#include<sstream>
#include <new>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<ctype.h>
#include<string>
#include<iterator>
#include<bitset>
#include<unordered_map>
#include<unordered_set>
#include<map>
#include<set>
#include<utility>
#include<memory.h>
#include<cstdlib>
#define PI 2*acos(0)
#define inf 0x3f3f3f3f
#define ppb push_back
#define ppf push_front
#define ll long long
#define ull unsigned long long
#define ssi(x) scanf("%d",&x)
#define ssd(x) scanf("%lf",&x)
#define ssc(x) scanf("%c",&x)
#define sss(x) scanf("%s",&x)
#define ssii(x,y) scanf("%d %d",&x,&y)
#define ssdd(x,y) scanf("%lf %lf",&x,&y)
#define sscc(x,y) scanf("%c %c",&x,&y)
#define ssss(x,y) scanf("%s %s",&x,&y)
#define eol printf("\n")
#define feol fprintf(f,"\n")
#define ssp printf(" ")
#define ggt getchar()
#define ppt putchar('.')
using namespace std;
//main()
//{
//    int cas,ccas=1;
////    cin>>cas;
//    ll i,j,k,l;
//    ll Sm;
////    while(cas--){
//    string s;
//    cin>>Sm>>s;
//    ll pre=s[0]-'0';
//    ll sum=0;
//    for(i=1,l=Sm+1;i<l;i++)
//    {
////        if(pre>=Sm) break;
//        if(s[i]!='0')
//        if(pre<i)
//            sum+=i-pre;
//        pre+=i-pre;
//    }
//
//    printf("Case #%d: %d\n",ccas++,sum);
//
////    }
//}
//

//6
//4 00020
//4 11111
//1 09
//5 110011
//0 1
//10 01910100001

main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.txt","w",stdout);
    int cas,ccas=1;
    cin>>cas;
    ll i,j,k,l;
    ll Sm;
    while(cas--){
    string s;
    cin>>Sm>>s;
    ll pre=s[0]-'0';
    ll sum=0;
    for(i=1,l=Sm+1;i<l;i++)
    {
        if(pre>=Sm) break;
        if(pre<i && s[i]>'0'){
            sum+=i-pre;
            pre=i;
        }

        pre+=s[i]-'0';
    }

    printf("Case #%d: %d\n",ccas++,sum);

    }
}

