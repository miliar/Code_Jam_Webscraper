#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream in("magictrick.in");
ofstream out("magictrick.out");

bool checkIfExists(vector<int> vect, int x){
    return find(vect.begin(), vect.end(), x) != vect.end();
}

void solve(int test){
    int row1,row2;
    vector<int> row1Elements;
    in>>row1;
    for(int i=1;i<=4;i++){
        for(int j=1;j<=4;j++){
            int x;
            in>>x;
            if(i==row1){
                row1Elements.push_back(x);
            }
        }
    }
    int sol = 0;
    in>>row2;
    for(int i=1;i<=4;i++){
        for(int j=1;j<=4;j++){
            int x;
            in>>x;
            if(i==row2 && checkIfExists(row1Elements, x)){
                if(sol == 0){
                    sol = x;
                } else{
                    sol = -1;
                    }
            }
        }
    }
    out<<"Case #"<<test<<": ";
    if(sol==-1){
        out<<"Bad magician!";
    } else if(sol==0){
        out<<"Volunteer cheated!";
    } else{
        out<<sol;
    }
    out<<"\n";
}

int main()
{
    int t;
    in>>t;
    for(int i=1;i<=t;i++){
        solve(i);
    }
    return 0;
}
