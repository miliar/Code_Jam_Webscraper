#include<bits/stdc++.h>
using namespace std;
#define read freopen("A-large.in","r",stdin)
#define write freopen("output2.txt","w",stdout)

string str;
vector<int>ans;

int main(){
    read;
    write;
    int T, caseno=1;
    scanf("%d", &T);
    while(T--){
        cin>>str;
        int len=str.size();

        //check Zero
        int cnt=0;
        for(int i=0; i<len; i++){
            if(str[i]=='Z') cnt++;
        }
        if(cnt){
            for(int i=0; i<cnt; i++) ans.push_back(0);
            int z=0, e=0, r=0, o=0;
            for(int i=0; i<len; i++){
                if(str[i]=='Z' && z<cnt){
                    str[i]=' ';
                    z++;
                }
                else if(str[i]=='E' && e<cnt){
                    str[i]=' ';
                    e++;
                }
                else if(str[i]=='R' && r<cnt){
                    str[i]=' ';
                    r++;
                }
                else if(str[i]=='O' && o<cnt){
                    str[i]=' ';
                    o++;
                }
            }
        }

        //check two
        cnt=0;
        for(int i=0; i<len; i++){
            if(str[i]=='W') cnt++;
        }
        if(cnt){
            for(int i=0; i<cnt; i++) ans.push_back(2);
            int t=0, o=0, w=0;
            for(int i=0; i<len; i++){
                if(str[i]=='T' && t<cnt){
                    str[i]=' ';
                    t++;
                }
                else if(str[i]=='O' && o<cnt){
                    str[i]=' ';
                    o++;
                }
                else if(str[i]=='W' && w<cnt){
                    str[i]=' ';
                    w++;
                }
            }
        }

        //check Four
        cnt=0;
        for(int i=0; i<len; i++){
            if(str[i]=='U') cnt++;
        }
        if(cnt){
            for(int i=0; i<cnt; i++) ans.push_back(4);
            int f=0, o=0, u=0, r=0;
            for(int i=0; i<len; i++){
                if(str[i]=='F' && f<cnt){
                    str[i]=' ';
                    f++;
                }
                else if(str[i]=='O' && o<cnt){
                    str[i]=' ';
                    o++;
                }
                else if(str[i]=='U' && u<cnt){
                    str[i]=' ';
                    u++;
                }
                else if(str[i]=='R' && r<cnt){
                    str[i]=' ';
                    r++;
                }
            }
        }

        //check Six
        cnt=0;
        for(int i=0; i<len; i++){
            if(str[i]=='X') cnt++;
        }
        if(cnt){
            for(int i=0; i<cnt; i++) ans.push_back(6);
            int s=0, ii=0, x=0;
            for(int i=0; i<len; i++){
                if(str[i]=='S' && s<cnt){
                    str[i]=' ';
                    s++;
                }
                else if(str[i]=='I' && ii<cnt){
                    str[i]=' ';
                    ii++;
                }
                else if(str[i]=='X' && x<cnt){
                    str[i]=' ';
                    x++;
                }
            }
        }

        //check Eight
        cnt=0;
        for(int i=0; i<len; i++){
            if(str[i]=='G') cnt++;
        }
        if(cnt){
            for(int i=0; i<cnt; i++) ans.push_back(8);
            int e=0, ii=0, g=0, h=0, t=0;
            for(int i=0; i<len; i++){
                if(str[i]=='E' && e<cnt){
                    str[i]=' ';
                    e++;
                }
                else if(str[i]=='I' && ii<cnt){
                    str[i]=' ';
                    ii++;
                }
                else if(str[i]=='G' && g<cnt){
                    str[i]=' ';
                    g++;
                }
                else if(str[i]=='H' && h<cnt){
                    str[i]=' ';
                    h++;
                }
                else if(str[i]=='T' && t<cnt){
                    str[i]=' ';
                    t++;
                }
            }
        }

        // check one
        cnt=0;
        for(int i=0; i<len; i++){
            if(str[i]=='O') cnt++;
        }
        if(cnt){
            for(int i=0; i<cnt; i++) ans.push_back(1);
            int o=0, n=0, e=0;
            for(int i=0; i<len; i++){
                if(str[i]=='O' && o<cnt){
                    str[i]=' ';
                    o++;
                }
                else if(str[i]=='N' && n<cnt){
                    str[i]=' ';
                    n++;
                }
                else if(str[i]=='E' && e<cnt){
                    str[i]=' ';
                    e++;
                }
            }
        }

        // check three
        cnt=0;
        for(int i=0; i<len; i++){
            if(str[i]=='T') cnt++;
        }
        if(cnt){
            for(int i=0; i<cnt; i++) ans.push_back(3);
            int t=0, h=0, r=0, e=0;
            for(int i=0; i<len; i++){
                if(str[i]=='T' && t<cnt){
                    str[i]=' ';
                    t++;
                }
                else if(str[i]=='H' && h<cnt){
                    str[i]=' ';
                    h++;
                }
                else if(str[i]=='R' && r<cnt){
                    str[i]=' ';
                    r++;
                }
                else if(str[i]=='E' && e<(2*cnt)){
                    str[i]=' ';
                    e++;
                }
            }
        }

        // check Five
        cnt=0;
        for(int i=0; i<len; i++){
            if(str[i]=='F') cnt++;
        }
        if(cnt){
            for(int i=0; i<cnt; i++) ans.push_back(5);
            int f=0, ii=0, v=0, e=0;
            for(int i=0; i<len; i++){
                if(str[i]=='F' && f<cnt){
                    str[i]=' ';
                    f++;
                }
                else if(str[i]=='I' && ii<cnt){
                    str[i]=' ';
                    ii++;
                }
                else if(str[i]=='V' && v<cnt){
                    str[i]=' ';
                    v++;
                }
                else if(str[i]=='E' && e<cnt){
                    str[i]=' ';
                    e++;
                }
            }
        }

        // check Seven
        cnt=0;
        for(int i=0; i<len; i++){
            if(str[i]=='S') cnt++;
        }
        if(cnt){
            for(int i=0; i<cnt; i++) ans.push_back(7);
            int s=0, e=0, v=0, n=0;
            for(int i=0; i<len; i++){
                if(str[i]=='S' && s<cnt){
                    str[i]=' ';
                    s++;
                }
                else if(str[i]=='E' && e<(2*cnt)){
                    str[i]=' ';
                    e++;
                }
                else if(str[i]=='V' && v<cnt){
                    str[i]=' ';
                    v++;
                }
                else if(str[i]=='N' && n<cnt){
                    str[i]=' ';
                    n++;
                }
            }
        }

        // check NINE
        cnt=0;
        for(int i=0; i<len; i++){
            if(str[i]=='I') cnt++;
        }
        if(cnt){
            for(int i=0; i<cnt; i++) ans.push_back(9);
            int n=0, i=0, e=0;
            for(int i=0; i<len; i++){
                if(str[i]=='N' && n<(2*cnt)){
                    str[i]=' ';
                    n++;
                }
                else if(str[i]=='I' && i<cnt){
                    str[i]=' ';
                    i++;
                }
                else if(str[i]=='E' && e<cnt){
                    str[i]=' ';
                    e++;
                }
            }
        }

        sort(ans.begin(),ans.end());
        printf("Case #%d: ", caseno++);
        for(int i=0; i<ans.size(); i++){
            printf("%d", ans[i]);
        }
        printf("\n");
        ans.clear();
    }
    return 0;
}

