#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
using namespace std;
int num[10][4]={{0,1,2,3},{4,5,6,7},{8,9,10,11},{12,13,14,15},{0,4,8,12},{1,5,9,13},{2,6,10,14},{3,7,11,15},{0,5,10,15},{3,6,9,12}};
char check(char box2[])
{
char first;
int j;
for(int k=0;k<10;k++)
{ j=0;
if(box2[num[k][j]]!='T')
{ first=box2[num[k][j]];}
else
{first= box2[num[k][j+1]];}

 for(j=0;j<4;j++)
 {    if((box2[num[k][j]]!=first&&box2[num[k][j]]!='T')||box2[num[k][j]]=='.')break; 

   if(j==3)return first;  
 }


}

return 'F';

}
int main ()
{

 //   ofstream cout ("1.out");
  //  ifstream cin ("1.in");
int N,i;
char box[16],now;
cin>>N;

for(int w=1;w<=N;w++)
{
   
  memset(box,0,sizeof(box));

 for(i=0;i<16;i++)cin>>box[i];

 cout<<"Case #"<<w<<": ";

now=check(box);
if(now=='F')
{
 for(i=0;i<16;i++)
 {
 if(box[i]=='.')
 { cout<<"Game has not completed"<<endl;
     break; }
 if(i==15)cout<<"Draw"<<endl;
 }

 
}
else
{
cout<<now<<" won"<<endl;

}



/*

for(i=0;i<16;i++)
{
cout<<box[i];
if(i%4==3)cout<<endl;
}

cout<<endl;
*/

}








//cin.close();
//cout.close();


   return 0;
}



