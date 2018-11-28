#include<fstream>
#include<iomanip>
using namespace std;

int main(){
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");
	int t;
	fin>>t;
	double ans;
	for(int kk=1;kk<=t;kk++){
		int n;
		double v,x,r[100],c[100];
		fin>>n>>v>>x;
		for(int i=0;i<n;i++){
			fin>>r[i]>>c[i];
		}
		int bigger=0,smaller=0;
		for(int i=0;i<n;i++){
			if(c[i]<x)smaller++;
			if(c[i]>x)bigger++;
		}
		if(smaller==n||bigger==n)
			fout<<"Case #"<<kk<<": "<<"IMPOSSIBLE"<<endl;
		else{
			ans=0;
			if(n==1){
				ans=v/r[0];
			}
			else if(n==2){
				if(c[0]==c[1]){
					ans=v/(r[0]+r[1]);
				}
				else{
					ans=(v*c[0]-v*x)/(r[1]*c[0]-r[1]*c[1]);
					if(ans<(v*c[1]-v*x)/(r[0]*c[1]-r[0]*c[0]))
						ans=(v*c[1]-v*x)/(r[0]*c[1]-r[0]*c[0]);
				}
			}
			fout<<"Case #"<<kk<<": "<<setprecision(18)<<ans<<endl;
		}
	}
	return 0;
}