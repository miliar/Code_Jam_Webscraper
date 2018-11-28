#include <bits/stdc++.h>
#include <iostream>
#include <conio.h>

using namespace std;

bool s0=false, s1=false, s2=false, s3=false, s4=false, s5=false, s6=false, s7=false, s8=false, s9=false;

void lNum(long int);

void lNum(long int n){
int tmp;
while(n!=0){
	tmp = n%10;
	n /= 10;
	if(tmp==0) s0=true;
	if(tmp==1) s1=true;
	if(tmp==2) s2=true;
	if(tmp==3) s3=true;
	if(tmp==4) s4=true;
	if(tmp==5) s5=true;
	if(tmp==6) s6=true;
	if(tmp==7) s7=true;
	if(tmp==8) s8=true;
	if(tmp==9) s9=true;
}
return;
}

int main(){
FILE *out;
out = fopen("A.out", "a");
int t;
cin>>t;
for(int aa=1;aa<=t;aa++){
	cout<<"Case #"<<aa<<": ";
	fprintf(out, "Case #%d: ", aa);
	bool ans=false;
	long int n;
	long long unsigned int i=1, tmp;
	cin>>n;
	while(i<=5000000){
		tmp = n*i;
		lNum(tmp);
		if(s0==true && s1==true && s2==true && s3==true && s4==true && s5==true && s6==true && s7==true && s8==true && s9==true){
			cout<<tmp<<endl;
			fprintf(out, "%d\n", tmp);
			ans = true;
			break;
		}
		i++;
	}
	if(ans==false){
		cout<<"INSOMNIA"<<endl;
		fprintf(out, "INSOMNIA\n");
	}
	s0=false;
	s1=false;
	s2=false;
	s3=false;
	s4=false;
	s5=false;
	s6=false;
	s7=false;
	s8=false;
	s9=false;
}
getch(); //comment this line out after algorithm is fully functional and working....
return 0;
}
