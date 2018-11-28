#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

string multiplying(char &res , char &a){
    string retStr;
    if(res=='1')
        return retStr+a;
    else if(res==a)
        return "-1";
    else if(a=='1')
        return retStr+res;
    else if(res=='i' && a=='j')
        return "k";
    else if(res=='i' && a=='k')
        return "-j";
    else if(res=='j' && a=='i')
        return "-k";
    else if(res=='j' && a=='k')
        return "i";
    else if(res=='k' && a=='i')
        return "j";
    else if(res=='k' && a=='j')
        return "-i";
}

int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    //freopen("Input.txt", "r", stdin);
    freopen("OutputC.txt", "w", stdout);
    int T,L;
    string s,answer,Sinitial;
    bool negative,newStart;
    int found;
    unsigned long long X,limit;
    char letters[2]= {'i','j'};
    cin>>T;
    for(int i=0;i<T;i++){
        string res;
        negative = false;
        newStart = false;
        answer = "NO";
        found = 0;
        cin>>L>>X;
        cin>>s;
        Sinitial = s;
        for(int j=1;j<X;j++){
            s += Sinitial;
        }
        limit = L*X;
        if(limit<3){
           cout<<"Case #"<<i+1<<": "<<"NO"<<endl;
           continue;
        }
        res = s[0];
        if(res[0]==letters[found]){
            found++;
            newStart = true;
        }
        for(int j=1;j<limit;j++){
            if(newStart)
                res = s[j];
            else
                res = multiplying(res[0],s[j]);
            if(res[0]=='-'){
                res = res.substr(1,1);
                negative = !negative;
            }
            if(!negative && res[0]==letters[found]){
                found++;
                newStart = true;
            }
            else
                newStart = false;
        }
        if(! negative && res[0]=='k'&&found==2)
            answer = "YES";
        cout<<"Case #"<<i+1<<": "<<answer<<endl;
    }





    return 0;
}
