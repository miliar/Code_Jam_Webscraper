#include<bits/stdc++.h>

using namespace std;

int main(){

    freopen("A-large.in","r",stdin);
    freopen("out1_large.txt","w",stdout);
    int t,p,n;
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>p;
        cout<<"Case #"<<(i+1)<<": ";
        if(p==0) {
                cout<<"INSOMNIA"<<endl;
                continue;
        }
        n=p;
        set<int> st;
        while(1){
            int x = n;
            while(x){
                st.insert(x%10);
                x=x/10;
            }
            if(st.size()==10) break;
            n=n+p;
        }
        cout<<n<<endl;
    }

}
