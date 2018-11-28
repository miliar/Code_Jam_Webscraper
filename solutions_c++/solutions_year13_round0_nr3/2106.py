#include<iostream>
#include<cstring>
#include<vector>
#include<cstdio>
#include<sstream>
#include<algorithm>
#include<cmath>
#include<set>
#include<map>
using namespace std;
vector<string>v;

bool mayorigual(string a,string b){
    if(a.size()!=b.size())return a.size()>b.size();
    return a>=b;
}

bool mayor(string a,string b){
    if(a.size()!=b.size())return a.size()>b.size();
    return a>b;
}    

int toi(string s){
    istringstream is(s);
    int t;
    is>>t;
    return t;
}

int main(){
    
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    string s;
    while(cin>>s){
        if(s[0]=='v'){
            string h="";
            for(int i=0;i<s.size();i++)
                if(isdigit(s[i])){
                    h+=s[i];
                }
            v.push_back(h);
        }else{
            
            int tc=toi(s);
            
            for(int caso=1;caso<=tc;caso++){
                cout<<"Case #"<<caso<<": ";
                string a,b;
                cin>>a>>b;
                
                int low=0;int hi=v.size();
                for(int i=0;i<30;i++){
                    int me=(low+hi)/2;
                    if( mayor(v[me],b) )hi=me;
                    else low=me;        
                }
                
                int ind=low;
                
                low=0;hi=v.size();
                
                for(int i=0;i<30;i++){
                    int me=(low+hi)/2;
                    if( mayorigual(v[me],a) )hi=me;
                    else low=me+1;        
                }
                
                cout<<ind-low+1<<endl;
                
            }
    
               
            
        }      
    }
    
    /*
    string s;
    while(cin>>s){
        string s2="";
        for(int i=0;i<s.size();i++)
            if(isdigit(s[i]))
                s2+=s[i];
        dev+=s2+"-";
    }
    
    cout<<dev<<endl;
    */
    
    
    return 0;
}
