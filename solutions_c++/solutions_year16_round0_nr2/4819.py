#include <iostream>

using namespace::std;
string s;

string obroc(string s, int ostatni){
string n;
for(int i = ostatni; i >= 0; i--){
    if(s[i]=='+') n+='-';
    else n+='+';
}
for(int i=ostatni+1; i<s.size(); i++){
    n+=s[i];
}
return n;
}


int solve(string s){
int last_minus;
int licznik=0;
    while(true){
        last_minus=-1;
        for(int i=0; i<s.size(); i++){
            if(s[i]=='-') last_minus=i;
        }
        if(last_minus==-1) return licznik;
        s.erase(last_minus+1,s.size()-last_minus-1);
        if(s[0]=='+'){
            int x;
            for(int i=0; i<s.size(); i++){
                if(s[i]=='-'){x=i-1; break;}
            }
        s=obroc(s,x);
        }else{
        s=obroc(s,last_minus);

        }
    licznik++;
    }


}

int main(){
int l;

cin>>l;

for(int i=0; i<l; i++){
    cin>>s;
cout<<"Case #"<<i+1<<": "<<solve(s)<<endl;
}

return 0;
}
