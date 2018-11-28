#include <cstdio>
#include <vector>
using namespace std;
int t;
int l,x;
char inp[10005];
char table[4][4] = {{'1','i','j','k'},
                    {'i','1','k','j'},
                    {'j','k','1','i'},
                    {'k','j','i','1'}};
int sign[4][4] = {{1,1,1,1},
                  {1,-1,1,-1},
                  {1,-1,-1,1},
                  {1,1,-1,-1}};

int toNumber(char c){
        if(c=='1')return 0;
        if(c=='i')return 1;
        if(c=='j')return 2;
        if(c=='k')return 3;
}
int main(){
        //FILE* inf = stdin;
        FILE* inf = fopen("C.in","r");
        FILE* outf = fopen("C.out","w");
        //FILE* outf = stdout;
        fscanf(inf,"%d",&t);
        for(int i=1;i<=t;++i){
                fscanf(inf,"%d%d%s",&l,&x,inp);
                for(int j=0;j<l;++j){
                        for(int k=1;k<x;++k){
                                inp[j+k*l] = inp[j];
                        }
                }

                vector<char> v;
                bool ans = true;
                int left, right;
                int csign = 1;
                char cur = '1';
                for(left=0;left<l*x && cur!='i';++left){
                        csign *= sign[toNumber(cur)][toNumber(inp[left])];
                        cur = table[toNumber(cur)][toNumber(inp[left])];
                }
                v.push_back(cur);
                cur = '1';
                for(right = l*x-1;right>=0 && cur!='k';--right){
                        csign*=sign[toNumber(inp[right])][toNumber(cur)];
                        cur = table[toNumber(inp[right])][toNumber(cur)];
                }
                v.push_back(cur);
                if(left>right)ans=false;
                cur = inp[left];
                for(int j=left+1;j<=right && ans;++j){
                        csign*=sign[toNumber(cur)][toNumber(inp[j])];
                        cur = table[toNumber(cur)][toNumber(inp[j])];
                }
                if(cur!='j' || v[0]!='i' || v[1]!='k' || csign==-1)
                        ans = false;
                fprintf(outf,"Case #%d: %s\n",i,ans?"YES":"NO");
        }

        return 0;
}
