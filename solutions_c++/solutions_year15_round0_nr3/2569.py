#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<cstdio>
#define FOR(i,n) for(int i=0;i<n;i++)
using namespace std;

map<pair<char,char>,char > r_val {
    {{'1','1'},'1' },
    {{'1','i'},'i' },
    {{'1','j'},'j' },
    {{'1','k'},'k' },
    {{'i','1'},'i' },
    {{'i','i'},'1' },
    {{'i','j'},'k' },
    {{'i','k'},'j' },
    {{'j','1'},'j' },
    {{'j','i'},'k' },
    {{'j','j'},'1' },
    {{'j','k'},'i' },
    {{'k','1'},'k' },
    {{'k','i'},'j' },
    {{'k','j'},'i' },
    {{'k','k'},'1' },
};
map<pair<char,char>,int > r_sign {
    {{'1','1'},1 },
    {{'1','i'},1 },
    {{'1','j'},1 },
    {{'1','k'},1 },
    {{'i','1'},1 },
    {{'i','i'},-1 },
    {{'i','j'},1 },
    {{'i','k'},-1 },
    {{'j','1'},1 },
    {{'j','i'},-1 },
    {{'j','j'},-1 },
    {{'j','k'},1 },
    {{'k','1'},1 },
    {{'k','i'},1 },
    {{'k','j'},-1 },
    {{'k','k'},-1 },
};
struct quater{
    char val='1';
    int sign=1;
    quater(){
        val = '1';
        sign = 1;
    }
    void times(char op){
        auto p = make_pair(val,op);
        val = r_val[p];
        int s = r_sign[p];
//        cout<<val<<' '<<op<<' '<<s<<endl;
        sign *= r_sign[p];
    }
};
int main(){
    int T;
    cin>>T;
    FOR(k,T){
        int L,X;
        cin.ignore();
        //scanf("%d %d",&L,&X);
        cin>>L>>X;
        cin.ignore();
        string str;
        cin>>str;
        string res;
        FOR(i,X){
            res+=str;
        }
        quater q1;
        q1.val='1';
        q1.sign = 1;
        bool ok = false;
        vector<quater> precalc(res.size(),quater());
        precalc[res.size()-1].times(res[res.size()-1]);
        for(int i=res.size()-2;i>=0;i--){
            precalc[i].val = res[i];
            precalc[i].times(precalc[i+1].val);
            precalc[i].sign *= precalc[i+1].sign;
        }
        FOR(i,res.size()){
            q1.times(res[i]);
            if(q1.val=='i'&&q1.sign==1){
                quater q2;
                q2.val = '1';
                q2.sign = 1;
                for(int j=i+1;j<res.size();j++){
                    q2.times(res[j]);
                    if(q2.val=='j'&&q2.sign==1){
                        if(j==res.size()-1){
                            break;
                        }
                        if(precalc[j+1].val=='k'&&precalc[j+1].sign==1){
                            ok =true;
                            //cout<<i<<" "<<j<<endl;
                            goto end;
                        }
                    }
                }
            }
        }
    end:
        cout<<"Case #"<<k+1<<": "<<(ok ? "YES" : "NO")<<endl;
    }
}
