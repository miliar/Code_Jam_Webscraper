#include<iostream>
#include<fstream>
#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
lli indexing(lli g,lli num){
	lli i=0,sum=0,rem;
	while(g){
		rem=g%10;
		sum+=rem*(lli)pow(num,i++);
		g/=10;
	}
	return sum;
}
int isprime(lli num){
	lli i=0;
	for(i=2;i<=sqrt(num);i++){
		if(num%i==0){
			return 0;
		}
	}
	return 1;
}
lli divisor(lli num){
	lli i;
	for(i=2;i<=num/2;i++){
		if(num%i==0){
			return i;
		}
	}
	return 0;
}
int main(){
	fstream i;
	i.open("gcjk.txt",ios::in|ios::out|ios::app);
	fstream o;
	o.open("aou.txt",ios::in|ios::out|ios::trunc);
	lli whichcase=0;
	lli t;
	i>>t;
	//cout<<isprime(7);
	//cout<<divisor(6);
	//cout<<indexing(1000000000001,2);
	//cout<<t<<endl;
	o<<"Case #1: "<<endl;
	while(t--){
		lli n,j;
		i>>n>>j;
		lli fish=0,ic;
		for(ic=(lli)pow(10,n-1);ic<(lli)pow(10,n);ic++){
			//cout<<ic<<" ";
			lli flag=0,rem,g=ic;
			while(g){
				rem=g%10;
				g/=10;
				if(rem>1){
					flag=1;break;
				}
				if(flag==0){
					if(rem==1){
						flag=2;
						continue;
					}
					else {
						flag=1;
						break;
					}
				}
			
			}
			if(flag==1||rem!=1){
				continue;
			}
			lli fact;fact=0;
			if(rem==1){
				lli count=0;
				for(count=2;count<=10;count++){
						lli num;num=indexing(ic,count);
						//cout<<num<<"  ";
						if(isprime(num)) {
							fact=2;
						}
						if(fact==2) break;
				}
				if(fact==2) continue;
				fish++;
				o<<ic<<" ";
				lli il;
				for(il=2;il<=10;il++){
					o<<divisor(indexing(ic,il))<<" ";
				}
					o<<endl;
			
			}
			if(fish==j){
				break;
			}
		}	
		}
	
	i.close();
	o.close();
}








