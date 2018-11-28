#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> let(26, 0); 
vector<int> dit;

int main(){
    int T;      cin>>T;
    for(int i=1; i<=T; ++i){
        string s;   cin>>s;
        int len = s.length();
        //cout<<"got here!"<<endl;
        for(int j=0; j<26; ++j)
            let[j]=0;
        
        for(int j=0; j<len; ++j)
            let[s[j]-'A']++;
        
        dit.clear();
        
        while(let['z'-'a']){
            dit.push_back(0);
            let['z'-'a']--;
            let['e'-'a']--; 
            let['r'-'a']--;
            let['o'-'a']--;
        }
        while(let['w'-'a']){
            dit.push_back(2);
            let['t'-'a']--;  //t
            let['w'-'a']--;  //w
            let['o'-'a']--;  //o
        }
        while(let['u'-'a']){
            dit.push_back(4);
            let['f'-'a']--;  //f
            let['o'-'a']--;   //o
            let['u'-'a']--;  //u
            let['r'-'a']--;  //r
        }
        while(let['x'-'a']){
            dit.push_back(6);
            let['s'-'a']--;
            let['i'-'a']--;
            let['x'-'a']--;
        }
        while(let['g'-'a']){
            dit.push_back(8);
            let['e'-'a']--;
            let['i'-'a']--;
            let['g'-'a']--;
            let['h'-'a']--;
            let['t'-'a']--;
        }
        
        while(let['o'-'a']){
            dit.push_back(1);
            let['o'-'a']--;
            let['n'-'a']--;
            let['e'-'a']--;
        }
        while(let['f'-'a']){
            dit.push_back(5);
            let['f'-'a']--;
            let['i'-'a']--;
            let['v'-'a']--;
            let['e'-'a']--;
        }
        while(let['s'-'a']){
            dit.push_back(7);
            let['s'-'a']--;
            let['e'-'a']--;
            let['v'-'a']--;
            let['e'-'a']--;
            let['n'-'a']--;
        }
        while(let['i'-'a']){
            dit.push_back(9);
            let['n'-'a']--;
            let['i'-'a']--;
            let['n'-'a']--;
            let['e'-'a']--;
        }
        while(let['h'-'a']){
            dit.push_back(3);
            let['t'-'a']--;
            let['h'-'a']--;
            let['r'-'a']--;
            let['e'-'a']--;
            let['e'-'a']--;
        }
        //cout<<"got here!"<<endl;
        sort(dit.begin(), dit.end());
        cout<<"Case #"<<i<<": ";
        for(int j=0; j<dit.size(); ++j)
            cout<<dit[j];
        cout<<endl;
    }
    return 0;
}
