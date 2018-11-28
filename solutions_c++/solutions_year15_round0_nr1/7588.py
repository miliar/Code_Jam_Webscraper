#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main (){
    ifstream in ("A-large.in");
    ofstream out ("test.out");
    int T;
    int N;
    string a;
    int people;
    int friends;
    int x;
    int A[100000];
    in >> T;
    for (int i=0; i<T; i++){
        in >> N;
        in >> a;
        for (int j=0; j<=N; j++){
            A[j]=a[j]-48;
        }
        
        people=0;
        friends=0;
        for (int j=0; j<N+1; j++){
            if (people>=j){
                people=people+A[j];
            }
            
            else{
                x=j-people;
                friends=friends+x;
                people=people+x+A[j];
            }
        }
        
        out << "case #" << i+1 << ": " << friends << endl;
    }
    
    in.close();
    out.close();
    return 0;
}