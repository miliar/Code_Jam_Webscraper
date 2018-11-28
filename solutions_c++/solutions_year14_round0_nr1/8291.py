#include<iostream>
#include<fstream>
using namespace std;


int main()
{
int array1[4][4], array2[4][4];
int cases,j,k,m,a1,a2,count,temp;

ifstream i;
ofstream out;
i.open("A-small-attempt0.in");
out.open("q1output.txt");

i>>cases;
for (j=1;j<=cases;j++){
    i>>a1;
    for (k=0;k<4;k++){
        for (m=0;m<4;m++){i>>array1[k][m];}   
    }
    i>>a2;
    for (k=0;k<4;k++){
        for (m=0;m<4;m++){i>>array2[k][m];}   
    }
    a1--;a2--;
    count=0;
    for (k=0;k<4;k++){
         for (m=0;m<4;m++){
            if (array1[a1][k]==array2[a2][m]){temp=array1[a1][k];count++;} 
         }
    }
    if (count==1) out<<"Case #"<<j<<": "<<temp<<endl;
    else  if (count>1) out<<"Case #"<<j<<": Bad magician!"<<endl;
    else if  (count==0) out<<"Case #"<<j<<": Volunteer cheated!"<<endl;
    //cout<<k;
}//for (j=0;j<cases;j++)


    //system("pause"); // comment it afterwards
    return 0;
}
