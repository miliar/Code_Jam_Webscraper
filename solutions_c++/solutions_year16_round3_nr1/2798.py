#include<bits/stdc++.h>
using namespace std;
#define MP(i,j) make_pair(i,j)
#define f first
#define s second
int main(){
    int n,T,num;
    cin>>T;
    for(int t = 1; t <= T; t++){
        cin>>n;
        priority_queue< pair<int,int> > P;
        for(int i = 0; i < n; i++){
            cin>>num;
            P.push(MP(num,i));
        }
        cout<<"Case #"<<t<<": ";
        string res = "";
        while(!P.empty()){
            int tam = P.size();
            pair<int,int> Y = P.top();P.pop();
            pair<int,int> Z = P.top();P.pop();
            if(tam%2 == 0){
                if(Z.f == Y.f){
                    int r = (Y.f)-1;
                    int l1 = Y.s;
                    int l2 = Z.s;
                    res += ((char)(l2 + 'A'));
                    res += ((char)(l1 + 'A'));
                    if(r){
                        P.push(MP(r,l1));
                        P.push(MP(r,l2));
                    }
                }else{
                    int r = (Y.f)-1;
                    int l = Y.s;
                    res += ((char)(l+'A'));
                    if(r) P.push(MP(r,l));
                    P.push(Z);
                }
            }else{
                int r = (Y.f)-1;
                int l = Y.s;
                res += ((char)(l+'A'));
                if(r)P.push(MP(r,l));
                P.push(Z);
            }
            res += " ";
        }
        cout<<res.substr(0,res.size()-1);
        if(t!= T)cout<<endl;
    }
}
