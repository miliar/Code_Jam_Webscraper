#include <bits/stdc++.h>
#include <fstream>
#include <cmath>

using namespace std;
ofstream out;
ifstream inp;


void openFile(){
	inp.open("D-small-attempt0.in");
  	out.open("D-small-attempt0.ou");
//	inp.open("D-large.in");
//  	out.open("D-large.ou");
}
void closeFile(){
  inp.close();
  out.close();
}
void mainWork(){
	int T,test;
	int k,c,s;
	int n,m;
	int a[22],b[22];
	inp>>T;		
	for(int test=1;test<=T;test++){
		out<<"Case #"<<test<<": ";
		inp>>k>>c>>s;
		//init
		for(int i=0;i<22;i++)a[i]=0;
		for(int i=0;i<22;i++)b[i]=0;
		
		//tinh a=k^(c-1)+k^(c-2)+...
		m=1;b[1]=1;
		n=0;
		for(int i=1;i<=c-1;i++){
			for(int j=1;j<=m;j++)b[j]=b[j]*k;
			for(int j=1;j<=m;j++){
				if(b[j]>=10){
					b[j+1]+=b[j]/10;
					b[j]%=10;
				}
			}
			while (b[m+1]>0){
				m++;
				b[m+1]=b[m]/10;
				b[m]%=10;
			}
			//tinh xong b=k^i
			//cong vao b
			n= (m>n?m:n);
			for(int i=1;i<=n;i++){
				a[i]+=b[i];
				if(a[i]>=10){
					a[i+1]=a[i]/10;
					a[i]%=10;
				}	
			}
			while(a[n+1]>0){
				n++;
				a[n+1]=a[n]/10;
				a[n]%=10;
			}
		}
//		cout<<k<<";"<<c<<";"<<endl;
//		for(int i=n;i>=1;i--)cout<<a[i];
//		cout<<endl;
		//xuat ra chon vi tri thu i
		for(int tt=0;tt<s;tt++){
			if(tt==0){
				out<<1<<" ";
				continue;
			}
			//tinh b=a*tt+(tt+1)
			for(int i=0;i<22;i++)b[i]=0;
			b[1]=tt+1;
			for(int i=1;i<=n;i++){
				b[i]+=a[i]*tt;
				if(b[i]>=10){
					b[i+1]+=b[i]/10;
					b[i]%=10;
				}
			}
			int m=n;
			while (b[m+1]>0){
				m++;
				b[m+1]=b[m]/10;
				b[m]%=10;
			}
			for(int i=m;i>0;i--)out<<b[i];
			out<<" ";
		}
		out<<endl;
		
	}
}

int main(){
	openFile();
	mainWork();
	closeFile();
	return 0;
}

