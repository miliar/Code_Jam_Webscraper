#include<iostream>
//#include<conio.h>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{  fstream fin;
   ofstream fout;
   fin.open("input.txt");
   fout.open("output.txt");
    long long int a,b,m,k,l,n,c,count=0,j=0,i,cases,check=0,cou=0;
  long long  int *arr;
    fin>>cases;
    while(cases--)
    { count=0;j++;check=0;
       fin>>a>>n;
       arr=new long long int[n];
       for(i=0;i<n;i++)
       fin>>arr[i];
       sort(arr,arr+n);
       for(i=0;i<n;i++)
       {
          if(arr[i]<a) { a+=arr[i];continue;}
          c=count;
          cou=0;
          
             while(a<=arr[i])
             {
                a=a+a-1;
                cou++;
                if(cou>n-i){check=1;break;}
                count++;
             }
             if(check==1) break;
             else a+=arr[i];
          
       }
       if(check==1) fout<<"Case #"<<j<<": "<<c+n-i<<"\n";
       else fout<<"Case #"<<j<<": "<<count<<"\n";
       
     }
      fout.close();    
   // getch();
    return 0;
}
