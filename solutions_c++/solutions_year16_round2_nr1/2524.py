#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("ans3.txt","w",stdout);
    int t;
    cin>>t;
    for(int h=1;h<=t;h++){
        string s;
        cin>>s;
        cout<<"Case #"<<h<<": ";
        int a[26];
        fill(a,a+26,0);
        for(int i=0;i<s.length();i++){
            int x=s[i]-65;
            a[x]++;
        }
        int n[10];
        n[0]=a[25];
        n[2]=a[22];
        n[8]=a[6];
        n[6]=a[23];
        n[3]=a[7]-n[8];
        n[4]=a[17]-n[3]-n[0];
        n[1]=a[14]-n[0]-n[4]-n[2];


        n[7]=a[18]-n[6];
        n[5]=a[21]-n[7];

        n[9]=(a[13]-n[7]-n[1])/2;
        for(int i=0;i<=9;i++){
            if(n[i]!=0){
                for(int j=0;j<n[i];j++){
                    cout<<i;
                }
            }
        }
        cout<<endl;
    }
    return 0;
}
