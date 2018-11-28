#include<fstream>
//#include<iostream>

using namespace std;
int a[1010];
int main(){
    int t,ans,tot;
    int Smax;
    char ch;
    ifstream cin("A-large-1.in");
    ofstream cout("A-large-1.out");
    cin>>t;
    for(int e=0;e<t;e++){
        cin>>Smax;
        for(int i=0;i<=Smax;i++){cin>>ch;a[i]=ch-'0';};
        tot = a[0];
        ans=0;
        for(int i=1;i<=Smax;i++){
            if(tot<i){
                ans = ans+i-tot;
                tot=i;
            }
            tot=tot+a[i];
        }
        cout<<"Case #"<<e+1<<": "<<ans<<'\n';
    }
    cin.close();
    cout.close();
    return 0;
}
