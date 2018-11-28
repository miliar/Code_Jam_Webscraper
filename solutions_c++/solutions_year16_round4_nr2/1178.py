#include<fstream>
#include<string.h>
#include<algorithm>
using namespace std;

int main(){
	ifstream fin("B-small-attempt4.in");
	ofstream fout("B-small-attempt4.out");
	int tt=0;
	fin>>tt;
	int n,k;
	double p[200],pp[200];
	double ans;
	double k1[200][200];
	for(int kk=1;kk<=tt;kk++){
		fin>>n>>k;
		for(int i=0;i<n;i++){
			fin>>p[i];
		}
		ans=0;
		for(int z=0;z<pow(2,n);z++){
			int s=0;
			int tmp=z;
			while(tmp>0){
				if(tmp%2==1)s++;
				tmp/=2;
			}
			if(s==k){
				int in1=0,in2=0;
				tmp=z;
				while(tmp>0){
					if(tmp%2==1){
						pp[in1]=p[in2];
						in1++;
					}
					tmp/=2;
					in2++;
				}
				k1[0][0]=1-pp[0];
				k1[0][1]=pp[0];
				for(int i=1;i<k;i++){
					k1[i][0]=k1[i-1][0]*(1-pp[i]);
					for(int j=1;j<=i+1;j++){
						k1[i][j]=k1[i-1][j]*(1-pp[i])+k1[i-1][j-1]*pp[i];
					}
				}
				if(ans<k1[k-1][k/2])ans=k1[k-1][k/2];
			}
		}
		if(ans<0.000001)ans=0;
		fout<<"Case #"<<kk<<": "<<ans<<endl;
	}
	return 0;
}