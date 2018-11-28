#include <iostream>
using namespace std;
int A[4][4];
int B[4][4];

int main(){

    int test_cases;
    int a, b;
    cin>>test_cases;
    int t = 0;
    while(test_cases--){
        t++;
        cin>>a;
        for(int i = 0; i < 4; i++) cin>>A[i][0]>>A[i][1]>>A[i][2]>>A[i][3];
        cin>>b;
        for(int i = 0; i < 4; i++) cin>>B[i][0]>>B[i][1]>>B[i][2]>>B[i][3];
        int c = 0, d = 0;
        a--; b--;
        for(int j = 0; j < 4; j++)
        for(int i = 0; i < 4; i++)
        if(A[a][i] == B[b][j]){
            c++;
            d = A[a][i];
//            cout<<"d = "<<d<<endl;
        }
//        c /= 2;

        if(c == 1)      cout<<"Case #"<<t<<": "<<d<<endl;
        else if(c > 1)  cout<<"Case #"<<t<<": Bad magician!"<<endl;
        else            cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
    }
}
