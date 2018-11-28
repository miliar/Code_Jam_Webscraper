#include <iostream>
#include <fstream>

using namespace std;
int main(){
	ifstream inp("B-large.in");
	ofstream out("2_large_out.txt");
	int A;
	inp>>A;
	for (int aa=0;aa<A;aa++){
		out<<"Case #"<<aa+1<<": ";
		int N,M;
		inp>>N>>M;
		int a[N][M];
		int maxhorz[N];
		int maxvert[M];
		memset(maxhorz,0,N*sizeof(int));
		memset(maxvert,0,M*sizeof(int));
		for (int i=0;i<N;i++){
			for (int j=0;j<M;j++){
				inp>>a[i][j];
				//cout<<a[i][j];
				if (maxhorz[i]<a[i][j])
					maxhorz[i]=a[i][j];
				if (maxvert[j]<a[i][j])
					maxvert[j]=a[i][j];
			}
			//cout<<endl;
		}
		for (int i=0;i<N;i++){
			for (int j=0;j<M;j++){
				if (a[i][j]==maxhorz[i] or a[i][j]==maxvert[j]){
				}
				else{
					out<<"NO\n";
					goto end;
				}
			}
		}
		out<<"YES\n";
		end:
			continue;
	}
	return 0;
}
