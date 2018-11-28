 #include<iostream>
 #include<fstream>
 using namespace std;
 
 int main()
 {
     int n,a1[4][4],a2[4][4],r1,r2,temp[4],d,count=0;
     ifstream fi;
     ofstream fc;
     fc.open("out.txt");
     fi.open("input.txt");
     fi>>n;
     for(int i=0;i<n;i++)
     {
                 fi>>r1;
                 for(int j=0;j<4;j++)
                 for(int k=0;k<4;k++)
                 {
                         fi>>a1[j][k];
                 }
                 fi>>r2;
                 for(int j=0;j<4;j++)
                 for(int k=0;k<4;k++)
                 {
                         fi>>a2[j][k];
                 }
                 for(int l=0;l<4;l++)
                 {
                         temp[l]=a1[r1-1][l];
                 }
                 for(int j=0;j<4;j++)
                 {
                         for(int k=0;k<4;k++)
                         {
                                 if(temp[j]==a2[r2-1][k])
                                 {
                                                   count++;
                                                   d=temp[j];
                                 }
                         }
                 }
                 fc<<"Case #"<<i+1<<": ";
                 if(count==1)
                 fc<<d<<endl;
                 else if(count>1)
                 fc<<"Bad magician!"<<endl;
                 else if(count==0)
                 fc<<"Volunteer cheated!"<<endl;
                 count=0;
     }
 return 0;
 }
