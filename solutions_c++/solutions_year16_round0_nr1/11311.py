#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int countSheep(int );
int main()
{
int ntc=0;
string s;
int i=0;
ifstream infile("file0.IN"); 
infile>>ntc;
int n[ntc];
cout<<ntc<<endl;
i=0;
while (i<ntc) 
{ 
infile>>n[i];
i++;
} 
i=0;
ofstream outputFile;
outputFile.open("outputcountingsheep.txt");
while(i<ntc)
{
    int m=countSheep(n[i]);
    if(m==-1)
    {
        cout<<"case #"<<i+1<<":"<<"INSOMNIA"<<endl;
outputFile<<"case #"<<i+1<<":"<<" INSOMNIA"<<endl;
    }
    else
    {
cout<<"case #"<<i+1<<":"<<m<<endl;
outputFile<<"case #"<<i+1<<": "<<m<<endl;

}
i++;
}
outputFile.close();
return 0;
}

int countSheep(int n)
{
int num=n;
int checked[10]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
if(n==0)
{
return -1;
}
int i=1;
while(1)
{
num=n*i;
int dnum=num,y=0;
while(num!=0)
{
int x=num%10;
checked[x]=x;
num=num/10;
}
while(checked[y]==y&&y<10)
{y++;}
if(y==10){return dnum;}
i++;
}
}



















