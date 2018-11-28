#include<iostream>
#include<math.h>

using namespace std;


bool func(unsigned long long int num){
    unsigned long long int r,sum=0,temp,root;



    for(temp=num;num!=0;num=num/10){
         r=num%10;
         sum=sum*10+r;
    }


    if(temp!=sum)
        return false;


    if(temp==sum)
    {

      sum=0;

     for(num=sqrt(temp);num!=0;num=num/10){
         r=num%10;
         sum=sum*10+r;
    }

      if(sum == sqrt(temp))
        return true;
      else return false;

    //return true;
    //root = (unsigned long long) floor(sqrt(temp));





    }



    //return false;
}



int main()
{

    unsigned long long int test,a,b,i,count1,count2=1;



    cin>>test;

    while(test--)
    {
        cin>>a>>b;
        count1=0;

        for(i=a;i<=b;i++)
        {
            if(func(i)==true)
                count1++;
        }

        cout<<"Case #"<<count2++<<": "<<count1<<endl;


    }



return 0;
}
