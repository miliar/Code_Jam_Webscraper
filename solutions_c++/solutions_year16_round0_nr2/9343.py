#include<bits/stdc++.h>
using namespace std;

string str,_str;
int main(){
//freopen("input.txt", "r", stdin);
//freopen("output.txt","w",stdout);
int t;
cin>>t;

for(int i=1;i<=t;i++)
{
    cin>>str;
    int count = 0;
    int r = str.length()-1;
    while(str[r] == '+')
        str.erase(str.begin()+r--);
    r = str.length();
    _str  = "";
    for(int j = 0; j < r; j++)
        _str += '+';
    while(str != _str)
    {
        int l = 0;
        if(str[l] == '-')
        {
            while(str[l] == '-')
                str[l++] = '+';
            count++;
        }
        else
        {
            while(str[l] == '+')
                str[l++] = '-';
            count++;
        }
    }
    cout<<"Case #"<<i<<": "<<count<<endl;
}

return 0;}
