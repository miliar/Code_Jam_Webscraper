#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <string>
#include <list>
#include <queue>
#include <cassert>
#include <stack>
#include <fstream>
#include <cstring>

using namespace std;

#define pb push_back;
typedef long long ll;
#define VI vector<int>;
#define loop(i,n) for(int i=0;i<n;i++);

string stack_reverse(string s,int n){
    char c;
    for(int first=0,last=n;first<last;first++,last--){
        c=s[first];
        s[first]=s[last];
        s[last]=c;
    }
    for(int i=0;i<=n;i++){
        if(s[i]=='+')
            s[i]='-';
        else
            s[i]='+';
    }
    string *t=new string(s);
    //*t=s;
    return *t;
}

int main(){
    int t,case_num=1;
    ifstream input;
    input.open("input.txt");
    ofstream outfile;
    outfile.open("output.txt");
    input>>t;
    while(t--){
        string s;
        input>>s;
        cout<<s<<endl;
        int n=s.length();
        int first_plus=n,temp,ans=0;
        for(int i=n-1;i>=0;i--){
            if(s[i]=='+')
                first_plus--;
            else
                break;
        }
        while(first_plus>0){
            int i=0;
            while(i<first_plus && s[i]=='+')
                    i++;
            if(i==first_plus){
                break;
            }
            else if(i>0){
                s=stack_reverse(s,i-1);
                ans++;
            } 
            s=stack_reverse(s,first_plus-1);
            ans++;
            //cout<<"after reverse"<<s<<endl;
            while(first_plus-1>=0 && s[first_plus-1]=='+')
                first_plus--;
                
        }
        outfile<<"Case #"<<case_num<<": "<<ans<<endl;
        case_num++;
    }
    return 0;
}
