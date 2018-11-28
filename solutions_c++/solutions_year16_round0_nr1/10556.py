#include<cstdlib>
#include<string>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
vector<int> v; 
long int testcase;
 long int get_num;
 scanf("%ld",&testcase);


//Gets the number of testcases 
for(long int i=1;i<=testcase;i++)
 {
  cin>>get_num;
  
if(get_num==0)
 {
 printf("Case #%ld: INSOMNIA\n",i);
continue;
}
else
{


string snum = to_string(get_num);
long int z_num;
long int rem=0;
long int ecount=0;
long int next_count=1;
v.clear();
//cout<<"VECTOR SIZE="<<v.size();

here:
//cout<<"ECOUNT-"<<ecount<<endl<<"NEXT_COUNT"<<next_count<<endl;
z_num = next_count*get_num;
//cout<<"Z_NUM="<<z_num<<endl;
long int num=z_num;
//Splits the number to seperate digits and stores in vector
for(long int j=1;j<=snum.length();j++)
{
while(num>0)
{
rem = num % 10;
num = num / 10;

//cout<<rem<<endl;
if(v.empty())
{
v.push_back(rem);
ecount = ecount + 1;
}
else if(!v.empty() && find(v.begin(), v.end(), rem) != v.end())
{ 
continue;
}
else
{
v.push_back(rem);
ecount = ecount + 1;
}
}
}
if(v.size()!=10)
{
next_count = next_count + 1;
goto here;
}
else
{

// CHECKPOINT cout<<"Content of Vector"<<endl;
/*for(int p=0;p<v.size();p++)
{
cout<<v[p]<<" ";
}
*/
printf("Case #%ld: %ld\n",i,z_num);
}
}
}
}


  
    
