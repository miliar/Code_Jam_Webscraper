#include <iostream>
#include<stdio.h>
#include<string>
#define gc getchar_unlocked
using namespace std;

long long int read_int()
{
char ch;
ch=gc();
while(ch<'0'||ch>'9')
ch=gc();
long long int ret=0;
while(ch>='0'&&ch<='9')
{
ret=ret*10+ch-48;
ch=gc();
}
 
return ret;
}

int main() {
	// your code goes here
    long long int T,smax,i,number_of_friends_given=0,total_people=0,difference=0,cnt=1;
	string s;
	T=read_int();
	while(T--)
    {
        smax=read_int();
        long long int number_of_people[smax+1];
        
        cin>>s;
        for(i=0;i<=smax;i++)
        {
            number_of_people[i]=s[i]-48;
           // total_people=number_of_people[i];
            if(number_of_people[i]!=0)
            {
                if(i>total_people)
                {
                difference=i-total_people;
                number_of_friends_given+=i-total_people;
                total_people+=number_of_people[i]+difference;  

                }
                else
                total_people+=number_of_people[i];
            }

                
            
        }
        
        cout<<"Case #"<<cnt<<": "<<number_of_friends_given<<endl;
        number_of_friends_given=total_people=difference=0;
        cnt++;
        
    }
	return 0;
}
