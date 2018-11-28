#include<fstream>
#include<set>
using namespace std;

ifstream fin("D-large.in");
ofstream fout("war.out");

int main(){
    int T;
    fin >> T;
    for(int t=0; t<T; t++){
        int N;
        fin >> N;
        
        double my[1005];
        for(int i=0; i<N; i++)
            fin >> my[i];
        sort(my, my+N);
        
        double op[1005];
        for(int i=0; i<N; i++)
            fin >> op[i];
        sort(op, op+N);
            
        int normal = 0;
        int i = 0, j = 0;
        while(j<N){
            if(op[j] > my[i]){
                j++;
                i++;
                normal++;
            }
            else j++;
        }
        
        int cheat = 0;
        i = 0, j = 0;
        while(i < N){
            if(my[i] > op[j]){
                cheat++;
                j++;
            }
            i++;
        }
        
        fout << "Case #" << t+1 << ": " << cheat << " " << N-normal << endl;
    }
}
