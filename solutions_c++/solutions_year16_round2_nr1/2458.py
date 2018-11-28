#include <fstream>

using namespace std;

int main() {
    fstream fin;
    fstream fout;
    fin.open("input.in",ios::in);
    fout.open("output.out",ios::out);
    int t,i;
    fin>>t;
    string s;
    int arr[26],count[10];
    for(int j=1;j<=t;j++)
	{
	    for(i=0;i<10;i++)
            count[i]=0;
        for(i=0;i<26;i++)
            arr[i]=0;
	    fin>>s;
	    fout<<"Case #"<<j<<": ";
	    for(i=0;i<s.size();i++)
            arr[s[i]-'A']++;
        if(arr['W'-'A']>0){
            count[2]=arr['W'-'A'];
            arr['T'-'A']-=arr['W'-'A'];
            arr['O'-'A']-=arr['W'-'A'];
            arr['W'-'A']-=arr['W'-'A'];
        }
        if(arr['Z'-'A']>0){
            count[0]=arr['Z'-'A'];
            arr['E'-'A']-=arr['Z'-'A'];
            arr['O'-'A']-=arr['Z'-'A'];
            arr['R'-'A']-=arr['Z'-'A'];
            arr['Z'-'A']-=arr['Z'-'A'];
        }
        if(arr['X'-'A']>0){
            count[6]=arr['X'-'A'];
            arr['S'-'A']-=arr['X'-'A'];
            arr['I'-'A']-=arr['X'-'A'];
            arr['X'-'A']-=arr['X'-'A'];
        }
        if(arr['G'-'A']>0){
            count[8]=arr['G'-'A'];
            arr['T'-'A']-=arr['G'-'A'];
            arr['E'-'A']-=arr['G'-'A'];
            arr['I'-'A']-=arr['G'-'A'];
            arr['H'-'A']-=arr['G'-'A'];
            arr['G'-'A']-=arr['G'-'A'];
        }
        if(arr['U'-'A']>0){
            count[4]=arr['U'-'A'];
            arr['F'-'A']-=arr['U'-'A'];
            arr['O'-'A']-=arr['U'-'A'];
            arr['R'-'A']-=arr['U'-'A'];
            arr['U'-'A']-=arr['U'-'A'];
        }
        if(arr['S'-'A']>0){
            count[7]=arr['S'-'A'];
            arr['E'-'A']-=arr['S'-'A'];
            arr['N'-'A']-=arr['S'-'A'];
            arr['E'-'A']-=arr['S'-'A'];
            arr['V'-'A']-=arr['S'-'A'];
            arr['S'-'A']-=arr['S'-'A'];
        }
        if(arr['V'-'A']>0){
            count[5]=arr['V'-'A'];
            arr['F'-'A']-=arr['V'-'A'];
            arr['I'-'A']-=arr['V'-'A'];
            arr['E'-'A']-=arr['V'-'A'];
            arr['V'-'A']-=arr['V'-'A'];
        }
        if(arr['I'-'A']>0){
            count[9]=arr['I'-'A'];
            arr['N'-'A']-=arr['I'-'A'];
            arr['N'-'A']-=arr['I'-'A'];
            arr['E'-'A']-=arr['I'-'A'];
            arr['I'-'A']-=arr['I'-'A'];
        }
        if(arr['N'-'A']>0){
            count[1]=arr['N'-'A'];
            arr['E'-'A']-=arr['N'-'A'];
            arr['O'-'A']-=arr['N'-'A'];
            arr['N'-'A']-=arr['N'-'A'];
        }
        if(arr['R'-'A']>0){
            count[3]=arr['R'-'A'];
            arr['T'-'A']-=arr['R'-'A'];
            arr['H'-'A']-=arr['R'-'A'];
            arr['E'-'A']-=arr['R'-'A'];
            arr['E'-'A']-=arr['R'-'A'];
            arr['R'-'A']-=arr['R'-'A'];
        }
        for(i=0;i<10;i++)
            for(int k=0;k<count[i];k++)
            fout<<i;
        fout<<endl;
    }
}
