#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

vector <string> k1;
vector <int> l;

void flip(string a,int g){
    for(int i=0;i<a.length();i++){
        string b=a;
        for(int k=0;k<i+1;k++){
            if(b[k]=='-')
                b[k]='+';
            else
                b[k]='-';
        }
        for(int k=0;k<(i+1)/2;k++){
            char temp=b[k];
            b[k]=b[i+1-k-1];
            b[i+1-k-1]=temp;
        }
        bool q=false;
        for(int k=0;k<k1.size();k++){
            if(b==k1[k]){
                if(g+1<l[k]){
                    l[k]=g+1;
                    flip(b,g+1);
                }
                q=true;
                break;
            }
        }
        if(!q){
            k1.push_back(b);
            l.push_back(g+1);
            flip(b,g+1);
        }
    }
}

void calc(){
    for(int r=1;r<=10;r++){
        cout<<r<<endl;
        string a="";
        for(int i=0;i<r;i++)
            a+="+";
        k1.push_back(a);
        l.push_back(0);
        flip(a,0);
    }
}

ifstream fin("b55.in");
ofstream fout("b55.out");


int main(){
    calc();
    cout<<endl;
    int y;
    cin>>y;
    int t;
    fin>>t;
    for(int i=0;i<t;i++){
        string a;
        fin>>a;
        for(int k=0;k<k1.size();k++){
            if(k1[k]==a){
                fout<<"Case #"<<i+1<<": "<<l[k]<<endl;
                break;
            }
        }
    }
    return 0;
}
