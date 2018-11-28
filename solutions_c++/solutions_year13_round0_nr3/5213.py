#include<iostream>
#include<math.h>
#include<sstream>
using namespace std;
bool palin(long long int  num){
    string s;
    stringstream ss;
    ss<<num;
    ss>>s;
    int i = 0;
    for(int j = s.size()-1; j >=0 ; j--){
        if(s[i]!=s[j]) return false;
        i++;
    }
    return true;
}
int main(){
    freopen ("C-small-attempt0.in","r",stdin);
    freopen ("output-C.txt","w",stdout);
    int T;
    long long int A;
    long long int B;
    int count = 0;
    cin>>T;
    for(int k = 0 ; k < T ; k++){
        cin>>A>>B;
        count = 0 ;
        for(long long int  i = A ; i <= B ; i++){
            double sqrt_num = sqrt(i);
            double div = sqrt_num/ (int)sqrt_num;
            if (div != 1.0) continue;
            if(palin((int)sqrt_num) && palin(i)){
               count++;
            }
        }
        cout<<"Case #"<<k+1<<": "<<count<<endl;
    }
return 0;
}
