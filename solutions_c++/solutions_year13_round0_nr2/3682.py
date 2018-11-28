
#include <iostream>
using namespace std;

void mower(int i){
    int n,m;
    cin>>n>>m;
    int garden[n][m],current[1][1];
    for (int j=0; j<n; j++) {
        for (int k=0; k<m; k++) {
            cin>>garden[j][k];
        }
    }
    for (int j=0; j<n; j++) {
        for (int k=0; k<m; k++) {
            current[0][0]=garden[j][k];
            for (int x=0; x<m; x++) {
                if (garden[j][x]>current[0][0]) {
                    for (int g=0; g<n; g++) {
                        if (garden[g][k]>current[0][0]) {
                            cout<<"Case #"<<i+1<<": NO"<<endl;
                            return;
                        }
                    }
                }
            }
        }
    }
    cout<<"Case #"<<i+1<<": YES"<<endl;
    return;
}
int main(int argc, const char * argv[])
{
    int no_of_tcases;
    cin>>no_of_tcases;
    for (int i=0; i<no_of_tcases; i++) {
        mower(i);
    }
    return 0;
}