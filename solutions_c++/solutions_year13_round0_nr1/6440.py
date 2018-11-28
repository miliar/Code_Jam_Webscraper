#include<iostream>
#include<vector>
using namespace std;
#define push_back pb
int main(){
    int t;
    cin>>t;
    int n=t;
    while(t--){
        vector<int>v;
        cout<<"Case #"<<n-t<<": ";
        string s;
        int draw=1;
        int winx=0;
        int wino=0;
        for(int i=0;i<4;i++){
            cin<<s;
            int test=s.find(".");
            if(test>=0)draw=0;
            v.pb(s);
        }
        for(int i=0;i<4;i++){
            if(v[i]=="XXXT" or v[i]=="XXTX" or v[i]=="XTXX" or v[i]=="TXXX")winx=1;
            if(v[i]=="OOOT" or v[i]=="OOTO" or v[i]=="OTOO" or v[i]=="TOOO")winy=1;
        }
        for(int j=0;j<4;j++){
            int x=0;
            int o=0;
            for(int i=0;i<4;i++){
                if(v[i][j]=='X')x++;
                if(v[i][j]=='O')o++;
                if(v[i][j]=='T')x++,o++;
            }
            if(x==4)winx=1;
            if(o==4)wino=1;
        }
        for(int i=0;i<4;i++){
            int x=0;
            int o=0;
            if(v[i][i]=='X')x++;
            if(v[i][i]=='O')o++;
            if(v[i][i]=='T')x++,o++;
            if(x==4)winx=1;
            if(o==4)wino=1;
        }
        for(int i=0;i<4;i++){
            int x=0;
            int o=0;
            if(v[i][3-i]=='X')x++;
            if(v[i][3-i]=='O')o++;
            if(v[i][3-i]=='T')x++,o++;
            if(x==4)winx=1;
            if(o==4)wino=1;
        }
        if(winx)cout<<"X won\n";
        else if(wino)cout<<"O won\n";
        else if(draw)cout<<"Draw\n";
        else cout<<"Game has not completed\n";
    }
    return 0;
}