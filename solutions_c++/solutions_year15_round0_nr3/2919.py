#include<iostream>
#include<map>
#include<string>

using namespace std;

int main(){
    map<string, pair<string,int> > mp;
    mp["ii"] = make_pair("",-1);
    mp["jj"] = make_pair("",-1);
    mp["kk"] = make_pair("",-1);
    mp["ij"] = make_pair("k",1);
    mp["jk"] = make_pair("i",1);
    mp["ki"] = make_pair("j",1);
    mp["ik"] = make_pair("j",-1);
    mp["ji"] = make_pair("k",-1);
    mp["kj"] = make_pair("i",-1);
    int T,t=1;
    cin>>T;
    while (t<=T) {
        int L,X,cp=1,ind = 0;
        string s,inp = "",cs = "";
        cin>>L>>X;
        cin>>s;
        for (int i=0; i<X; i++) {
            inp += s;
        }
        for (int i=0; i<inp.size(); i++) {
            if (ind == 0 && cs =="i") {
                ind++;
                cs = "";
            }
            if (ind == 1 && cs =="j") {
                ind++;
                cs = "";
            }
            
            if (cs=="") {
                cs += inp[i];
                continue;
            }
            else{
                cp *= mp[cs+inp[i]].second;
                cs = mp[cs+inp[i]].first;
            }
        }
        string res = "NO";
        if((ind == 2) && (cs=="k") && (cp==1)){
            res = "YES";
        }
        cout<<"Case #"<<t<<": "<<res<<endl;
        t++;
    }
    
    return 0;
}