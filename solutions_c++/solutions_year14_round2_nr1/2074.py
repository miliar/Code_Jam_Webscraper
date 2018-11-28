#include<iostream>
#include<string>
#include<cmath>

using namespace std;

int main(){
    int x;
    cin>>x;
    for(int cases=0; cases<x; cases++){
        int n;
        cin>>n;
        string a,b;
        cin>>a>>b;
        int result=0;
        auto i=a.begin(), j=b.begin();
        while(i!=a.end() && j!=b.end()){
            char c=*i;
            int q=0,w=0;
            while( i!=a.end() && *i==c ){
                i++;
                q++;
            }
            while( j!=b.end() && *j == c){
                j++;
                w++;
            }
            if(w==0){
                result=-1;
                break;
            }
            result+=abs(q-w);
        }
        cout<<"Case #"<<cases+1<<": ";
        if(result==-1||i!=a.end()||j!=b.end()){cout<<"Fegla Won";}else {cout<<result;}
        cout<<endl;
    }
    return 0;
}
