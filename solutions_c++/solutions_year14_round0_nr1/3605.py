#include<fstream>
#include<set>
using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("magictrick.out");

int main(){
    int T;
    fin >> T;
    for(int t=0; t<T; t++){
        set<int> A;
        int row, val;
        
        A.clear();
        fin >> row;
        for(int r=0; r<4; r++)
            for(int c=0; c<4; c++){
                fin >> val;
                if(r+1 == row)
                    A.insert(val);
            }
            
        int ans = 0, num;
                   
        fin >> row;
        for(int r=0; r<4; r++)
            for(int c=0; c<4; c++){
                fin >> val;
                if(r+1 == row && A.count(val)){
                    ans++;
                    num = val;
                }
            }
        
        fout << "Case #" << t+1 << ": ";
        if(ans == 0) fout << "Volunteer cheated!" << endl;
        else if(ans == 1) fout << num << endl;
        else fout << "Bad magician!" << endl;
    }
}
