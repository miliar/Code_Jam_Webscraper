#include<bits/stdc++.h>

using namespace std;

int main()
{
    ifstream in("in.in");
    ofstream out("out.out");
    int t,n,sum,req; string s;
    in>>t;
    for(int i=1; i<=t; i++)
    {
        in>>n; in>>s; sum=0; req=0;
        if((s[0]-'0')>0){sum=(s[0]-'0');}
        else{req=1;sum=1;}
        for(int j=1; j<n+1; j++)
        {
           if((s[j]-'0')>0&&sum<j){req+=(j-sum);sum=j;}
           sum+=(s[j]-'0');
        }
        out << "Case #" <<i << ": "<<req<<endl;
    }
    out.close();
    return 0;
}
