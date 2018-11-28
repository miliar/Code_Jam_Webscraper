#include <algorithm>
#include <cstdio>
#include <string>
#include <iostream>
#include <map>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;
typedef pair<string,string> P;

map<P,string> mat;
string vals[10004];

bool ok(const string& s) {
    for(int i=1;i<s.size();i++) if(vals[i]=="i") for(int j=i+1;j<s.size();j++)  {
        //string s1=s.substr(0,i);
        //string s2=s.substr(i,j-1);
        // string s3=s.substr(j,s.size()-i-j+1);

        //printf("[%d,%d) [%d,%d) [%d,%d)\n",0,i,i,j,j,s.size());
        string s1=vals[i];
        string s2=mat[P(s1,vals[j])];
        s2=mat[P(s2,"-1")];
        string s3=mat[P(vals[j],vals[s.size()])];
        s3=mat[P("-1",s3)];
        //cout<<s1<<","<<s2<<","<<s3<<endl;
        if(s1=="i"&&s2=="j"&&s3=="k") return true;
    }
    return false;
}

void small() {
    int L,X;
    cin>>L>>X;
    string s,t;
    cin>>s;
    rep(i,X) t+=s;

    vals[1]=string(1,t[0]);
    rep(i,t.size()+1) if(i>1) {
        vals[i]=mat[P(vals[i-1],string(1,t[i-1]))];
    }
    
    if(ok(t)) {
        cout<<"YES"<<endl;
    }
    else {
        cout<<"NO"<<endl;
    }

}

int main() {
    mat[P("1","1")]="1";
    mat[P("1","i")]="i";
    mat[P("1","j")]="j";
    mat[P("1","k")]="k";
    mat[P("1","-1")]="-1";
    mat[P("1","-i")]="-i";
    mat[P("1","-j")]="-j";
    mat[P("1","-k")]="-k";
    mat[P("-1","1")]="-1";
    mat[P("-1","i")]="-i";
    mat[P("-1","j")]="-j";
    mat[P("-1","k")]="-k";
    mat[P("-1","-1")]="1";
    mat[P("-1","-i")]="i";
    mat[P("-1","-j")]="j";
    mat[P("-1","-k")]="k";

    mat[P("i","1")]="i";
    mat[P("i","i")]="-1";
    mat[P("i","j")]="k";
    mat[P("i","k")]="-j";
    mat[P("i","-1")]="-i";
    mat[P("i","-i")]="1";
    mat[P("i","-j")]="-k";
    mat[P("i","-k")]="j";
    mat[P("-i","1")]="-i";
    mat[P("-i","i")]="1";
    mat[P("-i","j")]="-k";
    mat[P("-i","k")]="j";
    mat[P("-i","-1")]="i";
    mat[P("-i","-i")]="-1";
    mat[P("-i","-j")]="k";
    mat[P("-i","-k")]="-j";

    mat[P("j","1")]="j";
    mat[P("j","i")]="-k";
    mat[P("j","j")]="-1";
    mat[P("j","k")]="i";
    mat[P("j","-1")]="-j";
    mat[P("j","-i")]="k";
    mat[P("j","-j")]="1";
    mat[P("j","-k")]="-i";
    mat[P("-j","1")]="-j";
    mat[P("-j","i")]="k";
    mat[P("-j","j")]="1";
    mat[P("-j","k")]="-i";
    mat[P("-j","-1")]="j";
    mat[P("-j","-i")]="-k";
    mat[P("-j","-j")]="-1";
    mat[P("-j","-k")]="i";

    mat[P("k","1")]="k";
    mat[P("k","i")]="j";
    mat[P("k","j")]="-i";
    mat[P("k","k")]="-1";
    mat[P("k","-1")]="-k";
    mat[P("k","-i")]="-j";
    mat[P("k","-j")]="i";
    mat[P("k","-k")]="1";
    mat[P("-k","1")]="-k";
    mat[P("-k","i")]="-j";
    mat[P("-k","j")]="i";
    mat[P("-k","k")]="1";
    mat[P("-k","-1")]="k";
    mat[P("-k","-i")]="j";
    mat[P("-k","-j")]="-i";
    mat[P("-k","-k")]="-1";

    int T;
    cin>>T;
    rep(i,T) {
        printf("Case #%d: ",i+1);
        small();
    }
    return 0;
}

