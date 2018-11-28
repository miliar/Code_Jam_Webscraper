#include<fstream>
#include<set>
using namespace std;

ifstream fin("datapacking.in");
ofstream fout("datapacking.out");

int T, N, X;
int files[10005];

int main(){
    int T;
    fin >> T;
    for(int t=0; t<T; t++){
        fin >> N >> X;
        for(int i=0; i<N; i++)
            fin >> files[i];
            
        int discs = 0;
        
        int small = 0, big = N-1;
        sort(files, files + N);
        
        while(small <= big){
            if(small == big){ discs++; small++; }
            else{
                if(files[small] + files[big] <= X){
                    small++;
                    big--;
                    discs++;
                }
                else{
                    big--;
                    discs++;
                }
            }
        }
        
        fout << "Case #" << t+1 << ": ";
        fout << discs << endl;
    }
}
