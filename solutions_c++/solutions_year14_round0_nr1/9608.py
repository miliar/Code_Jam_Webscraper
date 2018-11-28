#include<stdio.h>
#include<conio.h>

int match[110];
FILE *f1,*f2;

void take_input(int arr[5][5]);
void store_selected_row(int arr[5][5],int,int selected_row[]);
int compare_choices(int arr1[],int arr2[],int match_index);

int main(){
    
    int arr1[5][5],row1,row1_sel[5];
    int arr2[5][5],row2,row2_sel[5];
    int no_test_case,result[110];
    
    
       f1 = fopen("E:\\A-small-attempt0 (2).in","r");
       f2=fopen("E:\\output_magician.txt","w");
    
  if(f1!=NULL && f2!=NULL)
  {
    
    fscanf(f1,"%d",&no_test_case);
    
    if(no_test_case<=100)
    {
       for(int temp=1;temp<=no_test_case;temp++)
       {
            
            fscanf(f1,"%d",&row1);   
            take_input(arr1);                 
            store_selected_row(arr1,row1,row1_sel);  
     
            
            fscanf(f1,"%d",&row2);             
            take_input(arr2);               
            store_selected_row(arr2,row2,row2_sel);
     
            int flag = compare_choices(row1_sel,row2_sel,temp);
    
            result[temp] = flag;
           
           
       }
    
       
       for(int temp=1;temp<=no_test_case;temp++)
       {
    
           if(result[temp] == 0)
                      fprintf(f2,"Case #%d:  Volunteer cheated! \n",temp);
    
           if(result[temp] == 1)
                      fprintf(f2,"Case #%d:  %d \n",temp,match[temp]);
                
           if(result[temp] > 1)
                      fprintf(f2,"Case #%d:  Bad magician! \n",temp);
                      
       }
    }
    
    else
     printf("\n Please enter a value less than 101");
 
 
 }
 else
     printf("\n OOPS!!! FILES COULDN'T BE OPENED...");
     
    fclose(f1); 
    fclose(f2);
    getch();
    return 0;
}


void take_input(int arr[5][5])
{
     for(int i=1;i<=4;i++)
    {
            
                      int j=1;
                    fscanf(f1,"%d %d %d %d",&arr[i][j],&arr[i][j+1],&arr[i][j+2],&arr[i][j+3]);
            
    }
     
}


void store_selected_row(int arr[5][5],int row_index, int selected_row[])
{
      
    for(int i=1;i<=4;i++)
    {
         selected_row[i]=arr[row_index][i];
               
         
     }

}

int compare_choices(int arr1[],int arr2[],int match_index)
{
    int flag=0;
    
    for(int i=1;i<=4;i++)
    {
         if(arr1[i]==arr2[1] || arr1[i]==arr2[2] || arr1[i]==arr2[3] || arr1[i]==arr2[4])
         {
               match[match_index]=arr1[i];
               flag++;
         }
    }
    
    return flag;
}







