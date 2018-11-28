#include<fstream>
#include<iomanip>
#include<algorithm>
using namespace std;

int main(int argc,char *argv[])
{
ifstream fin(argv[1]);
ofstream fout("output.txt");
	int T;
	fin>>T;
	for(int t=1;t<=T;t++){
	fout<<"Case #"<<t<<": ";
			int n;
			fin>>n;
			double ar1[n],ar2[n];
			int ans1=0,ans2=0;
			for(int i=0;i<n;i++)fin>>ar1[i];
			for(int i=0;i<n;i++)fin>>ar2[i];
			
			sort(ar1,ar1+n);
			sort(ar2,ar2+n);
			
			int i=0,j=0;
			while(i<n && j<n){
				if(ar1[i]>ar2[j])i++,ans1++,j++;
				else i++;
			}
			i=0,j=0;
			while(i<n && j<n){
				if(ar2[j]>ar1[i])i++,ans2++,j++;
				else j++;
			}
			ans2= n-ans2;
			fout<<ans1<<" "<<ans2<<endl;
			
	}
fin.close();
fout.close();
return 0;
}


