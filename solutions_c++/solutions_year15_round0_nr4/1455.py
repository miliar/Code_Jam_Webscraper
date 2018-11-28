#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<fstream>
#include<cstring>
#include<stack>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<queue>
#define ll long long int
using namespace std;
int main()
{
    ifstream cin;
	ofstream cout;
	cin.open("C:\\Users\\Admin\\Downloads\\2.in");
	cout.open("C:\\Users\\Admin\\Downloads\\out.txt");
    ll t,v=1;
    cin>>t;
    while(t--){
        ll x,r,c;
        cin>>x>>r>>c;
        ll check=x-1;
        string s;
        if((r*c)%x==0){
            if(check>r||check>c){
                s="RICHARD";
            }
            else
                s="GABRIEL";
        }
        else
            s="RICHARD";
        cout<<"Case #"<<v++<<": "<<s<<endl;
    }
    return 0;
}
