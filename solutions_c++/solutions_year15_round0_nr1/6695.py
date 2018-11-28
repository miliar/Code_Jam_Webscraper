#include <bits/stdc++.h>

using namespace std;

int main(){

    int t,s,sh,t2=0;
    ofstream cout("sal.txt");
    ifstream cin("A-large.in");
    cin>>t;
    string l;


    while (t--){
        cin>>s;
        vector<int> v(s+1,0);
        cin>>l;
        for (int i=0; i<l.size(); i++){

            v[i]=l[i]-'0';
        }
        /*for (int i=0; i<=s; i++){
            cin>>sh;
            v[i]=sh;
        }*/
        long long int cont = 0;

        long long int need = 0;
        for (int i=0; i<=s; i++){
            if (i>cont){
                need+= i-cont;
                cont+= i-cont;
            }
            cont+=v[i];
        }
        cout<<"Case #"<<++t2<<": "<<need<<endl;
    }

    return 0;
}
