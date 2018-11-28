#include<iostream>
#include<stdio.h>


using namespace std;

typedef long int li;

int main(){
	freopen("A-small-attempt1(1).in","r",stdin);
	freopen("A-small-attempt1(1).out","w",stdout);
	/*freopen("A-small-attempt0(1).in","r",stdin);
	freopen("A-small-attempt0(1).out","w",stdout);d*/
	/*freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);*/
	li r, t , n,i,area=0,t1=0, count =0,r1=0;
	scanf("%ld",&n);
	i=1;
	while(i<=n){
		scanf("%ld%ld",&r,&t);
		count =0;
		t1 = t;
		r1 = r+1;
		/*area = r*r;
		t1 -= area;
		if(t1>=0)
			count = 1;*/
		while(t1>=0){
		
			area = r1*r1 - r*r;
			t1 -= area;
			if(t1>=0)
				count++;
			r += 2;
			r1 += 2;
		}
		printf("Case #%ld: %ld",i,count);
		if(i!=n)
			cout<<endl;
		++i;
	}
	
	return 0;
}
