#include<bits/stdc++.h>
#include<iostream>
#include<string>
using namespace std;
int main()
{
    FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
    string s;
    int i,j,tt;
    cin>>tt;
    for(i=1; i<=tt; i++)
    {
        int moves = 0;
        char current = '+';
        cin>>s;
        for(int j = s.size()-1;j>=0;j--) {
            if(s[j]!=current) {
                moves++;
                current = (current=='+'?'-':'+');
            }
        }
         cout<<"Case #"<<i<<": "<<moves<<"\n";
    }
    return 0;
}
