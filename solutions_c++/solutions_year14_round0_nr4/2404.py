#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int T,N;
void printz(vector<double>& v){
    for(int i=0;i<v.size();i++){
        cout << v[i]*1000 << '\t';
    }
    cout << endl;
}
bool ffind(vector<double>& v, double k){
    for(int i=v.size()-1;i>=0;i--){
        if(v[i]>k){
            //cout << v[i] << endl;
            v.erase(v.begin()+i);
            return true;
        }
    }
    v.erase(v.end()-1);
    return false;
}
long long DWar(vector<double> k,vector<double> n){
    long long count=0,k1=0,k2=N-1,n1=0,n2=N-1;
    sort(k.begin(),k.end());
    sort(n.begin(),n.end());
    reverse(k.begin(),k.end());
    reverse(n.begin(),n.end());
    //printz(k);
    //printz(n);
    while(k1<=k2){
        if(ffind(n,k[k1])){
            count++;
        }
        k1++;
    }
    return count;
}
long long War(vector<double> k,vector<double> n){
    long long count=0,k1=0,k2=N-1,n1=0,n2=N-1;
    sort(k.begin(),k.end());
    sort(n.begin(),n.end());
    reverse(k.begin(),k.end());
    reverse(n.begin(),n.end());
    //printz(k);
    //printz(n);
    while(n1<=n2){
            //cout << n[n1] << " < ";
        if(!ffind(k,n[n1])){
            count++;
        }
        n1++;
    }
    return count;
}
int main()
{
    freopen("t.txt","r",stdin);
    freopen("o.txt","w",stdout);
    double temp;
    cin >> T;
    for(int t=0;t<T;t++){
        vector<double> Naomi;
        vector<double> Ken;
        cin >> N;
        for(int i=0;i<N;i++){
            cin >> temp;
            Naomi.push_back(temp);
        }
        for(int i=0;i<N;i++){
            cin >> temp;
            Ken.push_back(temp);
        }
        sort(Naomi.begin(),Naomi.end());
        sort(Ken.begin(),Ken.end());
        reverse(Ken.begin(),Ken.end());
        int f1=DWar(Ken,Naomi);
        int f2=War(Ken,Naomi);
        printf("Case #%i: %i %i\n",t+1,f1,f2);
    }
    return 0;
}
