//the first of the questions
#include<iostream>
#include<set>

using namespace std;

int T;


int main()
{

   int var;
   int temp;
   set<int> my_set;
   unsigned int count = 1;
   unsigned int factor = 2;
   unsigned int pre_var;

   cin>>T;

   while(T--)
   {
   	 cin>>var;

   	 if(var == 0){
   	 	cout<<"Case #"<<count<<": INSOMNIA"<<endl;
   	 	count++;
   	 	continue;
   	 }

     temp = var;

    while(my_set.size() != 10)
    {
       while(temp != 0)
        {
     	  my_set.insert(temp % 10);
     	  temp /= 10;
        }

        if(my_set.size() != 10){
          temp = var * (factor++);
          pre_var = temp;
        }
    }
    cout<<"Case #"<<count<<": "<<pre_var<<endl;
    count++;
    my_set.clear();
    factor = 2;
   }
   return 0;
}