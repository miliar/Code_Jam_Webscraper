#include <bits/stdc++.h>
using namespace std;

int main() {
    long long i,t;
    string ar;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        vector<int> s(26,0);
        vector<int> num(10,0);
        cin>>ar;
        for(long long j=0;j<ar.length();j++)
            s[ar[j]-65]++;
        if(s[25])
        {
            num[0]=s[25];
            s[4]-=s[25];
            s[17]-=s[25];
            s[14]-=s[25];
            s[25]-=s[25];
        }
        if(s[22])
        {
            num[2]=s[22];
            s[19]-=s[22];
            s[14]-=s[22];
            s[22]=0;
        }
        if(s[20])
        {
            num[4]=s[20];
            s[5]-=s[20];
            s[14]-=s[20];
            s[17]-=s[20];
            s[20]=0;
        }
        if(s[23])
        {
            num[6]=s[23];
            s[18]-=s[23];
            s[8]-=s[23];
            s[23]=0;
        }
        if(s[6])
        {
            num[8]=s[6];
            s[4]-=s[6];
            s[8]-=s[6];
            s[7]-=s[6];
            s[19]-=s[6];
            s[6]=0;
        }
        if(s[14])
        {
            num[1]=s[14];
            s[13]-=s[14];
            s[4]-=s[14];
            s[14]=0;
        }
        if(s[7])
        {
            num[3]=s[7];
            s[19]-=s[7];
            s[17]-=s[7];
            s[4]-=2*s[7];
            s[7]=0;
        }
        if(s[5])
        {
            num[5]=s[5];
            s[8]-=s[5];
            s[21]-=s[5];
            s[4]-=s[5];
            s[5]=0;
        }
        if(s[18])
        {
            num[7]=s[18];
        }
        if(s[8])
        {
            num[9]=s[8];
        }
        cout<<"Case #"<<i<<": ";
        for(long long j=0;j<10;j++)
            for(long long k=0;k<num[j];k++)
            cout<<j;
        
        
        cout<<"\n";
    }
	return 0;
}