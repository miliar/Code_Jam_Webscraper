#include<iostream>
#include<fstream>
#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
int main(){
	fstream i;
	i.open("gcjk.txt",ios::in|ios::out|ios::app);
	fstream o;
	o.open("aou.txt",ios::in|ios::out|ios::trunc);
	lli whichcase=0;
	lli t;
	i>>t;
	cout<<t<<endl;
	while(t--){
		lli num;
		i>>num;
	
		lli ic;ic=1;
		//lli counter=0;
		if(num==0){
			o<<"Case #"<<++whichcase<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		else {
			//cout<<"jdbxwjkbc"<<endl;
			//cout<<num;
			lli flag=0;
			lli ch=0;
			lli a[10];
			for(ch=0;ch<10;ch++){
				a[ch]=0;
			}
			lli m;
			while(flag!=1){
				lli k;
				k=ic*num;
				m=k;
				cout<<" "<<m<<" ";
				lli f=ic;
				while(k){
					lli fact=k%10;
					a[fact]++;
					cout<<a[fact];
					k/=10;
				}
				lli counter=1;
				for(ch=0;ch<10;ch++){
					if(a[ch]>0){
						continue;
					}
					else {
						ic++;break;
					}
				}
				//cout<<endl;

				
				if(f==ic){
					flag=1;
				}
			}
			o<<"Case #"<<++whichcase<<": "<<m<<endl;
			cout<<endl;
		}
	}
	i.close();
	o.close();
}










