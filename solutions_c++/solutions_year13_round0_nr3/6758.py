#include<iostream>
#include<conio.h>
using namespace std;
int chksquare(long num){
	long i=1,count=0;
	while(1){
		if((num-i)==0){
			count++;
			return count;
		}
		else if((num-i)<0)
			return -1;
		else{
			count++;
			num-=i;
			i+=2;
		}
	}
}
int chkpalindrome(long num){
	long rev=0,rnum=num;
	while(num!=0){
		rev=rev*10+num%10;
		num=num/10;
	}
	if(rnum==rev)
		return 1;
	else 
		return -1;		
}
int main(){
	int test;
	long numl,numu,count;
	cin>>test;
	for(int j=1;j<=test;j++){
		count=0;
		cin>>numl>>numu;
		for(long i=numl;i<=numu;i++){
			int chkpal=chkpalindrome(i);
			if(chkpal==1){
				long chksq=chksquare(i);
				if(chksq!=-1){
					chkpal=chkpalindrome(chksq);
					if(chkpal==1)
						count++;
				}
			}
		}
		cout<<"Case #"<<j<<": "<<count<<"\n";
	}
	getch();
	return 0;
}
