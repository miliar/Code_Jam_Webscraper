#include<bits/stdc++.h>
using namespace std;

int t, ca,len;
string s;
deque<char>q;
int main(){
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);

    //scanf("%d ",&t);
    cin>>t;
    for(ca=1;ca<=t;ca++){
        //scanf("%s",&s);
        cin>>s;
        len = s.length();
        while(!q.empty())q.pop_front();
        q.push_front(s[0]);
        for(int i = 1; i<len;i++){
           // cout<<"s:"<<s[i]<<"\tf:"<<q.front();
            if(s[i]<q.front()){
                q.push_back(s[i]);
            }
            else{
                q.push_front(s[i]);
            }
        }

        cout<<"Case #"<<ca<<": ";
        while(!q.empty()){
            cout<<q.front();
            q.pop_front();
        }
        cout<<"\n";
    }



    return 0;
}
