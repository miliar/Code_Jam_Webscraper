#include <bits/stdc++.h>
using namespace std;

bool isCorrect(vector<bool>& v){
    for(int i=0;i<v.size();i++){
        if (v[i]==0)
            return false;
    }
    return true;
}

int flipper(vector<bool>& v, int top){
    vector<bool> tmp=v;
    for(int i=0;i<=top;i++){
        v[i]=(tmp[top-i]+1)%2;
    }
    if (v[top]==0){
        v[top]=1;
        return 2;
    }
    else return 1;
}

int main(){
    freopen("B-large.in","r",stdin); freopen("00_output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int tc=1;tc<=t;tc++){
        char s[105];
        scanf("%s",s);
        int flips=0;
        int sLen=strlen(s);
        vector<bool> v;
        for(int i=0;i<sLen;i++){

            if (s[i]=='+')
                v.push_back(1);
            else v.push_back(0);
        }
       // cout<<"len of v = "<<v.size()<<endl;
        for(int i=sLen-1;i>=0;i--){
             if (!isCorrect(v)){
                for(int j=0;j<=i;j++){
                    if (v[j]==0){
                        if (j>0)
                        flips++;
                        break;
                    }
                    else if (v[j]==1){
                        v[j]=0;
                    }
                }
            }

           if (v[i]==0){
               /* for(int j=0;j<sLen;j++){
                cout<<v[j];
            }
           cout<<endl;*/
            flips+=flipper(v,i);
           }

        }
        printf("Case #%d: %d\n",tc,flips);
    }
}
