#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
using namespace std;

string outarr[]={"NO","YES"};

class Lawn{
    public:
    int row,col;
    int harr[100][100];
    bool visited[100][100];
    
    Lawn(int row,int col);
    int mark();
};

Lawn::Lawn(int rowNo,int colNo){
    row=rowNo;col=colNo;
    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            visited[i][j]=false;
        }
    }
}

int 
Lawn::mark(){
    int minrow=-1,mincol=-1,min=200;
    for (int i=0; i<row; i++){
       for(int j=0;j<col;j++){
            if(!visited[i][j]){
                if(harr[i][j]<min){
                    minrow=i;mincol=j;min=harr[i][j];
                }
            }
       }
    }
    //printf("%d %d %d\n", minrow,mincol,min);
    bool deleterow=true,deletecol=true;
    if(min!=200){//has remaining elements
        //check if min is the minimum of the row
        for(int j=0;j<col;j++){
            if(!visited[minrow][j]&&harr[minrow][j]!=min){
                deleterow=false;
            }
        }
        //check if min is the minimum of the col
        for(int i=0;i<row;i++){
            if(!visited[i][mincol]&&harr[i][mincol]!=min){
                deletecol=false;
            }
        }
        if(deleterow){
            for(int j=0;j<col;j++){
                visited[minrow][j]=true;
            }
        }
        if(deletecol){
            for(int i=0;i<row;i++){
                visited[i][mincol]=true;
            }
        }

        if(!deleterow && !deletecol){return 0;}
        return mark();
    }
    return 1;
}


int main(){
    int casenum,rowNo,colNo;
    
    scanf("%d\n",&casenum);

    for(int k=0;k<casenum;k++){
        scanf("%d %d\n",&rowNo,&colNo);
        Lawn *lawn=new Lawn(rowNo,colNo);
        for(int i=0;i<rowNo;i++){
            for(int j=0;j<colNo;j++){
                scanf("%d",&lawn->harr[i][j]);
            }
            scanf("\n");
        }
        int res=lawn->mark();
        delete lawn;
        printf("Case #%d: ",k+1);
        cout<<outarr[res]<<endl;
    }

    return 0;
}
