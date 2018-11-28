

#include<iostream>
#include<algorithm>
#include <cstdio>
#include<string>
using namespace std;

void replace(string& s, int start, int end, char newC){
    while (start < end){
        s[start++]=newC;
    }
}

int main(){
    freopen("output.txt","w",stdout);
    int testcases,steps,mIndx,pIndx;
    string s;
    cin>>testcases;
    for (int i=0 ; i<testcases ; i++){
            steps = 0;
            cin >> s;
            mIndx = s.find('-');
            pIndx = s.find('+');
            while (mIndx!=-1){
                    steps++;
                if (mIndx == 0){
                    if (pIndx != -1){
                            replace(s,0,pIndx,'+');
                    }else{
                        replace(s,0,s.length(),'+');
                    }
                }else{
                    replace(s,0,mIndx,'-');
                }
                mIndx = s.find('-');
                pIndx = s.find('+');
            }

        if(i)cout<<endl;
        cout<<"Case #"<<(i+1)<<": "<<steps;
    }
    return 0;
}
