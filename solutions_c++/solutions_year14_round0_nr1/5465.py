#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<map>
#include<cstdlib>
#include<stdio.h>
#include<set>
#include<cmath>
#include<cstring>
#include<utility>
#include<string>
#include<iomanip>
using namespace std;
void R( int &x ) {
x = 0;
char temp;
temp = getchar();
while( ! isdigit( temp ) && temp != '-' ) {
temp = getchar();
}
bool neg = 0;
if( temp == '-' ) {
neg = 1;
}
else if( isdigit( temp ) ) {
x = ( temp - '0' );
}
temp = getchar();
while( isdigit( temp ) ) {
x *= 10;
x += ( temp - '0' );
temp = getchar();
}
if( neg )
x *= - 1;
}
void R( long long &x ) {
x = 0;
char temp;
temp = getchar();
while( ! isdigit( temp ) && temp != '-' ) {
temp = getchar();
}
bool neg = 0;
if( temp == '-' ) {
neg = 1;
}
else if( isdigit( temp ) ) {
x = ( temp - '0' );
}
temp = getchar();
while( isdigit( temp ) ) {
x *= 10;
x += ( temp - '0' );
temp = getchar();
}
if( neg )
x *= - 1;
}
#define MAX 100005
 
int main(){
        freopen("in.in","r",stdin);freopen("out.out","w",stdout);
        int n,m,q;
        int t;
        int tt=1;
        R(t);
        while(t--){
                printf("Case #%d: ",tt);
                ++tt;
				int tmp;
				int a1[4],a2[4];
                R(n);
				for(int i=0;i<4;++i){
					for(int j=0;j<4;++j){
						if(i==n-1)R(a1[j]);
						else R(tmp);
					}}
				R(n);
					for(int i=0;i<4;++i){
					for(int j=0;j<4;++j){
						if(i==n-1)R(a2[j]);
						else R(tmp);
					}}
				int match=0,mc;
				for(int i=0;i<4;++i)
				for(int j=0;j<4;++j)
					if(a1[i]==a2[j])++match,mc=i;
				if(match==1)printf("%d\n",a1[mc]);
				else if(match==0)printf("Volunteer cheated!\n");
				else printf("Bad magician!\n");
		}}
