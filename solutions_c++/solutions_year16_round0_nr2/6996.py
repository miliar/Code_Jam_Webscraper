#include <bits/stdc++.h>
#define N 1000

using namespace std;

string inverse(string str, int l, int r){
    string k = str;
    for(int border=l;border<=r;border++){
        if(k[border]=='-') k[border]='+';
        else k[border]='-';
    }
    return k;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int n=0;
    cin>>n;
    string vec[N];
    int result[N];
    int sch=0;
    for(int in=0;in<n;in++){
        cin>>vec[in];
    }
    for(int i=0;i<n;i++){
        int res=0;
        for(int j=vec[i].length()-1;j>-1;j--){
            if(vec[i][j]=='-'){
                vec[i]=inverse(vec[i], 0, j);
                res++;
            }
        }
        result[sch]=res;
        sch++;
        res=0;
    }
    for(int out=0;out<sch;out++){
        cout<<"Case #"<<out+1<<": "<<result[out]<<endl;
    }
    return 0;
}
