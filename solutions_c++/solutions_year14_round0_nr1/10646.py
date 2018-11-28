#include<iostream>
#include<fstream>
#include<string>

using namespace std;

const int row=4;
const int col=4;

void init_board(int **p);
void init_array(int *p);
void fill_board(int **p,ifstream &input);
void save_row(int **p, int *array, int a);
void call_magic(int *array1, int *array2,int num,ofstream &output);


int main()
{
 
 int numTestCases;
 ifstream fin;
 ofstream fout;
 
 
 fin.open("A-small-attempt4.in");
 if(!fin){
          cout<<"NO Input file Detected!";      
 }
 
 fout.open("Output.txt");
 if(!fout){
      cout<<"No Output file detected;";     
 }
 
  fin>>numTestCases;
  
 for(int i=1;i<=numTestCases;i++){ 
 int result;
 int **board1;
 int **board2;
 int *arr1,*arr2;
 int ans1,ans2;
 
 fin>>ans1;
 //init_board(board1);
 board1=new int*[row];
 for(int i=0;i<row;i++)
 {board1[i]=new int[col];}
 
 //init_array(arr1);
 arr1=new int[row];
 
 fill_board(board1,fin);
 save_row(board1,arr1,ans1);
 
 fin>>ans2;
 //init_board(board2);
 board2=new int*[row];
 for(int i=0;i<row;i++)
 {board2[i]=new int[col];}
 
 //init_array(arr2);
 arr2=new int[row];
 
 fill_board(board2,fin);
 save_row(board2,arr2,ans2);
 
 call_magic(arr1,arr2,i,fout);
 
}
    
//system("pause");    
return 0;
}

void init_board(int **board)
{
 board=new int*[row];
 for(int i=0;i<row;i++)
 {board[i]=new int[col];}     
}

void init_array(int *p)
{
 p=new int[row]();     
}

void save_row(int **p, int *array, int a)
{
 int rows=a-1;
 for(int i=0;i<row;i++)
 {
  array[i]=p[rows][i];
         }
     
 }

void fill_board(int **p,ifstream &input)
{
 for(int i=0;i<row;i++)
 {
  for(int j=0;j<col;j++)
   {
    input>>p[i][j];
                   }
                      }    
}

void call_magic(int *array1, int *array2,int num, ofstream &output)
{
 int counter=0;
 int guess;
 int caseNum=num;
 
 /*for(int i=0;i<4;i++)
 {
  cout<<"array1["<<i+1<<"]"<<array1[i]<<endl;
  cout<<"array2["<<i+1<<"]"<<array2[i]<<endl;
         }*/
 
 for(int i=0;i<row;i++)
 {
  for(int j=0;j<row;j++)
  {
   if(array1[i]==array2[j])
   {
     counter++;
     if(counter==1)
      guess=array1[i];
   } 
          }
           }
  //cout<<counter;         
  
  switch(counter)
  {
   case 0:
        output<<"Case"<<" "<<"#"<<caseNum<<":"<<" "<<"Volunteer cheated!";
        break;
   case 1:
        output<<"Case"<<" "<<"#"<<caseNum<<":"<<" "<<guess;
        break;
   default:
           output<<"Case"<<" "<<"#"<<caseNum<<":"<<" "<<"Bad magician!";
           break;           
                       
                 
  }
  output<<endl;
 
}




































