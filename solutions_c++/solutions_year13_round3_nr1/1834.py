#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <fstream>

using namespace std;
char a[101];

int chk(int l,int j,int n)
{int cou=0,i=0,c=0,tag=0;
int ch=0;

while(l!=j)
{switch(a[l])
{case 'b': c++; break;
case 'c': c++; break;
case 'd': c++; break;
case 'f': c++; break;
case 'g': c++; break;
case 'h': c++; break;
case 'j': c++; break;
case 'k': c++; break;
case 'l': c++; break;
case 'm': c++; break;
case 'n': c++; break;
case 'p': c++; break;
case 'q': c++; break;
case 'r': c++; break;
case 's': c++; break;
case 't': c++; break;
case 'v': c++; break;
case 'w': c++; break;
case 'x': c++; break;
case 'y': c++; break;
case 'z': c++; break;
} 

if(tag==0)
{if(a[l]=='b' || a[l]=='c' || a[l]=='d' ||a[l]=='f' ||a[l]=='g' ||a[l]=='h' ||a[l]=='j' ||a[l]=='k' ||a[l]=='l' ||a[l]=='m' ||a[l]=='n' ||a[l]=='p' ||a[l]=='q' ||a[l]=='r' ||a[l]=='s' ||a[l]=='t' ||a[l]=='v' ||a[l]=='w' ||a[l]=='x' ||a[l]=='y' ||a[l]=='z')
 ch++; 
else
ch=0;
}
if(ch>=n)tag=1;
if(c>=n && tag==1) { cou++;}
l++;
}

    return cou;
}


int main(int argc, char *argv[])
{
    ifstream myfile ("INPUT.txt");
    ofstream myfile1;
    myfile1.open ("OUTPUT.txt");
    int t,count=0;
    myfile>>t;
    
    int n,j=0;
    for(int i=1;i<=t;i++)
    {myfile>>a>>n;
    while(a[j]!='\0') j++; 
     
    for(int k=0;k<j;k++)
    {count+=chk(k,j,n);
    }
    
    
    myfile1<<"Case #"<<i<<": "<<count;
     
     
     
    count=0;
    j=0;
    myfile1<<endl;
    }
    
    
    myfile1.close();
    myfile.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}
