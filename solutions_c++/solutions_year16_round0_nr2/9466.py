#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<vector>
#include<utility>
#include<cstring>
#include<fstream>

#define pb push_back
#define po pop_back
#define fs first
#define sc second
#define INF 999999999

using namespace std;
int n,i,j;
string a;
char lastChar;
int noOfPlus,result;

bool check(string s){
    for (int i=0; i<s.size(); i++)
        if(s[i]=='-')
            return false;
    return true;
}

int make(string s){
    if(check(s))
        return 0;
    for(int i=0;i<s.size()-1;i++){
        while(s[i]==s[i+1]&&i+1<s.size())
            s.erase(i+1,1);
    }
    int nrOfMin=0;
    for(int i=1;i<s.size();i++)
        if(s[i]=='-')
            nrOfMin++;
    if(s[0]=='-')
        return nrOfMin*2 +1;
    else return nrOfMin*2;
}

int main(){
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    cin.sync_with_stdio(false);
    cin>>n;
    for(i=0;i<n;i++){
        cin>>a;
        cout<<"Case #"<<i+1<<": "<<make(a)<<endl;
    }


    return 0;
}
