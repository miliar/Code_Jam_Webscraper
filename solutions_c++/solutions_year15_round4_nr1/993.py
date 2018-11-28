#include"cstdio"
#include"iostream"
#include"map"
#include"string"
#include"cstring"
#include"vector"
#include"utility"
#include"algorithm"
#include"cmath"
#include"queue"
#include"stack"
#include"set"

using namespace std;
int gR,gC;
int is_ok(int r,int c,vector<string>&grid,vector<string>&cf){
    char ch=grid[r][c];
    if(ch=='^'){
        bool has_arw=false;
        for(int i=r-1;i>=0;i--){
            if(grid[i][c]!='.'){
                has_arw=true;
                break;
            }
        }
        if(has_arw){return 1;}
        else {return 0;}
    }
    else if(ch=='>'){
        bool ha=false;
        for(int j=c+1;j<gC;j++){
            if(grid[r][j]!='.'){
                ha=true;
                break;
            }
        }
        if(ha){return 1;}
        else return 0;
    }
    else if(ch=='<'){
        bool ha=false;
        for(int j=c-1;j>=0;j--){
            if(grid[r][j]!='.'){
                ha=true;
                break;
            }

        }
        if(ha){return 1;}
        else {return 0;}
    }
    else if(ch=='v'){
        bool ha=false;
        for(int i=r+1;i<gR;i++){
            if(grid[i][c]!='.'){
                ha=true;
                break;
            }
        }
        if(ha){return 1;}
        else {return 0;}
    }
    else{

        puts("error!");
        return -1;
    }
}
int is_zero(vector<string>&grid,vector<string>&cf){
    int ans=0;
    for(int i=0;i<gR;i++){
        for(int j=0;j<gC;j++){
            if(grid[i][j]!='.'){
                //arrow:
                //if ok:
                if(is_ok(i,j,grid,cf)==1){
                    ;//
                }
                else {
                    //try
                    grid[i][j]='^';
                    if(is_ok(i,j,grid,cf)){
                        ans++;
                        continue;
                    }
                    grid[i][j]='>';
                    if(is_ok(i,j,grid,cf)){
                        ans++;
                        continue;
                    }
                    grid[i][j]='v';
                    if(is_ok(i,j,grid,cf)){
                        ans++;
                        continue;
                    }
                    grid[i][j]='<';
                    if(is_ok(i,j,grid,cf)){
                        ans++;
                        continue;
                    }
                    return -1;
                }
            }
        }
    }
    return ans;

}
int main(){
    freopen("d:A-large.in","r",stdin);
    freopen("d:A.out","w",stdout);

	int T;
	int casenum=0;
	cin>>T;
	while(casenum++<T){
        int R,C;
        cin>>R>>C;
        gR=R;
        gC=C;
        vector<string>grid;
        vector<string>can_flee;
        for(int i=0;i<R;i++){
            string tmp;
            cin>>tmp;
            grid.push_back(tmp);
            string tt(C,'n');
            can_flee.push_back(tt);
        }//input
        int ans=is_zero(grid,can_flee);
        if(ans==-1){
            printf("Case #%d: IMPOSSIBLE\n",casenum);
        }else{
            printf("Case #%d: %d\n",casenum,ans);
        }
	}


return 0;}
