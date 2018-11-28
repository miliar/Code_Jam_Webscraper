#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<cstdio>
using namespace std;

struct node{
    int limit;
    int joins;
}temp;
typedef struct node Node;
vector <Node> defalutval[10];

vector <Node> getans(int ar[],int n){
    if(n==1)
    {
        return defalutval[ar[0]];
    }
    vector <Node> mytemp = getans(ar,n-1);
    int index = n-1;
    vector <Node> otemp = defalutval[ar[index]];

    vector <Node> abc;
    for(int i=0;i<mytemp.size();i++){
        for(int j=0;j<otemp.size();j++){
            int k = mytemp[i].joins+otemp[j].joins;
            int l = max(mytemp[i].limit,otemp[j].limit);
            if(k+l>9)
                continue;
            temp.joins = k;
            temp.limit = l;
            abc.push_back(temp);
        }
    }
    return abc;
}


int main(){
    freopen("B.in","r",stdin);
    freopen("output.txt","w",stdout);
    temp.joins = 0;
    for(int i=1;i<=9;i++){
        temp.limit = i;
        defalutval[i].push_back(temp);
    }
    temp.joins = 1;
    temp.limit = 2;
    defalutval[4].push_back(temp);
    temp.limit = 3;
    defalutval[5].push_back(temp);
    defalutval[6].push_back(temp);
    temp.limit = 4;
    defalutval[7].push_back(temp);
    defalutval[8].push_back(temp);
    temp.limit = 5;
    defalutval[9].push_back(temp);
    temp.joins = 2;
    temp.limit = 3;
    defalutval[9].push_back(temp);
    int TC;
    cin>>TC;
    for(int ZZ = 1;ZZ<=TC;ZZ++){
        int d;
        cin>>d;
        int ar[d];
        for(int i=0;i<d;i++)
            cin>>ar[i];
        sort(ar,ar+d);
        vector <Node> ans = getans(ar,d);
        int ans1 = 1000;
        for(int i=0;i<ans.size();i++){
            ans1 = min(ans1,ans[i].limit+ans[i].joins);
        }
        cout<<"Case #"<<ZZ<<": "<<ans1<<endl;
    }
    return 0;
}
