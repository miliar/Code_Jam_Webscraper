#include<iostream>
#include<string>
#include<sstream>
#include<cmath>
#include<fstream>

#define N_MAX 1047
#define T_MAX 107

#define For(n) for(int i = 0; i<(n); i++)
#define ForJ(n) for(int j = 0; j<(n); j++)

#define cin input

int output[T_MAX];
int aud_sum[N_MAX];

using namespace std;

int main(){
    ifstream input; input.open("A-large.in");
    ofstream out; out.open("A-large.out");

    int T, Smax;
    string audience;
    cin>>T;

    For(T){
        int invite = 0;
        cin>>Smax;
        cin>>audience;
        for(int j = 0; j<=Smax; j++){
            stringstream a; char b;
            a<<audience.substr(j,1); a>>b;
            aud_sum[j+1] = (int)(b - '0') + aud_sum[j];
            invite += max(j-aud_sum[j]-invite, 0);
            //cout<<" ("<<aud[j]<<","<<aud_sum[j]<<" ";

        }//cout<<endl;
        //cout<<invite;
        output[i] = invite;
    }

    For(T){
        out<<"Case #"<<i+1<<": "<<output[i]<<endl;
    }



}
