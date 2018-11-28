#include<bits/stdc++.h>
using namespace std;

int T,K,L,S;
string Ks,Ls;
vector <string> v;

int func1(string b,string a,int S){
    int La=a.size(),Lb=b.size(),fl;
    for(int i=0;i<La;++i){
        fl=1;
        for(int j=0;j<Lb;++j){
            if(a[i]==b[j]){
                fl=0;
                break;
            }
        }
        if(fl)
            return 0;
    }
    if(La==1)
        return S;
    int i=0,j=1,x=1;
    while(j!=La){
        if(a[i]==a[j]){
            ++i,++j;
        }
        else{
            i=0;++j;
            x=j;
        }
    }
    S=S-La;
    return 1+S/x;
}

int func2(string s){
    if(s.size()==S){
        v.push_back(s);
        return 0;
    }
    for(int i=0;i<K;++i){
        func2(s+Ks[i]);
    }
}

int func4(string s){
    int fl=0;
    for(int i=0;i<s.size();++i){
        int ch=1,j=0,it=i;
        while(it<s.size() && j<L){
            if(s[it]==Ls[j]){
                ++it;++j;
            }
            else{
                ch=0;
                break;
            }
        }
        if(ch && j==L)
            ++fl;
    }
    return fl;
}

double func3(int minB){
    double ans=0;
    double prob=1.0/(double)K;
    for(int i=1;i<S;++i)
        prob=prob*1.0/(double)K;
    for(int i=0;i<v.size();++i){
        int x=func4(v[i]);
        ans=ans+(double)(minB-x)*prob;
    }
    return ans;
}

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("outBS1.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        v.clear();
        scanf("%d %d %d",&K,&L,&S);
        cin>>Ks;
        cin>>Ls;
        int minB=func1(Ks,Ls,S);
        func2("");
        printf("Case #%d: %.9lf\n",t,func3(minB));
    }
    return 0;
}
