#include<cstdio>
#include<algorithm>
#include<utility>
#include<stack>
using namespace std;
int tc,r,c,aa,bb;
char hedges[100][100];// r,c // ' ','/','\'
int courtier[400];
int main(){
    scanf("%d",&tc);
    for(int ct=1;ct<=tc;++ct){
        scanf("%d%d",&r,&c);
        for(int i=0;i<r+c;++i){
            scanf("%d%d",&aa,&bb);
            --aa;
            --bb;
            courtier[aa]=courtier[bb]=i;
        }
        printf("Case #%d:\n",ct);

        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                hedges[i][j]=' ';
            }
        }
        // do first crossing check:
        stack<int> st; //index
        bool br=false;
        for(int i=0;i<2*(r+c);++i){
            if(!st.empty()&&courtier[st.top()]==courtier[i]){
                // do aligned search:
                int target=st.top();
                st.pop();
                int source=i;
                // entry direction (from): 0:top,1:right,2:bottom,3:left
                int currx,curry,currdir;
                if(source<c){
                    currx=source;
                    curry=0;
                    currdir=0;
                }
                else if(source<c+r){
                    currx=c-1;
                    curry=source-c;
                    currdir=1;
                }
                else if(source<c+r+c){
                    currx=c-1-(source-c-r);
                    curry=r-1;
                    currdir=2;
                }
                else{
                    currx=0;
                    curry=r-1-(source-c-r-c);
                    currdir=3;
                }
                int reached;
                while(true){
                    if(hedges[curry][currx]==' '){
                        switch(currdir){
                        case 0:
                            hedges[curry][currx]='/';
                            break;
                        case 1:
                            hedges[curry][currx]='\\';
                            break;
                        case 2:
                            hedges[curry][currx]='/';
                            break;
                        case 3:
                            hedges[curry][currx]='\\';
                            break;
                        }
                    }
                    if(hedges[curry][currx]=='/'){
                        switch(currdir){
                        case 0:
                            --currx;
                            currdir=1;
                            break;
                        case 1:
                            ++curry;
                            currdir=0;
                            break;
                        case 2:
                            ++currx;
                            currdir=3;
                            break;
                        case 3:
                            --curry;
                            currdir=2;
                            break;
                        }
                    }
                    else{ // '\'
                        switch(currdir){
                        case 0:
                            ++currx;
                            currdir=3;
                            break;
                        case 1:
                            --curry;
                            currdir=2;
                            break;
                        case 2:
                            --currx;
                            currdir=1;
                            break;
                        case 3:
                            ++curry;
                            currdir=0;
                            break;
                        }
                    }
                    if(currx<0||currx>=c||curry<0||curry>=r){
                        if(curry<0){
                            reached=currx;
                        }
                        else if(currx>=c){
                            reached=curry+c;
                        }
                        else if(curry>=r){
                            reached=c-1-currx+c+r;
                        }
                        else{
                            reached=r-1-curry+c+r+c;
                        }
                        break;
                    }
                }
                if(reached!=target){
                    //printf("%d %d\n",reached,target);
                    printf("IMPOSSIBLE\n");
                    br=true;
                    break;
                }
            }
            else{
                st.push(i);
            }
        }
        if(br)continue;
        if(st.size()>0){
            printf("IMPOSSIBLE\n");
            continue;
        }
        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                if(hedges[i][j]==' ')hedges[i][j]='/';
                printf("%c",hedges[i][j]);
            }
            printf("\n");
        }
    }
}

