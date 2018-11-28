#include<iostream>
#include <fstream>
using namespace std;
int first[4][4];
int second[4][4];
int t,answer1,answer2;
int main(){
scanf("%d",&t);
ofstream ocout;
ocout.open("test2.txt");
int i,j,k,score;
for(k=1;k<=t;k++){
     scanf("%d",&answer1);
     for(i=0;i<4;i++)
     for(j=0;j<4;j++)
     scanf("%d",&first[i][j]);
     scanf("%d",&answer2);
     for(i=0;i<4;i++)
     for(j=0;j<4;j++)
     scanf("%d",&second[i][j]);
     score=0;
     int result;
     for(i=0;i<4;i++){
       for(j=0;j<4;j++)
           if(first[answer1-1][i]==second[answer2-1][j])
           {score++;result=first[answer1-1][i];}
     }
     if(score==1)
     ocout<<"Case #"<<k<<": "<<result<<endl;
     else if(score==0)
     ocout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
     else
     ocout<<"Case #"<<k<<": Bad magician!"<<endl;
}
ocout.close();
system("pause");
return 0;
}
