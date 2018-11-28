#include<iostream>
using namespace std;

int res[5] = {1,4,9,121,484};
int T,A,B;

int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int cs=1;cs<=T;++cs){
        cin>>A>>B;
        int cnt = 0;
        for(int i=0;i<5;++i){
            if(res[i]>=A&&res[i]<=B) ++cnt;
        }
        cout<<"Case #"<<cs<<": ";
        cout<<cnt<<endl;
    }
    return 0;
}
