#include<iostream>
#include<windows.h>
using namespace std;

int A[121];

int main() {
    ios_base::sync_with_stdio(0);
    int T, S;
    string s;
    cin>>T;
    for(int tt=1; tt<=T; tt++) {
        for(int i=1; i<=120; i++)
            A[i]=0;
        cin>>s;
        S=s.length();
        for(int i=1; i<=S; i++) {
            if(s[i-1]=='+')
                A[i]=1;
            else
                A[i]=0;
        }
        A[S+1]=1;
        int w=0;
        int counter = 0;
        int i = S;
        int tmp;
        while(i >= 1) {
            if(A[i]==0) {
                w++;
                while(i>=1 && A[i]==0)
                    i--;
                tmp = i;
                while( tmp>=1 ) {
                    A[tmp]+=1;
                    A[tmp]%=2;
                    tmp--;
                }
            } else {
                while(A[i]==1)
                    i--;
            }
        }
        cout<<"Case #"<<tt<<": "<<w<<endl;
    }

    return 0;
}







/*
void write(int l) {
    while(l > 0) {
        cout<<(l%2);
        l/=2;
    }
    cout<<endl;
    return;
}

int main() {
    ios_base::sync_with_stdio(0);
    int T, S;
    cin>>T;
    for(int tt=1; tt<=T; tt++) {
        cin>>S;
        int p = 1;
        unsigned int l = 0;
        char c;
        for(int i = 0; i<S; i++) {
            cin>>c;
            if(c=='-') {
                l += p;
            }
            p*=2; // - to 1
        }
        int counter = 0;
        cout<<l<<endl;
        write(l);
        //cout<<( ((1<<(S-1)) & l == 0) && S > 0)<<" "<<(!((1<<(S-1)) & l))<<" "<<((1<<(S-1)) & l == 0)<<" "<<(S>0)<<endl;
        /*while( !((1<<(S-1)) & l == 0) && S>0) {
                S--;
                cout<<" "<<S<<endl;
            }
       // cout<<((~l)%(1<<S-3))<<endl;
        while(l != 0 && S>0) {
            cout<<l<<" "<<(~l)<<endl;
            cout<<S<<endl;
             while( !((1<<(S-1)) & l == 0) && S>0) {
                S--;
                cout<<" "<<S<<endl;
            }
            int d = (1<<(S-1));
            l = (~l)%d;
            counter++;
        }
        cout<<counter<<endl;
    }

}
*/
