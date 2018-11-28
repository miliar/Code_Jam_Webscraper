#include<bits/stdc++.h>
using namespace std;
map<string,string> table;

int l, x;
int solve(string s,int start, string tofind){
    string res="";
    for(int i=start;i<l*x;i++){
        res+=s[i%l];
        if(res.length()>=2){
            res=table[res];
        }
        if(res==tofind && tofind!="k")
            return i;
        if(res==tofind&& tofind=="k" && i == l*x-1)
            return i;
    }
    return -1;
}

int main(){
    int tc;
    table["-i"]="-i";
    table["-j"]="-j";
    table["-k"]="-k";
    table["1i"]="i";
    table["1j"]="j";
    table["1k"]="k";
    table["-1i"]="-i";
    table["-1j"]="-j";
    table["-1k"]="-k";

    table["ii"]="-1";
    table["ij"]="k";
    table["ik"]="-j";
    table["-ii"]="1";
    table["-ij"]="-k";
    table["-ik"]="j";
    table["-1i"]="-i";
    table["-1j"]="-j";
    table["-1k"]="-k";

    table["ji"]="-k";
    table["jj"]="-1";
    table["jk"]="i";
    table["-ji"]="k";
    table["-jj"]="1";
    table["-jk"]="-i";

    table["ki"]="j";
    table["kj"]="-i";
    table["kk"]="-1";
    table["-ki"]="-j";
    table["-kj"]="i";
    table["-kk"]="1";
    cin>>tc;
    ofstream fout;
    fout.open("three.out");
    for(int z=1;z<=tc;z++){
        string s;
        cin>>l>>x;

        cin>>s;
        //cout<<s<<endl;

        int i=solve(s,0,"i");
        //cout<<i<<endl;
        if(i==-1){
            //cout<<"i not found"<<endl;
            fout<<"Case #"<<z<<": NO"<<endl;
            continue;
        }
        i=solve(s,i+1,"j");
        //cout<<i<<endl;
        if(i==-1){
            //cout<<"j not found"<<endl;
            fout<<"Case #"<<z<<": NO"<<endl;
            continue;
        }
        i=solve(s,i+1,"k");

        if(i==-1)
            fout<<"Case #"<<z<<": NO"<<endl;
        else fout<<"Case #"<<z<<": YES"<<endl;
    }
    return 0;
}
