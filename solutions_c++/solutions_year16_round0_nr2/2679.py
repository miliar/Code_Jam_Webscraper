#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("B.txt", "r", stdin);
    freopen("Bout.txt", "w", stdout);
    int T;
    cin>>T;
    for(int t=1 ; t<=T ; ++t){
        string te, st;
        cin>>te;
        st += te[0];
        for(int i=1 ; i<te.size() ; ++i){
            if(te[i] != st[st.size()-1])
                st += te
                [i];
        }
        //cout<<st<<endl;
        int b = st.size()-1, top = 0, temp;
        bool rev = false;
        long long ans = 0;
        for(int i=st.size()-1 ; i>=0 ; --i){
            if(!rev){
                if(st[b] == '-'){
                    if(st[top] == '+')
                        ans += 2;
                    else
                        ans += 1;
                    rev = true;
                    temp = top;
                    top = b;
                    b = temp+1;
                }
                else
                    b--;
            }
            else{
                if(st[b] == '+'){
                    if(st[top] == '-')
                        ans += 2;
                    else
                        ans += 1;
                    rev = false;
                    temp = top;
                    top = b;
                    b = temp-1;;
                }
                else
                    b++;
            }
        }
        cout<<"Case #"<<t<<": "<<ans<<"\n";
    }
}
