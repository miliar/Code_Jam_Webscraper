#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("A2.txt", "r", stdin);
    freopen("A2out.txt", "w", stdout);
    ios::sync_with_stdio(false); cin.tie(0);
    int t;
    cin>>t;
    for(int T=1 ; T<=t ; ++T){
        cout<<"Case #"<<T<<": ";
        string st;
        cin>>st;
        vector<int> c(100, 0);
        for(int i=0 ; i<st.size() ; ++i)
            c[st[i]-'A']++;
        vector<int> ans(100, 0);
        ans[0] += c['z'-'a'];
        //cout<<"Added to 0 "<<c['z'-'a']<<endl;;
        c['e'-'a'] -= c['z'-'a'];
        c['r'-'a'] -= c['z'-'a'];
        c['o'-'a'] -= c['z'-'a'];
        c['z'-'a'] -= c['z'-'a'];
        ans[2] += c['w'-'a'];
        //cout<<"Added to 2 "<<c['w'-'a']<<endl;;
        c['t'-'a'] -= c['w'-'a'];
        c['o'-'a'] -= c['w'-'a'];
        c['w'-'a'] -= c['w'-'a'];
        ans[4] += c['u'-'a'];
        c['f'-'a'] -= c['u'-'a'];
        c['o'-'a'] -= c['u'-'a'];
        c['r'-'a'] -= c['u'-'a'];
        c['u'-'a'] -= c['u'-'a'];
        ans[5] += c['f'-'a'];
        c['i'-'a'] -= c['f'-'a'];
        c['v'-'a'] -= c['f'-'a'];
        c['e'-'a'] -= c['f'-'a'];
        c['f'-'a'] -= c['f'-'a'];
        ans[6] += c['x'-'a'];
        c['s'-'a'] -= c['x'-'a'];
        c['i'-'a'] -= c['x'-'a'];
        c['x'-'a'] -= c['x'-'a'];
        ans[7] += c['v'-'a'];
        c['s'-'a'] -= c['v'-'a'];
        c['e'-'a'] -= c['v'-'a'];
        c['e'-'a'] -= c['v'-'a'];
        c['n'-'a'] -= c['v'-'a'];
        c['v'-'a'] -= c['v'-'a'];
        ans[8] += c['g'-'a'];
        c['e'-'a'] -= c['g'-'a'];
        c['i'-'a'] -= c['g'-'a'];
        c['h'-'a'] -= c['g'-'a'];
        c['t'-'a'] -= c['g'-'a'];
        c['g'-'a'] -= c['g'-'a'];
        ans[9] += c['i'-'a'];
        c['n'-'a'] -= c['i'-'a'];
        c['n'-'a'] -= c['i'-'a'];
        c['e'-'a'] -= c['i'-'a'];
        c['i'-'a'] -= c['i'-'a'];
        while(c['o'-'a']>0&&c['n'-'a']>0&&c['e'-'a']>0){
            c['o'-'a']--;
            c['n'-'a']--;
            c['e'-'a']--;
            ans[1]++;
            //cout<<"Add to 1"<<endl;
        }
        while(c['t'-'a']>0&&c['h'-'a']>0&&c['e'-'a']>1&&c['r'-'a']>0){
            c['t'-'a']--;
            c['h'-'a']--;
            c['e'-'a']-=2;
            c['r'-'a']--;
            ans[3]++;
        }
        /*while(c['f'-'a']>0&&c['o'-'a']>0&&c['u'-'a']>0&&c['r'-'a']>0){
            c['f'-'a']--;
            c['o'-'a']--;
            c['u'-'a']--;
            c['r'-'a']--;
            cout<<4;
        }
        while(c['f'-'a']>0&&c['i'-'a']>0&&c['v'-'a']>0&&c['e'-'a']>0){
            c['f'-'a']--;
            c['i'-'a']--;
            c['e'-'a']--;
            c['v'-'a']--;
            cout<<5;
        }while(c['s'-'a']>0&&c['i'-'a']>0&&c['x'-'a']>0){
            c['s'-'a']--;
            c['i'-'a']--;
            c['x'-'a']--;
            cout<<6;
        }while(c['s'-'a']>0&&c['n'-'a']>0&&c['v'-'a']>0&&c['e'-'a']>1){
            c['s'-'a']--;
            c['v'-'a']--;
            c['n'-'a']--;
            c['e'-'a']-=2;
            cout<<7;
        }
        while(c['e'-'a']>0&&c['i'-'a']>0&&c['g'-'a']>0&&c['h'-'a']>0&&c['t'-'a']>0){
            c['e'-'a']--;
            c['i'-'a']--;
            c['g'-'a']--;
            c['h'-'a']--;
            c['t'-'a']--;
            cout<<8;
        }while(c['n'-'a']>1&&c['i'-'a']>0&&c['e'-'a']>0){
            c['i'-'a']--;
            c['n'-'a']-=2;
            c['e'-'a']--;
            cout<<9;
        }*/
        for(int i=0 ; i<26 ; ++i){
            //cout<<c[i]<<" ";
            while(ans[i]>0){
                cout<<i;
                ans[i]--;
            }
        }
        cout<<"\n";
    }
}
