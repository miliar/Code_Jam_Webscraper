#include<fstream>

using namespace std;

int main()
{ifstream fin;
ofstream fout;
fin.open("file.txt");
fout.open("snigdha.txt");
int t,count=1;
unsigned int n,sum;
fin>>t;
std::string str;
std::string no;
while(t--)
{ int arr[1000];
getline(fin,no,' ');
getline(fin,str,'\n');
unsigned int len,i,req;
n=0;
len= no.length();
for(i=0;i<len;i++)
{
n= n*10+ no.at(i);
}
len= str.length();
int m;
for(i=0;i<len;i++)
{
m= (int)str.at(i)-48;
arr[i]= m;
//cout<<arr[i];
}
//cout<<"\n";
sum=0; req=0;
for(i=1;i<len;i++)
{ 
sum+= arr[i-1];
if(sum<i)
 { if(req<(i-sum))
   req= i-sum;
 }

}

fout<<"Case #"<<count<<": "<<req<<"\n";
count++;

}

return 0;
}