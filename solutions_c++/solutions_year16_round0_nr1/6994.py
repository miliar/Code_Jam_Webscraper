#include<iostream>
#include<fstream>
#include<set>
using namespace std;
set<int> digits;
int arr[30],carry,n,in[7],test_cases,in_len,num;

inline void add()
{
    int sum,i,j;
    carry=0;
    for(i=29,j=6;(j>(6-in_len));i--,j--)
    {
        sum=arr[i]+in[j]+carry;
        if(sum>9)
        {
            arr[i]=sum%10;
            carry=sum/10;
        }
        else
        {
            arr[i]=sum;
            carry=0;
        }
    }

    while(carry!=0)
    {
        sum=arr[i]+carry;
        if(sum>9)
        {
            arr[i]=sum%10;
            carry=sum/10;
            i--;
        }
        else
        {
            arr[i]=sum;
            carry=0;
        }
    }
}

inline void process()
{
    int i;
    for(i=0;i<30;i++) arr[i]=0;

    while(digits.size()<10)
    {
        add();
        for(i=0;(i<30)&&(arr[i]==0);i++);
        for(;(i<30);i++) digits.insert(arr[i]);
    }
}

int main()
{
              ifstream fin("A-large.in");
              ofstream fout("A-large.out");
              long input_no;

              int i;

              fin>>test_cases;
              //cin>>test_cases;
              for(int k=1;k<=test_cases;k++)
              {
                  fin>>input_no;
                  //cin>>input_no;
                  in_len=0;num=6;

                  //Save INPUT number in an array
                  for(i=0;i<7;i++) in[i]=0;
                  while(input_no>0)
                  {
                      in[num]=input_no%10;
                      input_no/=10;
                      num--;
                      in_len++;
                  }

                  //clear set
                  digits.clear();

                  //cout<<"Case #"<<k<<": ";
                  fout<<"Case #"<<k<<": ";

                  //Process the answer now
                  if(in_len==0)
                    fout<<"INSOMNIA\n";//cout<<"INSOMNIA\n";
                  else
                  {
                      process();
                      for(i=0;(i<30)&&(arr[i]==0);i++);
                      for(;(i<30);i++) fout<<arr[i];//cout<<arr[i];
                      fout<<"\n";
                      //cout<<"\n";
                  }
              }
              fin.close();
              fout.close();
              return 0;
}
