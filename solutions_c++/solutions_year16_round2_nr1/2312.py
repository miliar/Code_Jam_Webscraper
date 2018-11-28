#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int a[27];
vector<int > ans;
int main(){
    
    freopen("jam.txt","r",stdin);
    freopen("jam1.txt","w",stdout);
    
    int n;
    scanf("%d",&n);
    
    for(int i=1;i<=n;i++){
        ans.clear();
        char c[3000];
        scanf("%s",c);
        for(int j=0;c[j]!='\0';j++){
            a[c[j] - 'A']++;
        }
        
        if(a['Z'-'A']>0){
            int x = a['Z'-'A'];
            //printf("***");
            //printf("%d\n",x);
            for(int j=0;j<x;j++){
                ans.push_back(0);
            }
            a['Z' - 'A'] = 0;
            a['E' - 'A'] -= x;
            a['R' - 'A'] -= x;
            a['O' - 'A'] -= x;
            //printf("->%d\n",ans[0]);
        }
        if(a['X'-'A']>0){
            int x = a['X'-'A'];
            for(int j=0;j<x;j++){
                ans.push_back(6);
            }
            a['X' - 'A'] = 0;
            a['S' - 'A'] -= x;
            a['I' - 'A'] -= x;
        }
        if(a['G'-'A']>0){
            int x = a['G'-'A'];
            for(int j=0;j<x;j++){
                ans.push_back(8);
            }
            a['G' - 'A'] = 0;
            a['E' - 'A'] -= x;
            a['I' - 'A'] -= x;
            a['H' - 'A'] -= x;
            a['T' - 'A'] -= x;
        }
        if(a['W'-'A']>0){
            int x = a['W'-'A'];
            for(int j=0;j<x;j++){
                ans.push_back(2);
            }
            a['W' - 'A'] = 0;
            a['T' - 'A'] -= x;
            a['O' - 'A'] -= x;
        }
        if(a['U'-'A']>0){
            int x = a['U'-'A'];
            for(int j=0;j<x;j++){
                ans.push_back(4);
            }
            a['U' - 'A'] = 0;
            a['F' - 'A'] -= x;
            a['O' - 'A'] -= x;
            a['R' - 'A'] -= x;
        }
        if(a['F'-'A']>0){
            int x = a['F'-'A'];
            for(int j=0;j<x;j++){
                ans.push_back(5);
            }
            a['F' - 'A'] = 0;
            a['I' - 'A'] -= x;
            a['V' - 'A'] -= x;
            a['E' - 'A'] -= x;
        }
        if(a['T'-'A']>0){
            int x = a['T'-'A'];
            for(int j=0;j<x;j++){
                ans.push_back(3);
            }
            a['T' - 'A'] = 0;
            a['H' - 'A'] -= x;
            a['R' - 'A'] -= x;
            a['E' - 'A'] -= x;
            a['E' - 'A'] -= x;
        }
        if(a['S'-'A']>0){
            int x = a['S'-'A'];
            for(int j=0;j<x;j++){
                ans.push_back(7);
            }
            a['S' - 'A'] = 0;
            a['E' - 'A'] -= x;
            a['V' - 'A'] -= x;
            a['E' - 'A'] -= x;
            a['N' - 'A'] -= x;
        }
        if(a['O'-'A']>0){
            int x = a['O'-'A'];
            for(int j=0;j<x;j++){
                ans.push_back(1);
            }
            a['O' - 'A'] = 0;
            a['N' - 'A'] -= x;
            a['E' - 'A'] -= x;
        }
        if(a['I'-'A']>0){
            int x = a['I'-'A'];
            for(int j=0;j<x;j++){
                ans.push_back(9);
            }
            a['I' - 'A'] = 0;
            a['N' - 'A'] -= x;
            a['N' - 'A'] -= x;
            a['E' - 'A'] -= x;
        }
        sort(ans.begin(),ans.end());
        printf("Case #%d: ",i);
        for(int j=0;j<ans.size();j++){
            printf("%d",ans[j]);
        }
        printf("\n");
    }

}