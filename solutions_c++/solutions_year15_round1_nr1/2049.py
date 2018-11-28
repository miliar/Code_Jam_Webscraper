#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main(){
    
    int t=1,T;
    cin>>T;
    while (t<=T){
        int N,a1=0,a2=0,mr=0;
        cin>>N;
        vector<int> vi(N);
        for (int i=0; i<N; i++) {
            cin>>vi[i];
        }
        for (int i=1; i<N; i++) {
            if (vi[i]<vi[i-1]) {
                mr = max(mr,vi[i-1] - vi[i]);
                a1 += vi[i-1] - vi[i];
            }
            
        }
        
        for (int i=0; i<(N-1); i++) {
            //cout<<vi[i]<<"\t";
            a2 += min(mr,vi[i]);
        }
        //cout<<endl<<mr<<endl;
        cout<<"Case #"<<t<<": "<<a1<<' '<<a2<<endl;
        t++;
    }
    return 0;
}