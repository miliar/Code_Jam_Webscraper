#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;
int divi[9];
long int giv_div(long long int value)
{
    for(long long int c=2;c<value;c++)
    {
        if(value%c==0)
        {
            return c;
        }
    }

}

bool not_prime(long long int value)
{
    int st=0;
    long int logg=log2l(value);
    for(long long int c=2;c<(logg+1);c++)
  {
    if(value%c==0)
    {
        st=1;
        return true;

    }
  }
  if(st==0)
    return false;
}

long long int power(int x,int y)
{
    long long int temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}



int main()
{

string number,arr,num1,num2;
ifstream inp_file;
inp_file.open("question.txt");
getline(inp_file,number);
ofstream out_file;
out_file.open("uv_ans.txt");
out_file<<"Case #1:\n";

int lim;

int i=0;
getline(inp_file,arr);
arr[arr.length()]='.';
stringstream conver(arr);
conver>>lim;

while(arr[i]!=' ')
{
    i++;
}
int p=i+1;
i=0;
while(arr[p]!='.')
{
    num2.append(&arr[p]);
    p++;

}
int digits,out;
stringstream conver2(num2);
conver2>>out;
digits=lim;

int jam[40];
int cnt=0;
//digits=16;
//out=50;
int llim=digits-1;
int last=llim;
for(int i=0;i<digits;i++)
  {
      jam[i]=0;
  }
jam[0]=1;
  cout<<"DIGITS: "<<digits<<" OUT: "<<out;
int mou=0;
while(cnt<out)
{
  jam[last]=1;

 do {
  float j=0;
  int perm_sum=0;

  for(int j=0;j<9;j++)
    divi[j]=0;


  for(j=2;j<=10;j++)
  {

      long long int value=0;

      for(int k=0;k<(digits);k++)
      {
          value=value+((power(j,k))*jam[llim-k]);
      }
      cout<<"\nbase : "<<j<<" Value: "<<value<<endl;

      if(not_prime(value))
  {
      int df=giv_div(value);
      cout<<"\nDIVISOR: "<<df<<endl;
      divi[perm_sum]=df;
      perm_sum++;
  }
  else
  {
      cout<<("\nPRIME\n");
      break;
  }

  }

cout<<"\nPERM: "<<perm_sum<<endl;
if(perm_sum==9 && cnt<(out))
{

    cout<<"\nANSWER:"<<cnt<<endl;
  for(int h=0;h<digits;h++)
        {
            out_file<<jam[h];
            cout<<jam[h];
            ++mou;
        }

        cout<<endl;
       // out_file<<jam[h];
    for(int m=2;m<11;m++)
        {
            cout<<divi[m]<<endl;
            out_file<<" "<<divi[m-2];
        }
        for(int j=0;j<9;j++)
            divi[j]=0;
   out_file<<endl;

    cnt++;

}


} while ( std::next_permutation(jam+1,jam+llim) && (cnt<out));

last=last-1;

}



cout<<"\nMOU: "<<mou;
return 0;
}
