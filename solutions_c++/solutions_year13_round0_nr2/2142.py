#include<iostream>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T;
    cin>>T;
    cin.ignore();
    
    string outputs[2]={"NO","YES"};
    
    int result,noOfRows,noOfCols,i,j;
    
    int **matrix;
    int *maxInRow,*maxInCol;
    
    
    int t=1;
    while(T--)
    {
        cin>>noOfRows>>noOfCols;
        
        matrix = (int **)malloc(sizeof(int*)*noOfRows);
        for(i=0;i<noOfRows;i++)
        {
            matrix[i]= (int *)malloc(sizeof(int)*noOfCols);
        }
        
        maxInRow = (int *)malloc(sizeof(int)*noOfRows);
        maxInCol = (int *)malloc(sizeof(int)*noOfCols);
        
        //reset all values
        memset (maxInRow,0xFF,sizeof(int)*noOfRows);
        memset (maxInCol,0xFF,sizeof(int)*noOfCols);
        result=1;
        
        for(i=0;i<noOfRows;i++)
        {
            for(j=0;j<noOfCols;j++){
                cin>>matrix[i][j];
                if(matrix[i][j]>maxInRow[i])
                    maxInRow[i]=matrix[i][j];
                if(matrix[i][j]>maxInCol[j])
                    maxInCol[j]=matrix[i][j];
            }
        }
        
        for(i=0;i<noOfRows;i++)
        {
            for(j=0;j<noOfCols;j++){
                if(maxInCol[j]>matrix[i][j] && maxInRow[i]>matrix[i][j]){
                    result=0;
                    goto outsideNestedForLoop;
                }
            }
        }
        outsideNestedForLoop:
            
        
        cout<<"Case #"<<t++<<": "<<outputs[result]<<endl;
        cin.ignore();
        
        for(i=0;i<noOfRows;i++)
        {
            free(matrix[i]);
        }
        free(matrix);
    }
    
    return 0;
}