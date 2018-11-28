#include<iostream>


using namespace std;

void solveNumber(int );
void getArray(int iArr1[][4], int , int);

int main()
{
 int N=0,i=0;
 cin>>N;   //number of test cases
 cout<<"\n";
 
 for(i=0; i<N;i++)
 {
   solveNumber(i+1);   
 } 
 return 0;
}

void solveNumber(int Case)
{
  int firstRow, SecondRow, i=0,j=0;
  int iArr1[4][4], iArr2[4][4];
  //get first number
  cin>>firstRow;
  
  //get Array first
  getArray(iArr1,4,4);
  //get second number
  cin>>SecondRow;
  getArray(iArr2,4,4);

  //search elements in first row first array =>in second row second array
  //if single find got the number
  //if >1 find Bad magician
  //if 0 find Volunteer cheated!
  //

  int count =0, finNum=0;
  for(i=0;i<4;i++)
  {

    for(j=0;j<4;j++)
    {
     if(iArr1[firstRow-1][i] == iArr2[SecondRow-1][j])
     {
       count++;
       finNum = iArr1[firstRow-1][i];
     }
    }
  }

  if(count ==0)
  cout<<"Case #"<<Case<<": Volunteer cheated!"<<endl;
  else if(count > 1)
  cout<<"Case #"<<Case<<": Bad magician!"<<endl;
  else
  cout<<"Case #"<<Case<<": "<<finNum<<endl;
  
}

void getArray(int iArr1[][4], int M, int N)
{
   int i=0, j=0;
   for(i=0; i<M;i++)
  {
    for(j=0;j<N;j++)
    {
       cin>>iArr1[i][j];
       //cout<<"got::"<<iArr1[i][j]<<"\t";
    }
    //cout<<"\n";
  }

}
