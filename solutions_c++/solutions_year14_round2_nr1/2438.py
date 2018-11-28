#include <stdio.h>
#include <string.h>
#include <stack>
#include <deque>
#include <stdlib.h>
#include <math.h>
#include <queue>
#include <limits.h>
#include <time.h>
#include <utility>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <list>
#include <iostream>
using namespace std;
#define rookloop() for(int li=0;li<4;li++)
#define knightloop() for(int li=0;li<8;li++)
#define kingloop() for(int li=0;li<8;li++)
//int dx[]={1,-1,0,0},dy[]={0,0,1,-1}; // for left right up down move
//int dx[]={1,1,1,-1,-1,-1,0,0},dy[]={0,1,-1,0,1,-1,1,-1}; // for king move
//int dx[]={1,1,-1,-1,-2,-2,2,2},dy[]={2,-2,-2,2,1,-1,1,-1}; // for knight move
#define scI(a) scanf("%d",&a)
#define scL(a) scanf("%lld",&a)
#define scD(a) scanf("%lf",&a)
typedef long long L;
typedef unsigned long long uL;
//this function is for Prime Numbers.R__PrimeList vector contains prime numbes upto R__MaximumForPrime.R__PrimeDetectArr is used
//for a number is prime or not.if a number is prime than R__PrimeDetectArr array contains in that position 'P'.
/*int R__MaximumForPrime=2000000;char R__PrimeDetectArr[100000000+1];vector <int> R__PrimeList;
void R__Sieve(){R__PrimeDetectArr[2]='P';R__PrimeList.push_back(2);for(L r_ip01=3;r_ip01<=R__MaximumForPrime;r_ip01=r_ip01+2){if(R__PrimeDetectArr[r_ip01]==0){R__PrimeDetectArr[r_ip01]='P';R__PrimeList.push_back(r_ip01);for(L r_jp01=r_ip01*r_ip01;r_jp01<=R__MaximumForPrime;r_jp01=r_jp01+r_ip01) R__PrimeDetectArr[r_jp01]='1';}}}*/
//Euler Toitent Phi Function; suppose A=12;how many number 1 to A that gcd(A,number)=1;the answer give us R__Phi
//for the function must call R__Sieve();then call R__Euler_Toitent_Phi1();
/*vector <int> R__Phi;
void R__Euler_Toitent_Phi1(){for(int r_ip01=0;r_ip01<=R__MaximumForPrime;r_ip01++) R__Phi.push_back(r_ip01);R__Phi[1]=1;for(int r_ip01=0;r_ip01<R__PrimeList.size();r_ip01++){for(int r_jp01=R__PrimeList[r_ip01];r_jp01<=R__MaximumForPrime;r_jp01=r_jp01+R__PrimeList[r_ip01])R__Phi[r_jp01]=R__Phi[r_jp01]-R__Phi[r_jp01]/R__PrimeList[r_ip01];}}*/
//Extend Euclid - ax+by=gcd(a,b)=d;parameter pass a,b,d,x,y;so you get result in x,y,d variable;
void R__Extend_Euclid(L a,L b,L &d,L &x,L &y){if(!b) {x=1,y=0,d=a;}else R__Extend_Euclid(b,a%b,d,y,x),y-=(a/b)*x;}
template <class R> string R__MonthName(R name){string mon[15];mon[1]="January";mon[2]="February";mon[3]="March";mon[4]="April";mon[5]="May";mon[6]="June";mon[7]="July";mon[8]="August";mon[9]="September";mon[10]="October";mon[11]="November";mon[12]="December";return mon[name];}
template <class R> R R__MonthDay(R num){R month[13];month[1]=31;month[2]=28;month[3]=31;month[4]=30;month[5]=31;month[6]=30;month[7]=31;month[8]=31;month[9]=30;month[10]=31;month[11]=30;month[12]=31;return month[num];}
template <class R> R R__GCD(R a,R b){if(a==0&&b==0) return 0;if(a==0) return 1;if(b==0) return a;else return R__GCD(b,a%b);}
template <class R> R R__LCM(R a,R b){return (a*b)/R__GCD(a,b);}
template <class R> R R__POW( R a, R b){if(b==0) return 1; R x=a;for(R i=2;i<=b;i++) a=a*x;return a;}
template <class R> R R__Josephus(R n,R k){R ans=1;for(R i=2;i<=n;i++)ans=(ans+k-1)%i+1;return ans;}
template <class R> R R__BigMod(R a,R b,R c){if(a==0) return 0;if(b==0) return 1;if(b%2==0){R x=R__BigMod(a,b/2,c)%c;return (x*x)%c;}else return  ((a%c)*R__BigMod(a,b-1,c)%c)%c;}
template <class R> R R__Factorial(R a){R b=1;for(R i=1;i<=a;i++)b=b*i;return b;}
template <class R> R R__BinarySearch(R a[],R l,R h,R n){while(l<=h){R m=(l+h)/2;if(n<a[m])h=m-1;else if(n>a[m])l=m+1;else return m;} return -1;}
//In R__InverseMod two arguments a and b must be coprime
template <class R> R R__InverseMod(R a,R b){if(b==1) return 1;R b0=b,x0=0,x1=1;while(a>1){R temp = x0;x0=x1-(a/b)*x0;x1=temp;temp=b;b=a%b;a=temp;}if(x1<0) x1=x1+b0;return x1;}
template <class R> R R__Euler_Toitent_Phi2(R a){R result = a;for(R i=2;i*i<=a;i++){if(a%i==0) result=result-result/i;while(a%i==0) a=a/i;}if(a>1) result=result-result/a;return result;}
int main()
{
    //time_t t1=clock();
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test;
    cin>>test;
    for(int cas=1;cas<=test;cas++)
    {
        int N;
        cin>>N;
        string x,y;
        cin>>x>>y;
        int i = 0 , j=0 , cnt=0;
        bool d = true;
        while(1)
        {
            int l = 0 ;
            char a = x[i];
            while(i<x.size()&&a==x[i]) i++ , l++ ;
            int h = 0;
            while(j<y.size()&&a==y[j]) j++ , h++;
            if(h==0)
            {
                d=false;break;
            }
            else
            {
                int f = fabs(l-h);
                cnt=cnt+f;
            }
            if(i==x.size()&&j==y.size()) break;
        }
        cout<<"Case #"<<cas<<": ";
        if(d==false) cout<<"Fegla Won\n";else cout<<cnt<<"\n";
    }
    //time_t t2=clock();
    //cout<<(t2-t1);
    return 0;
}
