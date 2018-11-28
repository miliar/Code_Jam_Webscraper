#include<iostream>
using namespace std;
#include<algorithm>
int main(){
int t;
cin>>t;
for(int i=1;i<=t;++i){
	string s;
	cin>>s;
	cout<<"Case #"<<i<<": ";
	int j=0, l=s.size(), a[26]={0}, b[700]={0};
	while(j<l) a[(int)s[j++]-65]++;
	j=0;
	while(a[23]) {a[18]--; a[8]--; a[23]--; b[j++]=6;}
	while(a[25]) {a[25]--; a[4]--; a[17]--; a[14]--; b[j++]=0;}
	while(a[22]) {a[19]--; a[22]--;a[14]--; b[j++]=2;}
	while(a[20]) {a[5]--; a[20]--; a[17]--; a[14]--; b[j++]=4;}
	while(a[14]) {a[14]--; a[4]--; a[13]--; b[j++]=1;}	
		while(a[18]) {a[18]--; a[4]-=2; a[21]--; a[13]--; b[j++]=7;}
		while(a[6]) {a[8]--; a[4]--; a[7]--; a[6]--; a[19]--; b[j++]=8;}
	while(a[17]) {a[19]--; a[7]--; a[17]--; a[4]-=2; b[j++]=3;}

	while(a[5]) {a[5]--; a[4]--; a[8]--; a[21]--; b[j++]=5;}	
	while(a[13]>=2 && a[4] && a[8]) {a[13]-=2; a[4]--; a[8]--; b[j++]=9;}
	sort(b, b+j);
	for(int i=0;i<j;++i) cout<<b[i];
	cout<<endl; 
}
return 0;	
}
