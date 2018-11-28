#include <iostream>
#include <string>

using namespace std;

int happy_counter(string s)
{
    if(s=="") return 0;
    int i = s.length() - 1;
    string a="";
    if(s[i]=='+'){
        while(i!=-1 && s[i]=='+') i--;
        if(i==-1) return happy_counter("");
        s.erase(i+1);
        return happy_counter(s); 
    }else{
        while(i!=-1 && s[i]=='-') i--;
        if(i==-1) return happy_counter("") + 1;
        s.erase(i+1);
        for(int i=0;i<s.length();i++){
            if(s[i]=='+') s[i]='-';
            else          s[i]='+';
        }
        return happy_counter(s) + 1;
    }
}

int main()
{
    int t;
    string s;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        cin >> s;
        cout << "Case #" << i << ": " << happy_counter(s) << endl;
    }
    return 0;
}