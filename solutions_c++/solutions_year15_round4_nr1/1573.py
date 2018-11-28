
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

int T,R,C;

char matrix[100][100];
bool only[100][100];

int main()
{
    int res;

    scanf("%d",&T);
    for(int c=0;c<T;c++)
    {
        scanf("%d %d",&R,&C);
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                only[i][j]=false;
                do{
                    scanf("%c",&matrix[i][j]);
                }while(matrix[i][j]!='.'
                    && matrix[i][j]!='>'
                    && matrix[i][j]!='<'
                    && matrix[i][j]!='v'
                    && matrix[i][j]!='^');
            }
        }
        int first;
        int last;
        int res=0;
        bool imp=false;
        for(int i=0;i<R;i++){
            first=-1;
            last=-1;
            for(int j=0;j<C;j++)
            {
                if(matrix[i][j]=='.')
                    continue;
                if(first<0)
                    first=j;
                last=j;
            }
            if(first==-1)
                continue;
            if(first!=last){
                if(matrix[i][first]=='<'){
                    matrix[i][first]='>';
                    res++;
                }
                if(matrix[i][last]=='>'){
                    matrix[i][last]='<';
                    res++;
                }
            }else{
                if(matrix[i][first]=='<' || matrix[i][first]=='>'){
                    matrix[i][first]='*';
                    res++;
                }
                only[i][first]=true;
            }
        }
        for(int j=0;j<C;j++){
            first=-1;
            last=-1;
            for(int i=0;i<R;i++)
            {
                if(matrix[i][j]=='.')
                    continue;
                if(first<0)
                    first=i;
                last=i;
            }
            if(first==-1)
                continue;
            if(first!=last){
                if(matrix[first][j]=='^' || matrix[first][j]=='*'){
                    if(matrix[first][j]!='*')res++;
                    matrix[first][j]='v';
                }
                if(matrix[last][j]=='v' || matrix[last][j]=='*'){
                    if(matrix[last][j]!='*')res++;
                    matrix[last][j]='^';
                }
            }else{
                if(matrix[first][j]=='*')
                    imp=true;
                if(matrix[first][j]=='v' || matrix[first][j]=='^'){
                    if(only[first][j])
                        imp=true;
                    matrix[first][j]='>';
                    res++;
                }
            }
        }
        printf("Case #%d: ",c+1);
        if(imp)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",res);
    }
    return 0;
}

