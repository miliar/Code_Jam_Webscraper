#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string cakes;
char x,p='+', m='-';

void swap(int n) {
    int i;
    if(cakes[0]==p)
        x=m;
    else
        x=p;
    for(i=0;i<=n;i++)
        cakes[i]=x;
}
int main()
{

    FILE *fin = freopen("B-large.in", "r", stdin);
    FILE *fout = freopen("B-large.out", "w", stdout);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i,j=0,t,count;
    cin>>t;
    while(t--){
        cin>>cakes;
        j++;
        count=0;
        for(i=1;i<cakes.length();i++){
            if(cakes[i-1]!=cakes[i]){
                swap(i-1);
                count++;
            }
        }
        if(cakes[0]==m)
            count++;
        cout<<"Case #"<<j<<": "<<count<<endl;
    }
    return 0;
}