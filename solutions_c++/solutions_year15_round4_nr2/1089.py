#include <fstream>
#include <iomanip>
using namespace std;

int main(){
	ifstream fin ("B-small-attempt0.in");
	ofstream fout ("B-output.txt");
	fout << fixed;
	int T, N;
	double V, X;
	double R[2], C[2];
	fin >> T;
	for(int i = 1; i<=T; i++){
        fin >> N >> V >> X;
        for(int a = 0; a<N; a++){
            fin >> R[a] >> C[a];
        }
        if(N==1){
            if(C[0]!=X) fout << "Case #" << i << ": IMPOSSIBLE\n";
            else fout << "Case #" << i << ": " << setprecision(9) << V/R[0] << '\n';
        }
        if(N==2){
            if((X>C[0] && X<C[1]) || (X<C[0] && X>C[1])){
                double a = 0 - (X-C[0])/(X-C[1]);
                if(V*a/(a+1)/R[1] > V/(a+1)/R[0]) fout << "Case #" << i << ": " << setprecision(9) << V*a/(a+1)/R[1] << '\n';
                else fout << "Case #" << i << ": " << setprecision(9) << V/(a+1)/R[0] << '\n';
            }else if(X==C[0] && X==C[1]){
                fout << "Case #" << i << ": " << setprecision(9) << V/(R[0]+R[1]) << '\n';
            }else if(X==C[0]){
                fout << "Case #" << i << ": " << setprecision(9) << V/R[0] << '\n';
            }else if(X==C[1]){
                fout << "Case #" << i << ": " << setprecision(9) << V/R[1] << '\n';
            }else fout << "Case #" << i << ": IMPOSSIBLE\n";
        }
	}
	return 0;
}
