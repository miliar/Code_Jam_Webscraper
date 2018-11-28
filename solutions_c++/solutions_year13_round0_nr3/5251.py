/*
# Author:      pikkupr
# Problem:     Problem C. Fair and Square
*/
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;


inline int chk_if_pallin(unsigned long int num){
		unsigned long int n = num,size=0;
		while(n){
			n=n/10;
			size++;
		}
		size = size-1;
		//cout<<size;
		char s[size],strng_rev[size];
		sprintf(s,"%d",num);
		sprintf(strng_rev,"%d",num);
		strrev(strng_rev);
		//printf("%s",strng_rev);
		if(!strcmp(strng_rev,s)){
			//printf("\n%s",strng_rev);
			return 1;
		}
		return 0;

}

inline int chk_if_squ(unsigned long int num){
	unsigned long int n = sqrt(num);
	if(n*n == num){
        if(chk_if_pallin(n)==1)
            return 1;
	}
	return 0;

}
int main(){
    //unsigned long int x = 1111111111;
	//cout<<chk_if_pallin(100);
	//cout<<chk_if_squ(11);*/
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
    int n,t=1, a, b,cnt = 0;
    cin>>n;
    while(t<=n){
        cnt = 0;
        cin>>a>>b;
        for(int i = a;i<=b;i++){
            if(chk_if_pallin(i)==1)
                if(chk_if_squ(i)==1){
                    //cout<<"\n"<<i;
                    cnt++;
                }
        }
        printf("Case #%d: %d",t,cnt);
        if(t!=n)
            cout<<"\n";
        t++;
    }

	return 0;
}
