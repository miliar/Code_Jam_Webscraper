#include <iostream>

using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    int t,j,k,l,a[26];
    cin>>t;
    int arr[10];
    for(int x=1;x<=t;x++){
        string s;
        cin>>s;
        l=s.size();
        for(j=0;j<10;j++){
            arr[j]=0;
        }
        for(j=0;j<26;j++){
            a[j]=0;
        }
        for(j=0;j<l;j++){
            a[s[j]-'A']++;
        }
        if(a['Z'-'A']!=0){
            arr[0]=a['Z'-'A'];
            a['E'-'A']=a['E'-'A']-a['Z'-'A'];
            a['R'-'A']=a['R'-'A']-a['Z'-'A'];
            a['O'-'A']=a['O'-'A']-a['Z'-'A'];
            a['Z'-'A']=0;
        }
        if(a['W'-'A']!=0){
            arr[2]=a['W'-'A'];
            a['T'-'A']=a['T'-'A']-a['W'-'A'];
            a['O'-'A']=a['O'-'A']-a['W'-'A'];
            a['W'-'A']=0;
        }
        if(a['U'-'A']!=0){
            arr[4]=a['U'-'A'];
            a['F'-'A']=a['F'-'A']-a['U'-'A'];
            a['O'-'A']=a['O'-'A']-a['U'-'A'];
            a['R'-'A']=a['R'-'A']-a['U'-'A'];
            a['U'-'A']=0;
        }
        if(a['X'-'A']!=0){
            arr[6]=a['X'-'A'];
            a['S'-'A']=a['S'-'A']-a['X'-'A'];
            a['I'-'A']=a['I'-'A']-a['X'-'A'];
            a['X'-'A']=0;
        }
        if(a['G'-'A']!=0){
            arr[8]=a['G'-'A'];
            a['E'-'A']=a['E'-'A']-a['G'-'A'];
            a['I'-'A']=a['I'-'A']-a['G'-'A'];
            a['H'-'A']=a['H'-'A']-a['G'-'A'];
            a['T'-'A']=a['T'-'A']-a['G'-'A'];
            a['G'-'A']=0;
        }
        if(a['T'-'A']!=0){
            arr[3]=a['T'-'A'];
            a['H'-'A']=a['H'-'A']-a['T'-'A'];
            a['R'-'A']=a['R'-'A']-a['T'-'A'];
            a['E'-'A']=a['E'-'A']-a['T'-'A'];
            a['E'-'A']=a['E'-'A']-a['T'-'A'];
            a['T'-'A']=0;
        }
        if(a['O'-'A']!=0){
            arr[1]=a['O'-'A'];
            a['N'-'A']=a['N'-'A']-a['O'-'A'];
            a['E'-'A']=a['E'-'A']-a['O'-'A'];
            a['O'-'A']=0;
        }
        if(a['S'-'A']!=0){
            arr[7]=a['S'-'A'];
            a['V'-'A']=a['V'-'A']-a['S'-'A'];
            a['N'-'A']=a['N'-'A']-a['S'-'A'];
            a['E'-'A']=a['E'-'A']-2*a['S'-'A'];
            a['S'-'A']=0;
        }
        if(a['F'-'A']!=0){
            arr[5]=a['F'-'A'];
            a['I'-'A']=a['I'-'A']-a['F'-'A'];
            a['V'-'A']=a['V'-'A']-a['F'-'A'];
            a['E'-'A']=a['E'-'A']-a['F'-'A'];
            a['F'-'A']=0;
        }
        if(a['I'-'A']!=0){
            arr[9]=a['I'-'A'];
            a['N'-'A']=a['N'-'A']-2*a['I'-'A'];
            a['E'-'A']=a['E'-'A']-a['I'-'A'];
            a['N'-'A']=0;
        }
        cout<<"Case #"<<x<<": ";
        for(j=0;j<10;j++){
            if(arr[j]!=0){
                for(k=0;k<arr[j];k++){
                    cout<<j;
                }
            }
        }
        cout<<endl;
    }
    return 0;
}

