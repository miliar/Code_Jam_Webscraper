#include<bits/stdc++.h>
using namespace std;
long long int ar[11];
string finds(long long int a,long long int n){
	//cout<<"1";
	string s="";
	while(a>0){
		int t= a%2;
		string tmp ="0";
		tmp[0]=tmp[0]+t;
		s=tmp +s;
		a=a/2;
		
	}
	if(s.length() < n-2){
		string ss="";
		for(int i=0;i<n-2-s.length();i++) ss="0"+ss;
		s = ss+s;
	}
	//cout<<"2";
	return s;
}
long long int notprime(long long int num){
	//cout<<"3";
	long long int i;
	int inc=1, start=2;
	if(num%2==1) {
		inc =2;
		start=3;
	}
	for(i=start;i<=num/2;i=i+inc){
		if(num%i==0){
		//	cout<<"4";
			return i;
		}
	}
	//cout<<"4";
	return 0;
}
long long int notprime2(long long int n){
	if (n==2)
        return 0;
    if(n==3)
        return 0;
    if (n % 2 == 0)
        return 2;
    if (n % 3 == 0)
        return 3;

    long long int i = 5, w = 2;

    while (i * i <= n){
        if (n % i == 0)
            return i;

        i += w;
        w = 6 - w;
    	
	}

    return 0;
}
int findp(string s){
	//cout<<"5";
	long long int j,num;
	//cout<<s;
	for(int i=2;i<=10;i++){
		j=0,num=0;
		for(int k=s.length()-1;k>=0;k--){
			if(s[k]=='1'){
				num += pow(i,j);
			}
			j++;
		}
		long long int cc = notprime2(num);
		if(cc==0){
			//cout<<"cc is zero for i "<<i<<"and num "<<num<<endl;
			//cout<<"6";
			return 0;
		} else ar[i]=cc;
	}
	//cout<<"6";
	return 1;
}
int main() {
	ifstream oo;
	oo.open("C-small-attempt1.in");
	ofstream mm;
	mm.open("op5.txt");
	
	int t,i,k;
	oo>>t;
	for(i=1;i<=t;i++){
		mm<<"Case #"<<i<<":\n";
		long long int n, J,val,i, maxj,j;
		oo>>n>>J;
		//val = pow(2,n-1)+1;
		maxj = pow(2,n-2);
		for(j=0;j<maxj;j++){
			string bitt="1"+finds(j,n)+"1";
			if(findp(bitt)){
				mm<<bitt<<" ";
				for(k=2;k<=10;k++) mm<<ar[k]<<" ";
				mm<<endl;
				J--;
			}
			if(J==0) break;
		}
	}
	return 0;
}
