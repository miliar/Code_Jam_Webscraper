#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;
bool is(int num){
	int r,sum=0,temp;
	temp=num;
while(temp){
             r=temp%10;
             temp=temp/10;
             sum=sum*10+r;
         }
         if(num==sum) return true;
		 return false;
}
int PerfectSquare(int n)
{
    int h = n & 0xF; // last hexidecimal "digit"
    if (h > 9)
        return 0; // return immediately in 6 cases out of 16.

    // Take advantage of Boolean short-circuit evaluation
    if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
    {
        // take square root if you must
        int t = (int) floor( sqrt((double) n) + 0.5 );
            if(t*t == n)
				return is(t);
    }
    return 0;
}
int values[1000];
int main(){
	int n,c,a,b;
	freopen("1.in", "r", stdin), freopen("1.out", "w", stdout);
	scanf("%i",&n);
	for(int i=0;i<n;i++)
	{
		c=0;
		scanf("%i %i",&a,&b);
		for(int j=a;j<=b;j++){
			if(values[j]==7){
				c++;
				continue;
			}
			if(PerfectSquare(j) && is(j)){
				values[j]=7,c++;
			}
		}
		printf("Case #%i: %i\n",i+1,c);
	}
}