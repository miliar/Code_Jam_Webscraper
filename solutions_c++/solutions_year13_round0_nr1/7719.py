#include <cstdlib>
#include <iostream>

using namespace std;

bool FindVictor(int a,int arr[], int victory[][2], bool& ret)
{
     int j,k;
     for(j=0;j<a;j++) //row and col
     {
        for(k=0;k<2;k++)
        {
          if(arr[j] == victory[0][k]) //X win
          {
             ret = false;
             return true;
          }
          else if(arr[j] == victory[1][k]) //O win
          {
             ret = true;
             return true;   
          }
        }
     }
     return false;
}
int main(int argc, char *argv[])
{
    FILE* fp, *ofp;
    //char board[4][4];
    int row[4]={0},col[4]={0},diag[2]={0},iX,iY;
    bool dot=false;
    int victory[2][2]={348,352,316,321};//X,O
    int num,index=0,i,j,k;
    char c;
    
    fp = fopen("A-large.in","r");
    ofp = fopen ("A-large.out","w");
    if(!fp || !ofp) { 
        return 1; 
    } 
    
    fscanf(fp,"%d", &num);
    fgetc(fp);
    for(i=0;i<num;i++)
    {
     index = 0;
     memset(row, 0, sizeof(row));
     memset(col, 0, sizeof(col));
     memset(diag, 0, sizeof(diag));
     dot = false;
     while(!feof(fp))
     {
          c = fgetc(fp);
          if( c == '\n' || c == -1)
          {
              if(index == 16) 
              {
                //printf("\n");
                 break;
              }
              else
              { 
                  //printf("\n");
                  continue;
              }
          }
          else if(c == 46)
            dot = true;
            
          //printf("%d ",c);
          iX = index/4;
          iY = index%4;
          if(iX == iY)
             diag[0] += c;
          else if(iX+iY == 3)
             diag[1] += c;
          
          row[iX] += c;
          col[iY] += c;
          //board[iX][iY] = c;
          index++;
     } //end of while
     bool ret = false;
     if(FindVictor(4,row,victory,ret)||
        FindVictor(4,col,victory,ret)||
        FindVictor(2,diag,victory,ret))
     {
         if(ret)
            fprintf(ofp,"Case #%d: O won\n",i+1);
         else  fprintf(ofp,"Case #%d: X won\n",i+1);
     }
     else if(dot)
        fprintf(ofp,"Case #%d: Game has not completed\n",i+1);
     else fprintf(ofp,"Case #%d: Draw\n",i+1);

    }// end of for
    fclose(fp);
    fclose(ofp);
    //system("PAUSE");
    return EXIT_SUCCESS;
}
