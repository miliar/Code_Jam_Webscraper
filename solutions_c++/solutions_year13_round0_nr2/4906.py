#include<fstream>
#include<cstdio>
using namespace std;

int main(){
	int t,i,j,a[100][100];
	int cas,m,n;
	bool b;
	//ifstream in("B-large.in");
	ifstream in("D:\\Installed\\Down\\B-large.in");
	//ifstream in("D:\\Installed\\Down\\B-large.in");
	ofstream out("Lawnmower_Small.out");

	in>>t;
	for(cas=1;cas<=t;cas++){
		in>>n>>m;
		int rmx[100]={0};
		int cmx[100]={0};
		for(i=0;i<n;i++){
			for(j=rmx[i]=0; j<m;j++){
				in>>a[i][j];
				if(a[i][j] > rmx[i] )
					rmx[i] =  a[i][j] ;
				//out<<a[i][j]<<" ";
			}
		}
		for(i=0;i<m;i++){
			for(j=cmx[i]=0; j<n;j++){
				if(a[j][i] > cmx[i] )
					cmx[i] =  a[j][i] ;
			}
		}
		b = true;
		for(i=0;i<n && b ;i++){
			for(j=0; j<m;j++){
				if(a[i][j] != ( rmx[i]<cmx[j]? rmx[i]:cmx[j]) ){
					out<<"Case #"<<cas<<": NO\n";
					b=false;
					break;
				}
			}
		}
		if(b)
			out<<"Case #"<<cas<<": YES\n";
		
	}
	return 0;
}
	
