#include <iostream>

using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    int test,i,j,k,l,a[26];
    string s;
    cin>>test;
    int ans[10];
    for(i=1;i<=test;i++){
        cin>>s;
        l=s.length();
        for(j=0;j<10;j++){
            ans[j]=0;
        }
        for(j=0;j<26;j++){
            a[j]=0;
        }
        for(j=0;j<l;j++){
            a[s[j]-'A']++;
        }
        if(a['Z'-'A']!=0){
            ans[0]=a['Z'-'A'];
            a['E'-'A']=a['E'-'A']-a['Z'-'A'];
            a['R'-'A']=a['R'-'A']-a['Z'-'A'];
            a['O'-'A']=a['O'-'A']-a['Z'-'A'];
            a['Z'-'A']=0;
        }
        if(a['W'-'A']!=0){
            ans[2]=a['W'-'A'];
            a['T'-'A']=a['T'-'A']-a['W'-'A'];
            a['O'-'A']=a['O'-'A']-a['W'-'A'];
            a['w'-'A']=0;
        }
        if(a['U'-'A']!=0){
            ans[4]=a['U'-'A'];
            a['F'-'A']=a['F'-'A']-a['U'-'A'];
            a['O'-'A']=a['O'-'A']-a['U'-'A'];
            a['R'-'A']=a['R'-'A']-a['U'-'A'];
            a['U'-'A']=0;
        }
        if(a['X'-'A']!=0){
            ans[6]=a['X'-'A'];
            a['S'-'A']=a['S'-'A']-a['X'-'A'];
            a['I'-'A']=a['I'-'A']-a['X'-'A'];
            a['X'-'A']=0;
        }
        if(a['G'-'A']!=0){
            ans[8]=a['G'-'A'];
            a['E'-'A']=a['E'-'A']-a['G'-'A'];
            a['I'-'A']=a['I'-'A']-a['G'-'A'];
            a['H'-'A']=a['H'-'A']-a['G'-'A'];
            a['T'-'A']=a['T'-'A']-a['G'-'A'];
            a['G'-'A']=0;
        }
        if(a['T'-'A']!=0){
            ans[3]=a['T'-'A'];
            a['H'-'A']=a['H'-'A']-a['T'-'A'];
            a['R'-'A']=a['R'-'A']-a['T'-'A'];
            a['E'-'A']=a['E'-'A']-a['T'-'A'];
            a['E'-'A']=a['E'-'A']-a['T'-'A'];
            a['T'-'A']=0;
        }
        if(a['O'-'A']!=0){
            ans[1]=a['O'-'A'];
            a['N'-'A']=a['N'-'A']-a['O'-'A'];
            a['E'-'A']=a['E'-'A']-a['O'-'A'];
            a['O'-'A']=0;
        }
        if(a['S'-'A']!=0){
            ans[7]=a['S'-'A'];
            a['V'-'A']=a['V'-'A']-a['S'-'A'];
            a['N'-'A']=a['N'-'A']-a['S'-'A'];
            a['E'-'A']=a['E'-'A']-2*a['S'-'A'];
            a['S'-'A']=0;
        }
        if(a['F'-'A']!=0){
            ans[5]=a['F'-'A'];
            a['I'-'A']=a['I'-'A']-a['F'-'A'];
            a['V'-'A']=a['V'-'A']-a['F'-'A'];
            a['E'-'A']=a['E'-'A']-a['F'-'A'];
            a['F'-'A']=0;
        }
        if(a['I'-'A']!=0){
            ans[9]=a['I'-'A'];
            a['N'-'A']=a['N'-'A']-2*a['I'-'A'];
            a['E'-'A']=a['E'-'A']-a['I'-'A'];
            a['N'-'A']=0;
        }
        cout<<"Case #"<<i<<": ";
        for(j=0;j<10;j++){
            if(ans[j]!=0){
                for(k=0;k<ans[j];k++){
                    cout<<j;
                }
            }
        }
        cout<<endl;
    }
    return 0;
}

