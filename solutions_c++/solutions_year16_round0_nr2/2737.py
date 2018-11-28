#include <iostream>
#include <cstring>
#include <queue>
using namespace std;
typedef long long ll;
int hsh(string s){
    int h=0;
    for (int i=0;i<s.size();i++){
       if (s[i]=='-') h+=(1<<i);
    }
    return h;
}
string flip(string s){
    string fin="";
    for (int i=s.size()-1;i>=0;i--) fin+=s[i];
    return fin;
}
string inv(string s){
    string ans="";
    for (int i=0;i<s.size();i++){
        if (s[i]=='+') ans+='-';
        else ans+='+';
    }
    return ans;
}
int dist[2050];
bool visited[2050];
int main(){
    //basically BFS from the given stack and try to reach final (hashed=0), min dist?
    //For small test case, hash the string ez
    int t;
    cin>>t;
    for (int ca=1;ca<=t;ca++){
        memset(dist,0x3f,sizeof dist);
        memset(visited,false,sizeof visited);
        string s;
        cin>>s;
        queue<string> q;
        q.push(s);
        dist[hsh(s)]=0;
        while (!q.empty()){
            string here=q.front();
            int now=hsh(here);
            visited[now]=true;
            //cout<<now<<':'<<endl;
            q.pop();
            for (int i=1;i<=s.size();i++){
                string pos=inv(flip(here.substr(0,i)))+here.substr(i,s.size()-i);
                //cout<<pos<<endl;
                int nex=hsh(pos);
                //try nex
                if (!visited[nex]){
                    q.push(pos);
                    visited[nex]=true;
                    dist[nex]=dist[now]+1;
                }
            }
        }
        cout<<"Case #"<<ca<<": "<<dist[0]<<endl;
    }
}