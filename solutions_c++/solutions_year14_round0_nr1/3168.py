#include <iostream>

using namespace std;
void process() {
    int i,j;
    int mark[20];
    for(i=0;i<20;i++)
        mark[i] = 0;
    int n,k;
    cin>>n;
    for(i=1;i<=4;i++) {
        for(j=0;j<4;j++) {
            cin>>k;
            if (i==n) {
                mark[k]++;
            }
        }
    }
    int ret;
    cin>>n;
    for(i=1;i<=4;i++)
        for(j=0;j<4;j++) {
            cin>>k;
            if(i==n) {
                mark[k] ++;
                if (mark[k] == 2) {
                    ret = k;
                }
            }
        }
    
    int count = 0;
    for(i=1;i<20;i++)
        if(mark[i] == 2)
            count++;
    if(count == 0) {
        cout<<"Volunteer cheated!"<<endl;
    } else if (count == 1) {
        cout<<ret<<endl;
    } else {
        cout<<"Bad magician!"<<endl;
    }
    
}
int main() {
    int t;
    cin>>t;
    for(int i =0;i<t;i++) {
        cout<<"Case #"<<(i+1)<<": ";
        process();
    }
    return 0;
}