#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        string s;
        int i,x,j,a[3005],b[100];
        cin>>s;
        memset(a,0,sizeof a);
        for(i=0;i<s.size();i++){
            a[s[i]-'A']++;
        }
        printf("Case #%d: ",t);
        x = min(min(a['Z'-'A'],a['E'-'A']),min(a['R'-'A'],a['O'-'A']));
        a['Z'-'A']-=x;
        a['E'-'A']-=x;
        a['R'-'A']-=x;
        a['O'-'A']-=x;
        b[0]=x;
        x = min(min(a['T'-'A'],a['W'-'A']),a['O'-'A']);
        a['T'-'A']-=x;
        a['W'-'A']-=x;
        a['O'-'A']-=x;
        b[2]=x;
        x = min(min(a['F'-'A'],a['O'-'A']),min(a['U'-'A'],a['R'-'A']));
        a['F'-'A']-=x;
        a['O'-'A']-=x;
        a['U'-'A']-=x;
        a['R'-'A']-=x;
        b[4]=x;
        x = min(min(a['S'-'A'],a['I'-'A']),a['X'-'A']);
        a['S'-'A']-=x;
        a['I'-'A']-=x;
        a['X'-'A']-=x;
        b[6]=x;
        x = min(a['T'-'A'],min(min(a['E'-'A'],a['I'-'A']),min(a['G'-'A'],a['H'-'A'])));
        a['E'-'A']-=x;
        a['I'-'A']-=x;
        a['G'-'A']-=x;
        a['H'-'A']-=x;
        a['T'-'A']-=x;
        b[8]=x;
        x = min(min(a['T'-'A'],a['H'-'A']),min(a['R'-'A'],a['E'-'A']/2));
        a['T'-'A']-=x;
        a['H'-'A']-=x;
        a['R'-'A']-=x;
        a['E'-'A']-=2*x;
        b[3]=x;
         x = min(min(a['F'-'A'],a['I'-'A']),min(a['V'-'A'],a['E'-'A']));
        a['F'-'A']-=x;
        a['I'-'A']-=x;
        a['V'-'A']-=x;
        a['E'-'A']-=x;
        b[5]=x;
         x = min(min(a['S'-'A'],a['V'-'A']),min(a['N'-'A'],a['E'-'A']/2));
        a['S'-'A']-=x;
        a['V'-'A']-=x;
        a['N'-'A']-=x;
        a['E'-'A']-=2*x;
        b[7]=x;
        x = min(min(a['O'-'A'],a['N'-'A']),a['E'-'A']);
        a['O'-'A']-=x;
        a['N'-'A']-=x;
        a['E'-'A']-=x;
        b[1]=x;
        x = min(min(a['N'-'A']/2,a['I'-'A']),a['E'-'A']);
        b[9] = x;
        for(i=0;i<=9;i++){
            for(j=0;j<b[i];j++){
                cout<<i;
            }
        }
        cout<<endl;

    }
    return 0;
}
