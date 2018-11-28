#include<iostream>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
#include<limits.h>
using namespace std;

/*printing definitions*/
#define pi(x) printf("%d\n",(x))
#define pii(x,y) printf("%d %d\n",(x),(y))
#define pl(x) printf("%lld\n",(x))
#define pll(x,y) printf("%lld %lld\n",(x),(y))
#define pil(x,y) printf("%d %lld\n",(x),(y))
#define pli(x,y) printf("%lld %d\n",(x),(y))
#define plf(x) printf("%lf\n",(x))
#define plflf(x,y) printf("%lf %lf\n",(x),(y))

/*scanning definitions*/
#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define sil(x,y) scanf("%d %lld",&x,&y)
#define sli(x,y) scanf("%lld %d",&x,&y)
#define slf(x) scanf("%lf",&x)
#define slflf(x,y) scanf("%lf %lf",&x,&y)

//  CREATED BY: ATUL SEHGAL
string answer[4][4][4]={
                            //x=1
                            {
                                {"GABRIEL","GABRIEL","GABRIEL","GABRIEL"},
                                {"GABRIEL","GABRIEL","GABRIEL","GABRIEL"},
                                {"GABRIEL","GABRIEL","GABRIEL","GABRIEL"},
                                {"GABRIEL","GABRIEL","GABRIEL","GABRIEL"},
                            },
                            //x=2
                            {
                                {"RICHARD","GABRIEL","RICHARD","GABRIEL"},
                                {"GABRIEL","GABRIEL","GABRIEL","GABRIEL"},
                                {"RICHARD","GABRIEL","RICHARD","GABRIEL"},
                                {"GABRIEL","GABRIEL","GABRIEL","GABRIEL"},
                            },
                            //x=3
                            {
                                {"RICHARD","RICHARD","RICHARD","RICHARD"},
                                {"RICHARD","RICHARD","GABRIEL","RICHARD"},
                                {"RICHARD","GABRIEL","GABRIEL","GABRIEL"},
                                {"RICHARD","RICHARD","GABRIEL","RICHARD"},
                            },
                            //x=4
                            {
                                {"RICHARD","RICHARD","RICHARD","RICHARD"},
                                {"RICHARD","RICHARD","RICHARD","RICHARD"},
                                {"RICHARD","RICHARD","RICHARD","GABRIEL"},
                                {"RICHARD","RICHARD","GABRIEL","GABRIEL"},
                            }};
int main()
{
    freopen("input-Dsmall.txt","r",stdin);
    freopen("output-Dsmall.txt","w",stdout);
 	int t,i,j,n,ans,r,c,x,T=1;
	si(t);
	while(t--)
	{
	    ans=0;
		si(x),sii(r,c);
        printf("Case #%d: ",T++);
		cout<<answer[x-1][r-1][c-1]<<endl;
	}
	return 0;
}
