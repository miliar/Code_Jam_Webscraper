#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;
int digits[10];
int turn;

int DetermineDigitCount(int x)
{
    // This bit could be optimised with a binary search
    return x < 10 ? 1
         : x < 100 ? 2
         : x < 1000 ? 3
         : x < 10000 ? 4
         : x < 100000 ? 5
         : x < 1000000 ? 6
         : x < 10000000 ? 7
         : x < 100000000 ? 8
         : x < 1000000000 ? 9
         : 10;
}


int ConvertToArrayOfDigits(int orig,int value,int turn,int cnt)
{
    int number=value;
    int val;

//    int size = DetermineDigitCount(value);
    while(value>0)
    {
        val = value % 10;
        digits[val]=1;
        value = value / 10;
    }
    //cout<<number;
     for(int i=0;i<10;i++)
        if(digits[i])cnt++;
   // cout<<"cnt="<<cnt<<endl;
     if(cnt==10)
         return number;
    else {
        if(number<=1000000)
        {
      //   printf("Multiplied %d and %d\n",orig,turn);
         number=orig*turn;
         turn++;

         ConvertToArrayOfDigits(orig,number,turn,0);
        }
        else
        return -1;
    }

}


int main()
{

    freopen("A-small-attempt1.in","r",stdin);
    freopen("output_file_name.out","w",stdout);

    int t;
    cin>>t;
    int num=1;
    memset(digits,0,10);

    while(num<=t)
    {

        int n,ret=0;
        cin>>n;
        turn=2;
         for(int i=0;i<10;i++)
            digits[i]=0;

         if(n==0)
            cout<<"Case #"<<num<<": "<<"INSOMNIA\n";
            else
            {
               ret = ConvertToArrayOfDigits(n,n,turn,0);
               if(ret==-1)
               cout<<"Case #"<<num<<": "<<"INSOMNIA\n";
               else
                cout<<"Case #"<<num<<": "<<ret<<endl;


            }
            num++;
    }
    return 0;

}

