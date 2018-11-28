#include <iostream>
using namespace std;

bool solveable(int x, int y, int N) {
    switch(N) {
        case 1:
            return true;
        case 2:
            return !((x%2) && (y%2)); //only true if one is odd
        case 3:
            return ((x>1) && (y>1) && !((x*y)%3));
        case 4:
            return (x==4 || y == 4) && x+y > 6;  
        default:
            return false;
    }
}

int main() {
    int N;
    cin>>N;
    for(int i = 0; i < N; i++) {
        int x,r,c;
        cin>>x>>r>>c;
        cout<<"Case #"<<i+1<<": "<<(solveable(r,c,x)?"GABRIEL":"RICHARD")<<endl;
    }
    return 0;
}
