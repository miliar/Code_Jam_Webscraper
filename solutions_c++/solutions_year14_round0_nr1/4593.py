#include<fstream.h>
#include<iostream.h>

int row,col,case1[4][4],case2[4][4];

int result(void);

char results[100];

void main()
 {
  char junk;
  int k,j,cases,i;
  ifstream filin;
  filin.open("goog1i.in",ios::in);
  filin>>cases;
  filin.get(junk);
  for (i=0;i<cases;i++)
   {
    filin>>row;
    filin.get(junk);
    for (j=0;j<4;j++)
     {
      for (k=0;k<4;k++)
       {
	filin>>case1[j][k];
	filin.get(junk);
       }
      filin.get(junk);
     }
    filin>>col;
    filin.get(junk);
    for (j=0;j<4;j++)
     {
      for (k=0;k<4;k++)
       {
	filin>>case2[j][k];
	filin.get(junk);
       }
      filin.get(junk);
     }
    results[i]=result();
    filin.get(junk);
   }
  filin.close();
  ofstream filout;
  filout.open("goog1o.in",ios::out);
  for (i=0;i<cases;i++)
   {
    filout<<"Case #"<<i+1<<": ";
    if (results[i]==0)
     {
      filout<<"Bad magician!";
     }
    if (results[i]==17)
     {
      filout<<"Volunteer cheated!";
     }
    if (results[i]!=0&&results[i]!=17)
     {
      filout<<results[i];
     }
    filout<<'\n';
   }
  filout.close();
 }

int result(void)
 {
  int i,j,count,rowco[4],colco[4],stri,strj;
  for (count=0;count<4;count++)
   {
    rowco[count]=case1[row-1][count];
    colco[count]=case2[col-1][count];
   }
  count=0;
  for (i=0;i<4;i++)
   {
    for (j=0;j<4;j++)
     {
      if (rowco[i]==colco[j])
       {
	count++;
	stri=i;
       }
     }
   }
  if (count==0)
    return 17;
  if (count>1)
    return 0;
  return rowco[stri];
 }