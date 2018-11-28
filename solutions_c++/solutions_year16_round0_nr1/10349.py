#include<bits/stdc++.h>
using namespace std;
bitset<11> bs;
bool cek(){
    if(bs[0]==false && bs[1]==false && bs[2]==false && bs[3]==false && bs[4]==false && bs[5]==false && bs[6]==false && bs[7]==false && bs[8]==false && bs[9]==false)return true;
    else return false;
}
int main(){
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    long long num, t, temp;
    string result;
    cin>>t;
    bs.set();
    for(int i=1 ;i<=t ;i++){
        cin>>num;
        if(num==0){
             cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
             continue;
        }
        int ct = 1, x=1;
        temp =0;
        while(!cek()){
            temp += num;
            stringstream convert;
            convert << temp;
            result = convert.str();
            //cout<<result<<endl;
            for(int j=0 ;j<result.length();j++){
                int idx = (int) result.at(j) - '0';
                bs[idx] = false;
            }
            x++;ct++;
            result.clear();
        }
        cout<<"Case #"<<i<<": "<<temp<<endl;
        bs.set();
    }
    return 0;
}
