#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <valarray>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    FILE *fin = freopen("A-large.in", "r", stdin);
    FILE *fout = freopen("A-large.out", "w", stdout);
    int i,j=0,k,t,n,len;
    string s;
    cin>>t;
    while(t--){
    	j++;
        cin>>s;
        len = s.length();
        int chars[len]={0};
        chars[0]=(int) s[0];
        for(i=1;i<len;i++){
            n = (int)s[i];
            if(n < chars[0])
                chars[i] = n;
            else{
                for(k=i-1;k>=0;k--){
                    chars[k+1] = chars[k];
                }
                chars[0] = n;
            }
        }
        cout<<"Case #"<<j<<": ";
        for(i=0;i<len;i++)
            cout<<(char) chars[i];
        cout<<endl;
    }
    return 0;
}
