#include <bits/stdc++.h>
using namespace std;
unordered_map<char ,int > myMap;
char number[11][11];
int actual[11];
int l[11];
vector<int> ans;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out-large.txt","w",stdout);
    int T;
    scanf("%d",&T);
    strcpy(number[0],"ZERO");
    actual[0] = 0;
    strcpy(number[8],"ONE");
    actual[8] = 1;
    strcpy(number[7],"TWO");
    actual[7] = 2;
    strcpy(number[9],"THRE"); // E
    actual[9] = 3;
    strcpy(number[1],"FOUR");
    actual[1] = 4;
    strcpy(number[4],"FIVE");
    actual[4] = 5;
    strcpy(number[2],"SIX");
    actual[2] = 6;
    strcpy(number[5],"SEVN"); // E
    actual[5] = 7;
    strcpy(number[3],"EIGHT");
    actual[3] = 8;
    strcpy(number[6],"NIE"); // N
    actual[6] = 9;
    for(int i=0;i<10;i++){
        l[i] = strlen(number[i]);
    }
    for(int t=1;t<=T;t++){
        char text[30000];
        scanf("%s",&text);
        int len = strlen(text);
        for(int i=0;i<len;i++){
            myMap[text[i]]++;
        }
        for(int i=0;i<10;i++){
                int mini = 1000000;
                int stop = 0;
                for(int j=0;j<l[i];j++){
                    if(myMap.find(number[i][j])!=myMap.end()){
                        int hold = myMap[number[i][j]];
                        if(((actual[i]==3||actual[i]==7)&&number[i][j]=='E')||(actual[i]==9&&number[i][j]=='N')){
                            hold = hold/2;
                        }
                        mini = min(mini,hold);
                    }else{
                        mini = 0;
                    }
                }
                if(mini==0)continue;
                for(int j=0;j<l[i];j++){
                    if(((actual[i]==3||actual[i]==7)&&number[i][j]=='E')||(actual[i]==9&&number[i][j]=='N')){
                        if(myMap[number[i][j]] == mini*2){
                            myMap.erase(number[i][j]);
                        }else{
                            myMap[number[i][j]] -= mini*2;
                        }
                    }else{
                        if(myMap[number[i][j]]==mini){
                            myMap.erase(number[i][j]);
                        }else{
                            myMap[number[i][j]] -= mini;
                        }
                    }
                }
                for(;mini>0;mini--){
                    ans.push_back(actual[i]);
                }
        }
        sort(ans.begin(),ans.end());
        printf("Case #%d: ",t);
        for(int i=0;i<ans.size();i++){
            printf("%d",ans[i]);
        }
        printf("\n");
        myMap.clear();
        ans.clear();
}
    return 0;
}

