#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin>>t;
    string s;

    for(int k=1;k<=t;k++)
    {

        int arr[27]={};
        cin>>s;
        cout<<"Case #"<<k<<": ";
        int z=s.size();
        for(int i=0;i<z;i++)
        {
            arr[s[i]-'A']++;
        }

       int a[10]={};
       a[8]=arr['G'-'A'];  arr['I'-'A']-=a[8]; arr['E'-'A']-=a[8]; arr['H'-'A']-=a[8];  arr['T'-'A']-=a[8];
       a[0]=arr['Z'-'A']; arr['E'-'A']-=a[0]; arr['R'-'A']-=a[0]; arr['O'-'A']-=a[0];
       a[2]=arr['W'-'A']; arr['T'-'A']-=a[2]; arr['O'-'A']-=a[2];
       a[4]=arr['U'-'A']; arr['F'-'A']-=a[4]; arr['O'-'A']-=a[4]; arr['R'-'A']-=a[4];
       a[6]=arr['X'-'A']; arr['I'-'A']-=a[6]; arr['S'-'A']-=a[6];
       a[5]=arr['F'-'A'];  arr['I'-'A']-=a[5]; arr['V'-'A']-=a[5]; arr['E'-'A']-=a[5];
        a[7]=arr['V'-'A'];  arr['E'-'A']-=2*a[7]; arr['S'-'A']-=a[7]; arr['N'-'A']-=a[7];
        a[3]=arr['T'-'A'];  arr['E'-'A']-=2*a[3]; arr['H'-'A']-=a[3]; arr['R'-'A']-=a[3];
       a[9]=arr['I'-'A'];   arr['N'-'A']-=2*a[9]; arr['E'-'A']-=a[9];
       a[1]=arr['N'-'A'];
       for(int i=0;i<=9;i++)while(a[i]--) cout<<i;
       cout<<endl;
    }
	return 0;
}
