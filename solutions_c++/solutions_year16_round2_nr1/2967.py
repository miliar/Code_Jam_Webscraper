#include<iostream>
#include <fstream>

using namespace std;

int main(){
string s;
ifstream myfile ("A-large.in");
ofstream myf ("output.txt");
int t,len,cnt,cnt2,cnt3;
myfile >> t;
int a[10];
for(int i=1;i<t+1;i++){
	for(int j=0;j<10;j++)
		a[j]=0;
	cnt=0;cnt2=0,cnt3=0;
	myfile>>s;
	len = s.size();
	for(int j=0;j<len;j++){
		if(s[j]=='Z')
			a[0]++;
		if(s[j]=='W')
			a[2]++;
		if(s[j]=='U')
			a[4]++;
		if(s[j]=='X')
			a[6]++;
		if(s[j]=='G')
			a[8]++;
		}
	for(int j=0;j<len;j++){
		if(s[j]=='O'){
			cnt++;
			if(a[0]+a[2]+a[4] <cnt)
				a[1]++; }
		if(s[j]=='F'){
			cnt2++;
			if(a[4]<cnt2)
				a[5]++; }
		if(s[j]=='R'){
			cnt3++;
			if(a[0]+a[4] <cnt3)
				a[3]++; 
				}
		}
	cnt=0;
	for(int j=0;j<len;j++){
		if(s[j]=='V'){
			cnt++;
			if(a[5]<cnt)
				a[7]++; }
		}
	cnt2 = len - (a[0]*4+a[1]*3+a[2]*3+a[3]*5+a[4]*4+a[5]*4+a[6]*3+a[7]*5+a[8]*5);
	if(cnt2>0){
		cnt = cnt2/4;
		a[9]=cnt; }
	
	myf<<"Case #"<<i<<": ";
	for(int j=0;j<10;j++){
		while(a[j]>0){
			myf<<j; 
			a[j]--; }
		}
	myf<<"\n";
	}
	myfile.close();
	myf.close();
	return 0;
} 
			
	
			 
