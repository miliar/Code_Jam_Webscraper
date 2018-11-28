#include<iostream>
#include<fstream>
#include<vector>
#include<stack>
using namespace std;
int main()
{
vector<int> people(7);
int cases=0;
int sum=0;
int max=0;
int pta=0;
stack<int> n;
ifstream read;
ofstream write;
read.open("input.txt",ios::in);
write.open("output.txt",ios::out);
read>>cases;

for(int c=0;c<cases;c++){
int sum=0;
int max=0;
int pta=0;

read>>max;
int num=0;
read>>num;
for(int co=0;co<max+1;co++){
n.push(num%10);
num=num/10;
}
for(int c1=0;c1<max;c1++){

people[c1]=n.top();
n.pop();


}

for(int co1=0;co1<max;co1++){
sum=sum+people[co1];
if(people[co1]==0){
if(sum<co1+1){
pta++;
sum++;
}
}
}
write<<"Case #"<<c+1<<": "<<pta<<endl;
}
read.close();
write.close();
return 0;
}