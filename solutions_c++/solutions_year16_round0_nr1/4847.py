#include<bits/stdc++.h>
using namespace std;

string intToStr(int num){
    stringstream ss;
    ss<<num;
    return ss.str();
}

int strToInt(char str){
    stringstream ss;
    ss<<str;
    int num;
    ss>>num;
    return num;
}

bool isVectorTrue(vector<bool> vec){
    for(int i = 0;i<vec.size();i++){
        if(vec[i]==false) return false;
    }
    return true;
}

int getResult(int N){
    vector<bool> found(10);
    int i = 0;
    while(!isVectorTrue(found)){
        i++;
        string str = intToStr(N*i);

        for(auto& x:str){
            found[strToInt(x)] = true;
        }
    }
    return i*N;
}

int main(){
    ifstream in;in.open("A-large.in");ofstream out("A-large.out");
    //ifstream in("in.big.txt");ofstream out("out.big.txt");
    #define cin in
    #define cout out

    int T,N;
    cin>>T;
    //T=1000000;
    for(int t =0;t<T;t++){
        cin>>N;
        //N=t;
        cout<<"Case #"<<(t+1)<<": ";
        if(N!=0) cout<<getResult(N)<<endl;
        else{
            cout<<"INSOMNIA"<<endl;
        }
    }

}
