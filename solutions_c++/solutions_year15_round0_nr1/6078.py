//code2323
//Problem A : Standing Ovation (Large input)

#include<iostream>
#include<fstream>
using namespace std;

int main()
{
ifstream infile;
ofstream file2;


char filename[30];
char ch;
cout<<"Please enter file name"<<endl;
cin>>filename;
infile.open(filename);
file2.open("OutputFile.txt");

if(!infile)
{
    cout<<"File not found."<<endl;
    return 1;
    
}
int caseNumber=0;
int numSpaces=0;
int numfriends=0;
int i=-1;
int up=0;

infile.get(ch);
while(ch!='\n')
    infile.get(ch);

while(!infile.eof())
{
    int temp=0;
    infile.get(ch);
    if(ch==' ')
        numSpaces++;
    else if(ch=='\n' && caseNumber<100)
    {
        caseNumber++;
        file2<<"Case #"<<caseNumber<<": "<<numfriends<<endl;
        numfriends=0;
        numSpaces=0;
        i=-1;
        up=0;
    }
    else if (numSpaces==1)
    {
        i++;
        int cha= ch - '0';
        if(i==0 && ch=='0')
        {
            up++;
            numfriends++;
        }
        
        else if(i>up && ch!='0')
        {
            temp=i-up;
            up=up+temp;
            numfriends=numfriends+temp;
        }
        up= up + cha;
    }

}


return 0;
}