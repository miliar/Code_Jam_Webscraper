#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int n,t,m,tmp,xx,cc,x;
bool c[10];
int a[100],b[100];
ofstream out;
ifstream inp;

void openFile(){
  inp.open("A-large.in");
  out.open("A-large.ou");
}
void closeFile(){
  inp.close();
  out.close();
}
int main(){
	openFile();
	inp>>t;
	for(int test=0;test<t;test++){
		out<<"Case #"<<test+1<<": ";
		
		for(int i=0;i<10;i++)c[i]=false;
		
		inp>>xx;
		
		if(xx==0){
			out<<"INSOMNIA\n";
			continue;
		}
		
		n=0;
		while (xx>0){
			n++;
			a[n]=xx%10;
			xx/=10;
		}
		cc=10;
		x=1;
		while (cc>0){
			//nhan a voi x
			for(int i=0;i<100;i++)b[i]=0;
			for(int i=1;i<=n;i++){
				b[i]+=a[i]*x;
				if(b[i]>=10) {
					b[i+1]+=b[i]/10;
					b[i]%=10;
				}
			}
			m=n;
			while(b[m+1]>0){
				m++;
				b[m+1]+=b[m]/10;
				b[m]%=10;
			}
			
			for(int i=1;i<=m;i++)
			if(! c[b[i]] ){
				c[b[i]]=true;
				cc--;
			}
			x++;
		}
		for(int i=m;i>=1;i--)out<<b[i];
		out<<endl;	
	}
	closeFile();
	return 0;
}

