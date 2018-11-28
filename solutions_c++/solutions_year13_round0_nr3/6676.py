#include<iostream>
#include<stack>
#include<cmath>
using namespace std;
stack<int> mystack;
int flag;
void pushb(int num)
{
int number=num;
while(num>0)
{
mystack.push(num%10);
num=num/10;
}
while(number>0)
{
if(mystack.top()==number%10)
{
mystack.pop();
number=number/10;
}
else
break;
}
if(mystack.empty())
{
//cout<<" palindrome "<<endl;
flag++;
}

while(!mystack.empty())
mystack.pop();  
}

//main function

int main()
{
int t,test_case;
double new_val,val1;
int count=0;
flag=0;
cin>>t;
test_case=t;
int frm,to;
while(t--)
{
count=0;
cin>>frm;
cin>>to;
while(frm<=to)
{
//cout<<" frm is "<<frm<<endl;
pushb(frm);
if(flag==1)
{
new_val=sqrt(frm);
int i_sqrt=new_val;
if(new_val==i_sqrt)
pushb(new_val);
//else
//break;
if(flag==2)
{
//cout<<"perfect number"<<endl;
count++;
//cout<<" flag val is "<<flag<<" for "<<frm<<endl;
flag=0;
}
}

flag=0;
frm++;
}
cout<<"Case #"<<(test_case-t)<<": "<<count<<endl;
}
return 0;
}

